import nltk
from nltk.tokenize import word_tokenize

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

def pos_tagging(text):
    tokens = word_tokenize(text)

    # Using NLTK's POS tagger with Penn Treebank tagset
    pos_tags_treebank = nltk.pos_tag(tokens)

    # Using NLTK's POS tagger with Universal tagset
    pos_tags_universal = nltk.pos_tag(tokens, tagset='universal')

    return pos_tags_treebank, pos_tags_universal

if __name__ == "__main__":
    text = input("Enter the text to apply POS tagging: ")
    pos_tags_treebank, pos_tags_universal = pos_tagging(text)

    print("POS Tags (Penn Treebank tagset):")
    print(pos_tags_treebank)

    print("\nPOS Tags (Universal tagset):")
    print(pos_tags_universal)