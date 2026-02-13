"""
👨‍💻 Stemming Task

Your goal is to:
1️⃣ Read the content of either story1.txt or story2.txt.
2️⃣ Apply regex with re.sub() to remove:
    - HTML tags (e.g. <div>...</div>)
    - URLs
    - Hashtags (#), asterisks (*), excessive punctuation (e.g. !!!, ???)
    - Extra whitespace

3️⃣ Tokenize the cleaned text into words using nltk.word_tokenize.
4️⃣ Remove stopwords using nltk.corpus.stopwords.
5️⃣ Apply stemming using nltk.stem.PorterStemmer to reduce each word to its root form.
6️⃣ Print out the list of stemmed words.

📌 Hints:
- Remember to import the required NLTK modules.
- Think about what patterns to use in your regex for URLs and HTML tags.
- Inspect intermediate results to ensure your cleaning is working!

Write your code below this string.
"""

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
import re

file = open("story1.txt")
text_from_file = file.read()
file.close()

# pattern = (
#     r'(?is)'
#     r'<[^>]+>'                              # HTML tags
#     r'|https?://\S+|www\.\S+'               # URLs
#     r'|#[A-Za-z0-9_]+'                      # hashtags like #tag
#     r'|[*#]+'                               # stray * or # runs
#     r'|[!?.,]{2,}'                          # excessive punctuation (e.g. !!!, ???, ..)
#     r'|\s+'                                 # extra whitespace
# )

# clean_text = re.sub(pattern, '', text_from_file)

# CLEAN_RE = re.compile(
#     r'(?is)'
#     r'<[^>]+>'                              # HTML tags
#     r'|https?://\S+|www\.\S+'               # URLs
#     r'|#[A-Za-z0-9_]+'                      # hashtags like #tag
#     r'|[*#]+'                               # stray * or # runs
#     r'|[!?.,]{2,}'                          # excessive punctuation (e.g. !!!, ???, ..)
#     r'|\s+'                                 # extra whitespace
# )

# def clean_text(s: str) -> str:
#     return CLEAN_RE.sub(' ', s).strip()

story_tokenized_by_sent = sent_tokenize(text_from_file)
print(clean_text)
