# 🧠 AI Chat Log Summarizer

This Python project summarizes user-AI chat logs stored in `.txt` files. It extracts the number of exchanges, identifies key topics using keywords, and uses OpenAI's GPT model to generate a one-sentence summary of each conversation.

---

## 📁 Project Structure

```
├── AI_chat_log_summarizer.py   # Main script to process and summarize chat logs
├── chat_logs/                  # Folder containing .txt chat log files
├── .env                        # (You must create this file with your own OpenAI key)
└── README.md                   # Project documentation
```

---

## 🚀 Features

- Counts total messages exchanged (User/AI)
- Extracts top keywords from the conversation
- Uses OpenAI GPT (via API) to generate a short summary of each chat log
- Outputs the summary in the terminal

---

## 🛠 Requirements

Make sure you have Python 3.7+ installed.

Install the required packages using:

```bash
pip install -r requirements.txt
```
---

## 🔐 API Key Setup

1. **Create a `.env` file** in the root directory of the project.
2. **Paste your own OpenAI API key** like this:

```env
OPENAI_API_KEY=your-api-key-here
```

## 📂 How to Use

1. Put all your `.txt` chat logs in the `chat_logs/` folder.  
   
2. Run the script:

```bash
python AI_chat_log_summarizer.py
```

