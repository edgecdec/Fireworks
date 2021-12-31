# Control show timer
scoreboard players enable @a[team=fireworks] fwshow
execute as @a[team=fireworks,scores={fwshow=1..}] run scoreboard players reset $fw.timer
execute as @a[team=fireworks,scores={fwshow=1..}] run scoreboard players operation $fw.show fwvar = @s fwshow
scoreboard players reset @a[team=fireworks,scores={fwshow=1..}] fwshow
execute as @a[team=fireworks,scores={fwshow=..-1}] run scoreboard players operation $fw.show fwvar = @s fwshow
scoreboard players reset @a[team=fireworks,scores={fwshow=..-1}] fwshow

execute if score $fw.show fwvar matches 1.. run scoreboard players add $fw.timer fwvar 1
execute if score $fw.show fwvar matches ..0 if score $fw.timer fwvar matches 1.. run scoreboard players set $fw.timer fwvar 0

# Shows
execute if score $fw.timer fwvar matches 1.. run title @a[team=fireworks] actionbar [{"text":"Fireworks Timer: ","color":"aqua"},{"score":{"objective":"fwvar","name":"$fw.timer"}}]
execute if score $fw.show fwvar matches 1..99 as @e[type=area_effect_cloud,tag=fwmarker] at @s run function fireworks:control/play_shows
execute if score $fw.show fwvar matches 100.. as @e[type=area_effect_cloud,tag=fwmarker] at @s run function fireworks:control/play_images

# Speed control
#execute as @a store result score @s fwspeed run attribute @s minecraft:generic.movement_speed get 10
#execute as @a if score @s fwspeed matches 2.. run attribute @s minecraft:generic.movement_speed base set 0.10000000149011612
