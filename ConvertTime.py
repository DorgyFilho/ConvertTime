#24-Hour Format to 12-Hour Format
def convertTime(h, m):
    conv = h/12
    if conv <= 1: #A.M ->> P.M
        H = str(h)
        print(f'Hour: {H}:', end='')
    elif conv > 1 and conv < 2:
        H2 = str(h-12) #P.M -->> A.M
        print(f'Hour: {H2}:', end='')
    else:
        print('Invalid Format!')

#Minutes
    if conv <= 1 and m <= 60:
        print(f'{m} A.M')
    elif conv > 1 and m <= 60:
        print(f'{m} P.M')
    else:
        print('Invalid Format')

while True:
    print('0 to Exit')
    h = int(input('Hour: '))
    if h == 0:
        print('Turn Off!')
        exit()
    m = int(input('Minute: '))
    
    convertTime(h,m)
