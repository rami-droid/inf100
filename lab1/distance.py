x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

dist = ((abs(x1 - x2))**2 +(abs(y1 - y2))**2)
dist = dist ** 0.5
print(f'Avstanden mellom ({x1}, {y1}) og ({x2}, {y2}) er {dist}')