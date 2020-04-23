from pynput import keyboard
import msvcrt
from os import system, name

keys = []
sortedKeys = []


class Key():
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount
        pass


def sorter(e):
    return e.amount


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def bar(a, b, c):
    return "".join([b for k in range(a)]+[c for k in range(10-a)])


def barrior():
    return str('\n'.join(
        [str(k.item) + "["+(bar(k.amount, "-", " ") if (k.amount < 150) else "....")+"] "+str(k.amount) for k in keys]))


def showArray():
    file1 = open("log.txt", "w+")
    # remove("log.txt")

    keys.sort(key=sorter)
    string = barrior()
    print(string)
    print(len(keys))
    file1.write(string)
    file1.write(len(keys))
    file1.close()


def searchAdd(array, item):
    i = 0
    isthere = False
    ind = -1
    for i in range(len(array)):
        if array[i].item == item:
            isthere = True
            ind = i
            pass
        pass

    if isthere:
        array[ind].amount += 1
        pass
    else:
        array.append(Key(item, 1))
        return len(array)-1

    return ind

# event listener


def on_release(key):

    try:
        k = key.char  # single-char keys
        clear()
        searchAdd(keys, key)
        showArray()
    except:
        # k = key.name  # other keys
        pass


listener = keyboard.Listener(on_release=on_release)
listener.start()
listener.join()


##########################

# while True:
#    file1 = open("log.txt", "a")
#    keys.sort(key=sorter)
###    string = barrior()
#  file1.write(string)
#  file1.close()
