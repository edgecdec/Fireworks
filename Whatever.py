import random
from Util import zipDir

COORDS = (0, 100, 0)
X_SPREAD = 50
Y_SPREAD = 20
Z_SPREAD = 50
REPEAT = 500
LIFETIME_SPREAD = 20

DEFAULT_SHOW_FILE_PATH = 'fireworks/data/fireworks/functions/shows'

fireworkList = []

with open('List Of Fireworks', 'r') as fireworks:

    for line in fireworks:
        if len(line) < 2:
            continue
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


def randomLocation(showFileName, xSpread = X_SPREAD, ySpread = Y_SPREAD, zSpread = Z_SPREAD, r = REPEAT,centerCoord = COORDS, lifetimeSpread = LIFETIME_SPREAD):
    with open(f'{DEFAULT_SHOW_FILE_PATH}/{showFileName}.mcfunction', 'w') as file:
        print(file.name)
        for line in range(1, r+1):
            x = centerCoord[0] + random.randint(-xSpread, xSpread)
            y = centerCoord[1] + random.randint(-ySpread, ySpread)
            z = centerCoord[2] + random.randint(-zSpread, zSpread)
            lifetime = random.randint(30-lifetimeSpread, 30+lifetimeSpread)
            fireworkType = random.choice(fireworkList)
            file.write(f'execute if score {showFileName} ShowTimer matches {line} run summon firework_rocket {x} {y} {z} '
                       f'{{LifeTime:{lifetime},FireworksItem:{fireworkType}}}\n')

for i in range(1,10):
    randomLocation(showFileName=f'july_4_show_{i}')

zipDir("fireworks/", "fireworks.zip")
