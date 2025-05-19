def read_chat_file(path):
    
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    file_path = 'chat.txt'
    data = read_chat_file(file_path)
    for line in data:
        print(line.strip())