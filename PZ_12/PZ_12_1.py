# Даны значения роста 20 юношей. Определить сколько юношей будут направлены
# в баскетбольную команду (рост от 190) и сколько в футбольную (остальные)

heights = [183, 185, 192, 198, 191, 188, 200, 185, 187, 189, 185, 180, 190, 200, 199, 193, 201, 198, 187, 195, 170, 180, 190, 200, 210]

basketball_count = 0
football_count = 0

for height in heights:
    if height >= 190:
        basketball_count += 1
    else:
        football_count += 1

print("в баскетбол:", basketball_count)
print("в футбол:", football_count)