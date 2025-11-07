import matplotlib.pyplot as plt
#SJØ

def plot_whatever(path):
    with open(path, "r", encoding="iso 8859-1") as f:
        content = f.read().splitlines()
        csv = [r.split(";") for r in content]
    east_water = []
    north_water = []

    east_land = []
    north_land = []
    print(csv[1][-6])

    for item in csv[2::]:
        if item[-6] == "LAND":
            east_land.append(float(item[-1]))
            north_land.append(float(item[-2]))

        else:
            east_water.append(float(item[-1]))
            north_water.append(float(item[-2]))
        
    plt.scatter(east_water, north_water)
    plt.scatter(east_land, north_land)
    plt.xlabel('east')
    plt.ylabel('north')


plot_whatever('Akvakulturregisteret.csv')
plt.show()
