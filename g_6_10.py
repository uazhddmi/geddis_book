import sys 

def write():
    while True:
        name = input("Enter player name: ")
        score = input('Enter score of the game: ')
        with open('player.txt', 'a') as file:
            file.write(name + ',' + score + '\n')

        cont = input('if you want proceed futher press any key, if you want exit - enter n: ')
        if cont == 'n':
            sys.exit()
        else:
            continue
        
def read():
    with open('player.txt', 'r') as file:
        for line in file.readlines():
            print(line, end='')

read()
