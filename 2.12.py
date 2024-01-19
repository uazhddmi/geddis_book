QA = 2000
IN_COST = 40.00
FI_COST = 42.75
COMIS = 0.03

st_sum = QA*IN_COST
fi_sum = QA*FI_COST
nd_com = fi_sum*COMIS
st_com = st_sum*COMIS
print(f'Initially {st_sum:.2f} $ was paid,\n\tComission to the broker was {st_com:.2f}')
print(f'Stakes wer sold for {fi_sum:.2f}$\ncomission to the broker was \t{nd_com:.2f} $')
print(f'Revenue {fi_sum - st_sum - st_com - nd_com} $ was received')
