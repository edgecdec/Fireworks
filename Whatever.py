with open('fireworks/data/fireworks/functions/shows/2021_22_show_1.mcfunction', 'w') as file:
    x = 0
    y = 100
    z = 0
    for line in range(1, 11):
        file.write(f'execute if score showTime ShowTimer1 matches {line} run summon firework_rocket {x} {y} {z} '
                   f'{{LifeTime:15,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Explosions:'
                   f'[{{Type:4,Flicker:0,Trail:0,Colors:[I;5554263,5407270,9576437,16607458],FadeColors:[I;14206582,1322348,9863818,16710712]}}],Flight:2}}}}}}}}\n')

