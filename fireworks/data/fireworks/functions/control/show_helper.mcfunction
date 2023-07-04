# Increment helper variable in scoreboard
scoreboard players add july_4_show_1 ShowTimer 1
function fireworks:shows/july_4_show_1
execute if score july_4_show_1 ShowTimer matches 1000 run scoreboard players set july_4_show_1 ShowTimer 0
