"""
👨‍💻 Lemmatization Task

Your goal is to:
1️⃣ Read the content of either story1.txt or story2.txt.
2️⃣ Apply regex with re.sub() to remove:
    - HTML tags (e.g. <div>...</div>)
    - URLs
    - Hashtags (#), asterisks (*), excessive punctuation (e.g. !!!, ???)
    - Extra whitespace

3️⃣ Tokenize the cleaned text into words using nltk.word_tokenize.
4️⃣ Remove stopwords using nltk.corpus.stopwords.
5️⃣ Tag each word with its part of speech using nltk.pos_tag.
6️⃣ Map POS tags to WordNet tags so the lemmatizer can use them.
7️⃣ Apply lemmatization using nltk.stem.WordNetLemmatizer, passing the correct POS.
8️⃣ Print out the list of lemmatized words.

📌 Hints:
- You’ll need a helper function to convert Treebank POS tags to WordNet POS tags.
- Check your intermediate outputs (POS tags, lemmatized results).

Write your code below this string.
"""
import nltk
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re

file = open("story2.txt")
text_from_file = file.read()
file.close()

CLEAN_PATTERN = (
    r'(?is)'
    r'<[^>]+>'                              # HTML tags
    r'|https?://\S+|www\.\S+'               # URLs
    r'|#[A-Za-z0-9_]+'                      # hashtags like #tag
    r'|[*#]+'                               # stray * or # runs
    r'|-{2,}'                               # repeated dashes ---
    r'|[!?.,]{2,}'                          # excessive punctuation
    r'|[^\x00-\x7F]+'                       # emojis & non-ASCII chars
    r'|\s+'                                 # extra whitespace
)

# def clean_text(s):
#     return CLEAN_RE.sub(' ', s).strip()

clean_text = re.sub(CLEAN_PATTERN, ' ', text_from_file)
clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # step 2
# print(clean_text)

story_tokenized_by_word = word_tokenize(clean_text)  # step 3
# print(story_tokenized_by_word)

stop_words = set(stopwords.words("english"))        # step 4
stopwords_removed = [word for word in story_tokenized_by_word if word not in stop_words]

# print(len(stopwords_removed))


from nltk import pos_tag                            # step 5

# Tag each word with its part of speech
tagged_words = pos_tag(stopwords_removed)

# print(tagged_words)



from nltk.corpus import wordnet                     # step 6

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun if unknown

from nltk.stem import WordNetLemmatizer             # step 7

lemmatizer = WordNetLemmatizer()

lemmatized_words_with_pos = [
    lemmatizer.lemmatize(word, get_wordnet_pos(pos_tag))
    for word, pos_tag in tagged_words
]

print(lemmatized_words_with_pos)
