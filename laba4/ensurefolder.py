import os


def ensure_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)

    print(f"Папка готова: {folder_name}")