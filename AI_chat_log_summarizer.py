import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('stopwords', force=True)

def read_chat_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except Exception as e:
        print("Error reading file:", e)
        return []

def split_messages(lines):
    user_msgs = []
    ai_msgs = []
    for line in lines:
        line = line.strip()
        if line.startswith("User:"):
            user_msgs.append(line[5:].strip())
        elif line.startswith("AI:"):
            ai_msgs.append(line[3:].strip())
    return user_msgs, ai_msgs

def count_messages(user_list, ai_list):
    return {
        'User': len(user_list),
        'AI': len(ai_list),
        'Total': len(user_list) + len(ai_list)
    }

def extract_keywords(texts, top_n=5):
    full_text = ' '.join(texts).lower()

    tokenizer = TreebankWordTokenizer()
    tokens = tokenizer.tokenize(full_text)

    stop_words = set(stopwords.words('english'))
    filtered = [word for word in tokens if word.isalpha() and word not in stop_words]

    return Counter(filtered).most_common(top_n)

def make_summary(stats, keywords):
    summary = []
    summary.append(f"Total exchanges: {stats['Total']}")
    summary.append(f"The User asked mainly about {keywords[0][0]} and its uses.")
    keyword_list = ', '.join([word for word, _ in keywords])
    summary.append(f"Most common keywords: {keyword_list}")
    return '\n'.join(summary)

if __name__ == '__main__':
    file_path = 'chat.txt'
    data = read_chat_file(file_path)
    user_msgs, ai_msgs = split_messages(data)
    stats = count_messages(user_msgs, ai_msgs)
    print("Stats:", stats)
    keywords = extract_keywords(user_msgs + ai_msgs)
    print("Keywords:", keywords)
    print(make_summary(stats, keywords))