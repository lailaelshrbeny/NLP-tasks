import nltk
from nltk.corpus import stopwords

def get_stopwords(language):
    nltk.download('stopwords')
    return stopwords.words(language)

if __name__ == "__main__":
    languages = ['english', 'spanish', 'french', 'german']
    
    for lang in languages:
        print(f"Common stop words in {lang}:")
        print(get_stopwords(lang))
        print()