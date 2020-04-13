from index import do_index
import os
import time

# save path of index file
index_path = r'D:\Dokumente\PycharmProjects\Patchouli\output\index.json'
# file path of root anime folder
anime_path = r'D:\Dokumente\PycharmProjects\Patchouli\test'


def show(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(.02)
    print("")
    time.sleep(1)


def commands(command):
    if command == 'exit!':
        show("Have a good day!")
        time.sleep(2)
        quit()
    elif command == 'help!':
        show("I can do")
        print("'help!'    -shows this message")
        print("'clean!'   -I'll clean the screen for you")
        print("'index!'   -I'll start indexing your anime library")
        print("'exit!'    -I'll be waiting for you!")
        time.sleep(1)
        mainloop()
    elif command == 'clean!':
        os.system('CLS')
        mainloop()
    else:
        show("I'm sorry, I don't know how to do this...")
        mainloop()


def mainloop():
    command = input("What do you want me to do? \n:>")
    commands(command)

if __name__ == '__main__':
    os.system('CLS')
    show("Hello. I'm Patchouli, the librarian of your anime collection!")
    show("If you want to know, what I'm able to do, please input 'help!' ")
    show("If you want to leave, enter 'exit!'\n")
    mainloop()
