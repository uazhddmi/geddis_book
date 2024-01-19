tm = int(input('Please enter time in seconds '))
MN = 60
HR = 3600
DAY = 86400
if tm >= DAY:
    day = tm // DAY
    hr = (tm % DAY)// HR
    mn = ((tm % DAY) % HR) //MN
    sc = ((tm % DAY) % HR) % MN
    print(f"Elsewhere your time is {day} days, {hr} hours, {mn} minutes and {sc} seconds")

elif HR <= tm < DAY :
    hr = tm // HR
    mn = (tm % HR) // MN
    sc = (tm % HR) % MN
    print(f"Elsewhere your time is {hr} hours, {mn} minutes and {sc} seconds")
elif MN <= tm < HR :
    mn = tm // MN 
    sc = tm % MN
    print(f"Elsewhere your time is {mn} minutes and {sc} seconds")
else:
    print(f"Elsewhere your time is still same {tm} seconds")
