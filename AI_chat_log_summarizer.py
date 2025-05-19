import os
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
nltk.download('stopwords', force=True)

def llm_summarize(text, filename):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""Summarize the main topic and purpose of this user-AI chat in one sentence:
    
    Chat from file {filename}:
    {text}

    Return a short summary like: "The user asked mainly about natural language processing and its applications."
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()

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

def process_file(file_path):
    data = read_chat_file(file_path)
    user_msgs, ai_msgs = split_messages(data)
    stats = count_messages(user_msgs, ai_msgs)
    keywords = extract_keywords(user_msgs + ai_msgs)
    chat_text="\n".join(data)
    summary_sentence=llm_summarize(chat_text,os.path.basename(file_path))
    
    return f""" Summary for file: {os.path.basename(file_path)}
    - The conversation had {stats['Total']} exchanges.
    - {summary_sentence}
    - Most common keywords: {', '.join([w for w, _ in keywords])}
    """

def process_folder(folder_path):
    print(f"Processing chat logs in folder: {folder_path}\n" + "-"*50)
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            summary = process_file(file_path)
            print(summary)
            print("-" * 50)

if __name__ == '__main__':
    folder_path = 'chat_logs'  
    process_folder(folder_path)
