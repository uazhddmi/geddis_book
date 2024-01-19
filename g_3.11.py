book_qtt = int(input('How many books did you buy this moths? '))

if book_qtt == 0:
    print(f'You bough {book_qtt} and received 0 points')
elif 2 <= book_qtt < 4:
    print(f'You bough {book_qtt} and received 5 points')
elif 4 <= book_qtt < 6:
    print(f'You bough {book_qtt} and received 15 points')
elif 6 <= book_qtt < 8:
    print(f'You bough {book_qtt} and received 30 points')
elif book_qtt >= 8:
    print(f'You bough {book_qtt} and received 60 points')
