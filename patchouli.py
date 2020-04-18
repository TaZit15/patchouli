from index import do_index
import os
import time
import json

# default paths
# save path of index file
index_path = r'D:\Dokumente\PycharmProjects\Patchouli\output\index.json'
settings_path = r'D:\Dokumente\PycharmProjects\Patchouli\settings.json'
# file path of root anime folder
anime_path = r'Z:\Serien\Anime'

def show(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(.02)
    print("")
    time.sleep(1)


def start_indexing():
    show("Indexing is experimental and has no use yet.")
    show("It also uses a lot of time.")
    show("Do you still want to continue? (y/n)")
    y_n = input(":>")
    if y_n == 'n' or 'no':
        mainloop()
    elif y_n == 'y' or 'yes':
        show(f"I'll start indexing your anime archive at {settings['Archive folder path']}")
        show(f"I'll save my index at {settings['Index save path']}")
        tic = time.perf_counter()
        do_index(index_path, anime_path, settings['Simulation mode'])
        toc = time.perf_counter()
        show(f"I finished indexing. It took {toc-tic:0.4f} seconds")
        mainloop()
    else:
        show("Please answer with y(es) or n(o)...")
        mainloop()


def show_settings():
    for setting, value in settings.items():
        print(f"{setting} == {value}")
    mainloop()

def change_settings(command):
    parsed = command.split(" ")

    # don't know why but
    # if parsed[3] == 'false' or 'False':
    # and
    # if parsed[3] == 'true' or 'true:
    # don't work so here is the ugly if chain...

    if parsed[3] == 'false':
        parsed[3] = False
    if parsed[3] == 'False':
        parsed[3] = False
    if parsed[3] == 'true':
        parsed[3] = True
    if parsed[3] == 'True':
        parsed[3] = True
    settings_list = [setting for setting in settings]
    setting_to_change = int(parsed[1])
    settings[settings_list[setting_to_change]] = parsed[3]
    with open(settings['2: Settings file path'], 'w') as f:
        json.dump(settings, f)
    show("Changed setting!")
    show_settings()


def commands(command):
    # i know i should use a dict or smth but this should be enough for now
    if command == 'exit!':
        show("Have a good day!")
        time.sleep(2)
        quit()
    elif command == 'help!':
        show("I can do")
        print("'help!'                            -shows this message")
        print("'clean!'                           -I'll clean the screen for you")
        print("'index!'                           -I'll start indexing your anime library")
        print('                                   # Caution, as this is experimental and uses a lot of time!')
        print("'settings!'                        -shows current settings")
        print("'change <setting number> to <option>'    -changes settings")
        print("'exit!'                            -I'll be waiting for you!")
        time.sleep(1)
        mainloop()
    elif command == 'clean!':
        os.system('CLS')
        mainloop()
    elif command == 'index!':
        start_indexing()
    elif command == 'settings!':
        show_settings()
    elif 'change' in command:
        change_settings(command)
    else:
        show("I'm sorry, I don't know how to do this (yet)...")
        mainloop()


def mainloop():
    command = input("What do you want me to do? \n:>")
    commands(command)

if __name__ == '__main__':
    try:
        # load settings file
        with open(settings_path) as f:
            settings = json.load(f)
    except FileNotFoundError:
        # create default settings file
        settings = {'0: Archive folder path': anime_path, '1: Index save path': index_path,
                    '2: Settings file path': settings_path, '3: Simulation mode': True}
        with open(settings_path, 'w') as f:
            json.dump(settings, f)
    os.system('CLS')
    show("Hello. I'm Patchouli, the librarian of your anime collection!")
    show("If you want to know, what I'm able to do, please input 'help!' ")
    show("If you want to leave, enter 'exit!'\n")
    mainloop()
