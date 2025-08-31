personer = int(input("hvor mange er dere på laget?"))
total = int(input('hvor mange twist er det i posen dere vant?'))

rest = total % personer

divisible = total - rest

amntPerson = int(divisible / personer)

print(f"det blir {amntPerson} twist til hver, og det blir {rest} twist til overs.")
