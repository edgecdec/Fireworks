import random

COORDS = (0, 20, 0)
X_SPREAD = 20
Y_SPREAD = 5
Z_SPREAD = 20
REPEAT = 500
LIFETIME_SPREAD = 15

fireworkList = []

with open('List Of Fireworks', 'r') as fireworks:

    for line in fireworks:
        line = f'\t{line[0:-1]}'
        lineArray = line.split("id:firework_rocket")
        if len(lineArray) == 1:
            lineArray = line.split('id:"firework_rocket"')
        if len(lineArray) == 1:
            lineArray = line.split("id:'firework_rocket'")
        if len(lineArray) != 2:
            continue
        line = lineArray[1]
        fireworkList.append(f'{{id:firework_rocket{line}')


def randomLocation(xSpread = X_SPREAD, ySpread = Y_SPREAD, zSpread = Z_SPREAD, r = REPEAT,centerCoord = COORDS, lifetimeSpread = LIFETIME_SPREAD):
    with open('fireworks/data/fireworks/functions/shows/2021_22_show_1.mcfunction', 'w') as file:
        for line in range(1, r+1):
            x = centerCoord[0] + random.randint(-xSpread, xSpread)
            y = centerCoord[1] + random.randint(-ySpread, ySpread)
            z = centerCoord[2] + random.randint(-zSpread, zSpread)
            lifetime = random.randint(0, lifetimeSpread + 1)
            fireworkType = random.choice(fireworkList)
            file.write(f'execute if score showTime ShowTimer1 matches {line} run summon firework_rocket {x} {y} {z} '
                       f'{{LifeTime:{lifetime},FireworksItem:{fireworkType}}}\n')


randomLocation()