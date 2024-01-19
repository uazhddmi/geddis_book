def readfile():
    d_w = {}
    set_w = set()
    with open('text.txt', "r") as file:
        for line in file.readlines():
            for word in line.rstrip().split():
                if word.endswith((',', '.', '!', '?')):
                    set_w.add(word[:-1])
                else:
                    set_w.add(word)
                d_w[word] = d_w.get(word, 0) + 1

    return sorted(set_w), len(set_w)

print(readfile())