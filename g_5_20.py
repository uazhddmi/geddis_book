import random


def gess_procedure(n):
    '''ask user to gess randomly generated number, provide feedback for correction,
    additionatlly count quantitiy of stabs'''
    count = 0
    while True:
        num = int(input('What do you think what number I've choosen : '))
        if num > n:
            print('Too much, try one more time')
            count += 1
        elif num < n:
            print('Too less, try one more time')
            count += 1
        else:
            return f'Well done, you made {count} stabs'

def main():
    game = None
    while game != 'end':
        n = random.randint(1,101)# generated number which should be gessed
        print(gess_procedure(n))
        game =input('If you want to finish, type \'end\' ')

if __name__ == '__main__':
    main()