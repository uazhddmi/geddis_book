def count_uniq_words():
    d_w = {}
    with open('text.txt', "r") as file:
        for line in file.readlines():
            for word in line.rstrip().split():
                if word.endswith((',', '.', '!', '?')):
                    d_w[word[:-1]] = d_w.get(word[:-1], 0) + 1
                else:
                    d_w[word] = d_w.get(word, 0) + 1


    return d_w

dict_w = count_uniq_words()

print(format('слово', '15'),'\t',format('появления','15'))
print('----------------------------------------------')
while len(dict_w)>0:
    pair = dict_w.popitem()
    print(format(pair[0],'15'), format(pair[1], '15'))