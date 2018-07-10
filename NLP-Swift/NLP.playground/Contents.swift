import Foundation

//https://medium.com/swiftworld/swift-world-whats-new-in-ios-11-natural-language-processing-2a16b7422334

debugPrint("*****************************************")
debugPrint("*****************************************")
debugPrint("*****************************************")
// Enumerating string
var string : String = "The American Red Cross was established in Washington, D.C., by Clara Barton."
var range = NSRange(location:0, length: string.utf16.count)
var tagger : NSLinguisticTagger = NSLinguisticTagger.init(tagSchemes: [.tokenType], options: 0)
var options : NSLinguisticTagger.Options = [.omitPunctuation]
tagger.string = string
tagger.enumerateTags(in: range, unit: .word, scheme: .tokenType, options: options) { (tag, tokenRange, stop) in
    if let tag = tag {
        let name = (string as NSString).substring(with: tokenRange)
        print("\(name): \(tag)")
    }
}

debugPrint("*****************************************")
debugPrint("*****************************************")
debugPrint("*****************************************")
// Language Identification
tagger = NSLinguisticTagger(tagSchemes: [.language], options: 0)
string = "WWDC 2017 已经结束了。"
tagger.string = string
if let language = tagger.dominantLanguage {
    print(language)
} else {
    print("can't get domainant language")
}

debugPrint("*****************************************")
debugPrint("*****************************************")
debugPrint("*****************************************")
//Tokenization
string = "The American Red Cross was established in Washington, D.C., by Clara Barton."
range = NSRange(location:0, length: string.utf16.count)
tagger = NSLinguisticTagger.init(tagSchemes: [.tokenType, .nameType], options: 0)
tagger.string = string
options = [.omitPunctuation, .omitWhitespace, .joinNames]
let tags: [NSLinguisticTag] = [.personalName, .placeName, .organizationName]
tagger.enumerateTags(in: range, unit: .word, scheme: .nameType, options: options) { tag, tokenRange, stop in
    if let tag = tag, tags.contains(tag) {
        let name = (string as NSString).substring(with: tokenRange)
        print("\(name): \(tag)")
    }
}

