import os
import shutil

'''
    Sometimes you have some folders that have some PDFs inside
    but you don't know how to study these PDFs, becuase
    it is not arranged based on some order, but the only
    thing that arranged is the root folders themselves.
    so this SCRIPT aims to rename that PDFs based on 
    their root folders, then move these pdf in another folder
    to help you to study for them sequentially.

    `Move the script to the root folder of the course and run it.`
'''

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder_name = input("Enter the name of the final folder: ")
PDF_DIR = os.path.join(BASE_DIR, folder_name)


def rearrange(path):
    for filename in os.listdir(BASE_DIR):
        if filename[0].isdigit():
            new_dir = os.chdir(os.path.join(BASE_DIR, filename))
            for file in os.listdir(new_dir):
                if file.lower().endswith('.pdf'):
                    print(file)
                    os.rename(file, f"{filename}.pdf")
                    os.makedirs(PDF_DIR, exist_ok=True)
                    shutil.move(file, PDF_DIR)


if __name__ == "__main__":
    rearrange(BASE_DIR)
