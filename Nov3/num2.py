favCar = {
    'JJ' : ['Golf', 'Camry', 'LFA'],
    'Nicklas' : ['Innova', 'Panther', 'Fortuner'],
    'Moreno' : ['CRV','Avanza','Jazz'],
    'Sebastian' : ['City','Terios','Altis'],
    'Greg' : ['HRV','Civic','Accord']
}

def printDict():
    for name in favCar:
        print(name, 'likes these cars:')
        for i in range(3):
            print("- ", favCar[name][i])
        print()

printDict()