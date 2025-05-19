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

if __name__ == '__main__':
    file_path = 'chat.txt'
    data = read_chat_file(file_path)
    user_msgs, ai_msgs = split_messages(data)
    stats = count_messages(user_msgs, ai_msgs)
    print("Stats:", stats)