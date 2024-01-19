def read_file(file):
    result = set()
    with open(file, 'r') as f:
        for line in f.readlines():
            for word in line.rstrip().split():
                if word.endswith((',', '.', '?', '!')):
                    result.add(word[:-1])
                else:
                    result.add(word)

    return result


def print_result(w_lst: set):
    w_lst= sorted(tuple(w_lst))
    print('\t', end='')
    for word in w_lst[:-1]:
        print(word, end=', ')
    print(w_lst[-1])

def main():
    file1 = read_file('first_file.txt')
    file2 = read_file('second_file.txt')

    print('Unick words in both files')
    print_result(file1 | file2)

    print('Unick words that are present at both files')
    print_result(file1 & file2)

    print('Unick words in 1st file with extraction words from 2nd file')
    print_result(file1 -  file2)

    print('Unick words in 2nd file with extraction words from 1st file')
    print_result(file2 - file1)

    print('Words either from 1st file or from 2nd file, but neither in both')
    print_result(file1 ^ file2)

if __name__ == "__main__":
    main()