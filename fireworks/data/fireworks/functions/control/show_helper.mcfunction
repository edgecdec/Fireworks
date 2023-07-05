# Increment helper variable in scoreboard
scoreboard players add july_4_show ShowTimer 1
function fireworks:shows/july_4_show_1
function fireworks:shows/july_4_show_2
function fireworks:shows/july_4_show_3
function fireworks:shows/july_4_show_4
function fireworks:shows/july_4_show_5
function fireworks:shows/july_4_show_6
function fireworks:shows/july_4_show_7
function fireworks:shows/july_4_show_8
function fireworks:shows/july_4_show_9
function fireworks:shows/july_4_show_10
execute if score july_4_show ShowTimer matches 10000 run scoreboard players set july_4_show_1 ShowTimer 0
