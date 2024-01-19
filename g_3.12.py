box_qtt = int(input('How many boxes do you want to buy? '))
PR = 99
if box_qtt < 10:
    D1 = 0
    disk_pr = PR*(1-D1)
    print(f'You\'r going to buy {box_qtt}, you discont is {D1*box_qtt}$. Total cost  is {box_qtt*disk_pr}$')
elif 10 <= box_qtt < 20:
    D2 = 0.1
    disk_pr = PR*(1-D2)
    print(f'You\'r going to buy {box_qtt}, you discont is {D2*PR*box_qtt}$. Total cost  is {box_qtt*disk_pr}$')
elif 20 <= box_qtt < 50:
    D3 = 0.2
    disk_pr = PR*(1-D3)
    print(f'You\'r going to buy {box_qtt}, you discont is {D3*PR*box_qtt}$. Total cost  is {box_qtt*disk_pr}$')
elif 50 <= box_qtt < 100:
    D4 = 0.3
    disk_pr = PR*(1-D4)
    print(f'You\'r goinjg to buy {box_qtt}, you discont is {D4*PR*box_qtt}$. Total cost  is {box_qtt*disk_pr}$')
else:
    D5 = 0.4
    disk_pr = PR*(1-D5)
    print(f'You\'r goinjg to buy {box_qtt}, you discont is {D5*PR*box_qtt}$. Total cost  is {box_qtt*disk_pr}$')
