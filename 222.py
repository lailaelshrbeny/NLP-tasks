import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data if not already present
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Read the CSV file
file_path = 'text_summarization.csv'  
data = pd.read_csv(file_path)

# Concatenate all text data into a single string
all_text = ' '.join(data['category'])  

# Tokenize the text into sentences
sentences = sent_tokenize(all_text)

# Tokenize and remove stopwords from each sentence
stop_words = set(stopwords.words('english'))
clean_sentences = []
for sentence in sentences:
    words = word_tokenize(sentence)
    words = [word.lower() for word in words if word.isalnum()]
    words = [word for word in words if word not in stop_words]
    clean_sentences.append(' '.join(words))

# Calculate TF-IDF scores
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(clean_sentences)

# Calculate cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Generate summary
summary_sentences = []
similarity_threshold = 0.5  # Adjust the threshold as needed
for i in range(len(sentences)):
    if cosine_sim[i].mean() > similarity_threshold:
        summary_sentences.append(sentences[i])

summary = ' '.join(summary_sentences)

# Print the summary
print(summary)