# run this to install all the requirements for the project
import os

if os.name == "nt":
    os.system(f'cmd /c "pip install -r requirements.txt > out.txt"')
    with open("out.txt") as W:
        text = W.read()
        print(text)
else:
    os.system('cmd /c "pip3 install -r requirements.txt > out.txt"')
    with open("out.txt") as W:
        text = W.read()
        print(text)

input("Press enter to exit...")