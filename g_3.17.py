print('Reboot your computer and try to connect')
answ = input('Did it solved problem (y/n)? ')
if answ == 'y':
    print('Well done, thank you for cooperation')
else:
    print('Reboot router and try to connect')
    answ = input('Did it solved problem (y/n)? ')
    if answ == 'y':
        print('Well done, thank you for cooperation')
    else:
        print('Make sure that cables are connected')
        answ = input('Did it solved problem (y/n)? ')
        if answ == 'y':
            print('Well done, thank you for cooperation')
        else:
            print('Bring your router to a new place')
            answ = input('Did it solved problem (y/n)? ')
            if answ == 'y':
                print('Well done, thank you for cooperation')
            else:
                print('Take a new router')
