import string as st

PN = tuple(st.punctuation)
def main():
    file = 'Kennedy.txt'

    with open(file, 'r') as raws:
        word_list = [i.strip().lower() for i in raws.readlines()]

    un_word_list = get_unick_words(word_list)
    result = find_word(un_word_list, word_list)
    write_file(result)
def get_unick_words(wl: list) -> set:
    result = []
    for line in wl:
        for word in line.split():
            if word[-1] in PN:
                result.append(word[:-1])
            else:
                result.append(word)
    return set(result)


def find_word(un_w: set, wl: list) -> dict:
    d_result = {}
    for word in un_w:
        d_result[word] = []
        for i in range(len(wl)):
            if word in wl[i].split():
                d_result[word].append(i + 1)
            else:
                continue

    return sorted(d_result.items())


def write_file(count_lines):
    with open('output.txt', 'w') as output:
        for i in count_lines:
            output.write(i[0] + ':')
            for y in i[1]:
                output.write(' ' + str(y))
            output.write('\n')


if __name__ == '__main__':
    main()


















