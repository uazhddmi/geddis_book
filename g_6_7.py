import random
from tkinter.ttk import Separator
quant_num = int(input('Enter how much numbers you need to generate: '))
with open('random_numbers.txt', 'w') as f:
    for i in range (quant_num):
        f.write('%d \n' % random.randint(1, 500))

