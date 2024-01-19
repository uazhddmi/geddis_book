tc = float(input('You bought meals for $'))
TX = 0.07
TIP = 0.18
tx = tc*TX
tips = (tx+tc)*TIP

print(f'You bought meal for {tc+tx+tips:.2f} with {tx:.2f}$ tax and {tips:.2f} $ tips included')
