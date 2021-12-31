scoreboard players set @a[tag=!ujoin] ujoin 1
execute as @a[scores={ujoin=1}] run function fireworks:information/welcome
scoreboard players add @a[scores={ujoin=1..199}] ujoin 1
execute as @a[scores={ujoin=200}] run function fireworks:information/help