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

