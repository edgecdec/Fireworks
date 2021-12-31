scoreboard objectives add fwvar dummy
scoreboard objectives add ujoin minecraft.custom:minecraft.leave_game
team add NoCollision
team modify NoCollision collisionRule never

# Fireworks
team add fireworks
scoreboard objectives add fwshow trigger
execute unless score $fw.show fwvar matches -2147483648..2147483647 run scoreboard players set $fw.show fwvar 0
execute unless score $fw.timer fwvar matches -2147483648..2147483647 run scoreboard players set $fw.timer fwvar 0

# Minemarch
#execute if score $fw.minemarch.enabled fwvar matches 1.. run function fireworks:minemarch/enable
#execute unless score $fw.minemarch.enabled fwvar matches 1.. run function fireworks:minemarch/disable