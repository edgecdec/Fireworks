# Firework marker
kill @e[type=area_effect_cloud,tag=fwmarker]
execute at @s[y_rotation=-45..44] align xyz positioned ~0.5 ~ ~0.5 run summon area_effect_cloud ~ ~ ~ {Rotation:[0.0f,0.0f],Age:-2147483648,Duration:-1,WaitTime:-2147483648,Tags:[fwmarker]}
execute at @s[y_rotation=45..134] align xyz positioned ~0.5 ~ ~0.5 run summon area_effect_cloud ~ ~ ~ {Rotation:[90.0f,0.0f],Age:-2147483648,Duration:-1,WaitTime:-2147483648,Tags:[fwmarker]}
execute at @s[y_rotation=135..224] align xyz positioned ~0.5 ~ ~0.5 run summon area_effect_cloud ~ ~ ~ {Rotation:[180.0f,0.0f],Age:-2147483648,Duration:-1,WaitTime:-2147483648,Tags:[fwmarker]}
execute at @s[y_rotation=225..314] align xyz positioned ~0.5 ~ ~0.5 run summon area_effect_cloud ~ ~ ~ {Rotation:[270.0f,0.0f],Age:-2147483648,Duration:-1,WaitTime:-2147483648,Tags:[fwmarker]}

# Music marker
kill @e[type=armor_stand,tag=music_marker]
execute at @s align xyz positioned ~0.5 ~ ~0.5 run summon armor_stand ~ 0 ~ {Marker:1b,Invulnerable:1b,Invisible:1b,Silent:1b,NoGravity:1b,NoBasePlate:1b,DisabledSlots:4144959,Tags:[music_marker]}
