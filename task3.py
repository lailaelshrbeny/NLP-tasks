import spacy

def tokenize_text(text, language):
    nlp = spacy.blank(language)
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

if __name__ == "__main__":
    text = input("Enter the text to tokenize: ")
    language = input("Enter the language of the text (e.g., 'fr' for French, 'de' for German): ")
    tokenized_sentences = tokenize_text(text, language)
    print("Tokenized Sentences:")
    for sentence in tokenized_sentences:
        print(sentence)
