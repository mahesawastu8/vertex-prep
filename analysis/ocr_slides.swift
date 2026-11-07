import Foundation
import PDFKit
import Vision
import AppKit

struct Slide: Codable {
    var lecture: String
    var lecturer: String
    var slide: Int
    var n: Int
    var text: String
    var chars: Int
    var ocr: String?
}

let dir = "/Users/dimaswastu/VERTEX-PREP/analysis"
let sPath = "\(dir)/bdt_slides.json"
let data = try! Data(contentsOf: URL(fileURLWithPath: sPath))
var slides = try! JSONDecoder().decode([Slide].self, from: data)

var docs: [String: PDFDocument] = [:]
var count = 0
for i in 0..<slides.count {
    if slides[i].chars >= 80 { continue }
    let lec = slides[i].lecture
    if docs[lec] == nil {
        let p = "\(dir)/lectures/7 (BDT)/\(lec).pdf"
        docs[lec] = PDFDocument(url: URL(fileURLWithPath: p))
    }
    guard let doc = docs[lec], let page = doc.page(at: slides[i].slide - 1) else { continue }
    let img = page.thumbnail(of: NSSize(width: 1600, height: 1200), for: .mediaBox)
    guard let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { continue }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    try? VNImageRequestHandler(cgImage: cg).perform([req])
    let txt = (req.results ?? []).compactMap { $0.topCandidates(1).first?.string }.joined(separator: " ")
    slides[i].ocr = txt
    if txt.count > slides[i].chars {
        slides[i].text = (slides[i].text + " " + txt).trimmingCharacters(in: .whitespaces)
    }
    count += 1
}
let out = try! JSONEncoder().encode(slides)
try! out.write(to: URL(fileURLWithPath: sPath))
print("OCR selesai untuk \(count) slide minim-teks")
