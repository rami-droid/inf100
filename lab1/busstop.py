house_number = int(input('Husnummer: \n'))

nearest_stop = ((house_number + 3) // 7) * 7

print(f'Nærmeste busstopp er ved nummer {nearest_stop}')