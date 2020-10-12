print('du sover: \n\tvakna\n\tfortsätt sova')
exist = input('vad gör du?').lower() [0]

if exist == 'v':
    print('du tar dig ur sängen och åker till skolan')

elif exist == 'f':
    print('du missar bussen och får frånvaro')
    frånvaro = input('ska du ta dig till skolan [ja/nej]').lower()
    if frånvaro [0] == 'j':
        print('okej bra')
    elif frånvaro [0] == 'n':
        print('jaha.')
else: 
    print('ZZZzzz')
