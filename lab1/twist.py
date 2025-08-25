personer = int(input('hvor mange personer er dere? '))
total = int(input('hvor mange twist i posen? '))

rest = total % personer

divisible = total - rest

amntPerson = int(divisible / personer)

print(f"det blir {amntPerson} twist til hver, og det blir {rest} twist til overs.")
