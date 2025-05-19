def read_chat_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except Exception as e:
        print("Error reading file:", e)
        return []

if __name__ == '__main__':
    file_path = 'chat.txt'
    data = read_chat_file(file_path)
    for line in data:
        print(line.strip())