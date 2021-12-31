import random

# Return one 24-bit color value 
def rgbToColor(r, g, b):
    return (r << 16) + (g << 8) + b

stop = 0
file = open('10.mcfunction', 'w')
for i in range(1000000):
#    file.write
    time = random.randint(1,1)
    stop = stop + time
    x = random.randint(0,20)
    y = random.randint(0,15)
    z = random.randint(0,15)
    num = random.randint(0,1)
    randneg = ''
    if num == 1:
        randneg = '-'
    lifetime = random.randint(20,60)
    flicker = random.randint(0,1)
    trail = random.randint(0,1)
    type = random.randint(0,5)
    color_count = random.randint(1,4)
    colors = []
    fadeColors = []
    for i in range(color_count):
        colors.append(str(random.randint(0,16777215)))
        fadeColors.append(str(random.randint(0,16777215)))
    colors = ",".join(colors)
    fadeColors = ",".join(fadeColors)
    file.write('execute if score $fw.timer fwvar matches '+str(stop)+' positioned ^'+randneg+str(x)+' ^'+randneg+str(y)+' ^'+randneg+str(z)+' run summon firework_rocket ~ ~ ~ {LifeTime:'+str(lifetime)+',FireworksItem:{id:"firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Type:'+str(type)+',Flicker:'+str(flicker)+',Trail:'+str(trail)+',Colors:[I;'+colors+'],FadeColors:[I;'+fadeColors+']}],Flight:2}}}}\n')
    if stop > 24000:
        break


def get_random_choice():
    c1 = random.randint(0,1)
    if c1 == 0:
        return rgbToColor(random.randint(249,255), random.randint(194-5,194+5), random.randint(26-5,26+5))
    else:
        return rgbToColor(random.randint(75-5,75+5), random.randint(46-5,46+5), random.randint(131-5,131+5))

"""
stop = 0
file = open('8.mcfunction', 'w')
for i in range(1000000):
#    file.write
    time = random.randint(1,4)
    stop = stop + time
    x = random.randint(0,20)
    y = random.randint(0,15)
    z = random.randint(0,15)
    num = random.randint(0,1)
    randneg = ''
    if num == 1:
        randneg = '-'
    lifetime = random.randint(20,60)
    flicker = random.randint(0,1)
    trail = random.randint(0,1)
    type = random.randint(0,5)
    color_count = random.randint(1,4)
    colors = []
    fadeColors = []
    for i in range(color_count):
        colors.append(str(get_random_choice()))
        fadeColors.append(str(get_random_choice()))
    colors = ",".join(colors)
    fadeColors = ",".join(fadeColors)
    file.write('execute if score $fw.timer fwvar matches '+str(stop)+' positioned ^'+randneg+str(x)+' ^'+randneg+str(y)+' ^'+randneg+str(z)+' run summon firework_rocket ~ ~ ~ {LifeTime:'+str(lifetime)+',FireworksItem:{id:"firework_rocket",Count:1,tag:{Fireworks:{Explosions:[{Type:'+str(type)+',Flicker:'+str(flicker)+',Trail:'+str(trail)+',Colors:[I;'+colors+'],FadeColors:[I;'+fadeColors+']}],Flight:2}}}}\n')
    if stop > 1200:
        break
"""
