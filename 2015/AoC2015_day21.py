import math as m

boss_hp = 109
boss_dmg = 8
boss_arm = 2

player_hp = 100

weapons = [
    [8, 4, 0],
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0]
]

armors = [
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 4],
    [102, 0, 5],
    [0, 0, 0]
]

rings = [
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3],
    [0, 0, 0]
]


def player_win(dmg, arm):
    d1 = max(dmg - boss_arm, 1)
    d2 = max(boss_dmg - arm, 1)
    return True if m.ceil(boss_hp/d1) <= m.ceil(player_hp/d2) else False


cost = 0

for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in rings:
                if ring2 != [0, 0, 0] and ring2 == ring1:
                    continue
                if not player_win(weapon[1]+ring1[1]+ring2[1], armor[2]+ring1[2]+ring2[2]):
                    cost = max(cost, weapon[0]+armor[0]+ring1[0]+ring2[0])

print(cost)
