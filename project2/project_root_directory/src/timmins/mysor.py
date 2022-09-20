import os
import sys
from pathlib import Path

def main():
    path = sys.argv[1]#r'C:\Users\Asus\Desktop\clean'
    if len(sys.argv) < 2:
        raise ValueError('empty path')
    if not (os.path.exists(path) and Path(path).is_dir()):
        raise ValueError('incorrect path')

    cleaner(path)
    print(':)')
def cleaner(path):
    items = os.listdir(path)#C:\Users\Asus\Desktop\sor
    for file in items:
        try:
            if file.endswith('.jpg') or file.endswith('.png'):
                os.remove(os.path.join(path, file))
                print(f'Image delete: {file}')
        except FileNotFoundError:
            continue
if __name__ == "__main__":
    main()

#python mysor.py C:\Users\Asus\Desktop\sor| cd \Users\Asus\Desktop\Projects
