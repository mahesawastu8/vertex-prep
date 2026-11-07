import Foundation
import PDFKit
import AppKit

let args = CommandLine.arguments
guard args.count >= 3 else { exit(1) }
let pdfPath = args[1]
let outDir = args[2]

let url = URL(fileURLWithPath: pdfPath)
guard let doc = PDFDocument(url: url) else { exit(1) }

let fm = FileManager.default
try? fm.createDirectory(atPath: outDir, withIntermediateDirectories: true, attributes: nil)

for i in 0..<doc.pageCount {
    let outPath = "\(outDir)/slide_\(i + 1).jpg"
    if fm.fileExists(atPath: outPath) { continue }
    guard let page = doc.page(at: i) else { continue }
    let pageRect = page.bounds(for: .mediaBox)
    let scale: CGFloat = 1.4
    let size = NSSize(width: pageRect.width * scale, height: pageRect.height * scale)
    let img = page.thumbnail(of: size, for: .mediaBox)
    guard let tiff = img.tiffRepresentation,
          let rep = NSBitmapImageRep(data: tiff),
          let jpg = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.82]) else { continue }
    try? jpg.write(to: URL(fileURLWithPath: outPath))
}
print("Rendered \(doc.pageCount) slides to \(outDir)")
