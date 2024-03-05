import os
import json


def get_usernames(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        parsed_data = json.load(file)
    return [item['username'] for item in parsed_data['data']]

def filter(content):
    keywords = ["Bitcoin", "BTC", "NFT", "cryptocurren", "DeFi", "Crypto", "ICO", "Ethereum", "Altcoin", "Happy", "$"]
    for keyword in keywords:
        if keyword in content:
            return True
    return False

def process_file(file_name, name):
    encodings = ["utf-8", "gbk", "ascii"]
    for encoding in encodings:
        try:
            with open(file_name, 'r', encoding=encoding, errors='ignore') as file:
                content = file.read()
                if filter(content):
                    with open("filtered_output_by" + name + ".txt", 'a', encoding='utf-8') as store:
                        store.write(f"{content}\n")
                        break
        except UnicodeDecodeError:
            continue

def traverse_folder(folder_path, name):
    for root, dirs, files in os.walk(folder_path, topdown=True):
        for file_name in files:
            if file_name.endswith(".md"):
                file_path = os.path.join(root, file_name)
                process_file(file_path, name)

if __name__ == "__main__":
    current_path = os.getcwd()
    names = get_usernames(os.path.join(current_path, "bignames.json"))
    for name in names:
        folder_path = current_path + "\\output_from_" + name
        traverse_folder(folder_path, name)