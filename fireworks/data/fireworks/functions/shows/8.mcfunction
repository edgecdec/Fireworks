# Add show events below
# To position fireworks, use ^ ^ ^
# Arguments are Left/Right, Up/Down, Forward/Backward offset from the marker
execute if score $fw.timer fwvar matches 1 positioned ^ ^ ^ run function fireworks:firework/example
