def main():

    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print("All rings are done")

def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print(f'Move ring from peg {from_peg} to {to_peg}')
        move_discs(num - 1, temp_peg, to_peg, from_peg)

if __name__ == '__main__':
    main()
