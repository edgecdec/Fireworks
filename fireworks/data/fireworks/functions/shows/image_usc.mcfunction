execute if score $fw.timer fwvar matches 15 at @e[type=area_effect_cloud,tag=fwmarker] positioned ^ ^15 ^ run function fireworks:firework/image_usc
execute if score $fw.timer fwvar matches 15.. run scoreboard players set $fw.timer fwvar 0