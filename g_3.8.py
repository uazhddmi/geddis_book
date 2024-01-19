BREAD_PACK = 8
SOS_PACK = 10
people = int(input('How many people will you invite (number)? '))
qt_hpp = int(input('How many hod-dogs per person will be needed? '))
quant = people*qt_hpp
if quant <= BREAD_PACK:
    q_of_bp = 1
else:
    if quant %  BREAD_PACK == 0:
        q_of_bp = quant // BREAD_PACK 
    else:
        q_of_bp = quant // BREAD_PACK + 1
if quant <= SOS_PACK:
    q_of_sp = 1
else:
    if quant % SOS_PACK ==0:
        q_of_sp = quant // SOS_PACK
    else:
        q_of_sp = quant // SOS_PACK + 1

s_left = q_of_sp*SOS_PACK - quant
b_left = q_of_bp*BREAD_PACK - quant
print(f"You will need {q_of_bp} pack(s) of bread, and {q_of_sp} pack(s) of sosidges")
print(f'After party there will {b_left} breads and {s_left} sosidges left')
