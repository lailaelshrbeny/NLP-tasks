import nltk

def tokenize_words(text):
    return nltk.word_tokenize(text)

def tokenize_sentences(text):
    return nltk.sent_tokenize(text)

def split_text(text):
    return text.split()

def main():
    text = input("Enter the text: ")
    choice = int(input("Choose one of the following options:\n1. Tokenize words\n2. Tokenize sentences\n3. Split text\n"))

    if choice == 1:
        print(tokenize_words(text))
    elif choice == 2:
        print(tokenize_sentences(text))
    elif choice == 3:
        print(split_text(text))
    else:
        print("Invalid choice")

main()