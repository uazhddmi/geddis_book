import random

CH1 = 'stone'
CH2 = 'scissors'
CH3 = 'paper'


def random_choice():
    num = random.randint(1, 4)
    if num == 1:
        ch = CH1
    elif num == 2:
        ch = CH2
    else:
        ch = CH3
    return ch


def u_choice(num: int):
    if num == 1:
        ch = CH1
    elif num == 2:
        ch = CH2
    else:
        ch = CH3
    return ch


def game(c_ch, u_ch):
    if c_ch == CH1 and u_ch == CH2 or c_ch == CH2 and u_ch == CH3 or c_ch == CH3 and u_ch == CH1:
        print("Computer won")
    elif u_ch == CH1 and c_ch == CH2 or u_ch == CH2 and c_ch == CH3 or u_ch == CH3 and c_ch == CH1:
        print("You win")
    else:
        print('You are equal. You should play again')
        main()


def main():
    u_ch = int(input('Make you choice: \n\t\t1. stone \n\t\t2. scissors\n\t\t3. paper\n?>'))
    u_ch = u_choice(u_ch)  # transform user's number to a string
    print(f'Your choice is: ', u_ch)
    c_ch = random_choice()
    print("Computer chosen", c_ch)
    game(c_ch, u_ch)


if __name__ == '__main__':
    main()
