boss_hp = 55
boss_dmg = 8

player_hp = 50
player_mp = 500

spells = {
    "mm": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229
}


class Combatant:
    def __init__(self, hp):
        self.hp = hp
    mp = player_mp
    dmg = 8
    armor = 0
    poison = 0
    shield = 0
    recharge = 0

    def progress(self):
        self.hp -= 3 if self.poison else 0
        self.armor = 7 if self.shield else 0
        self.mp += 101 if self.recharge else 0

        self.poison = max(self.poison - 1, 0)
        self.shield = max(self.shield - 1, 0)
        self.recharge = max(self.recharge - 1, 0)


def mp_cost(spell_list):
    return sum([spells[spell] for spell in spell_list])


def player_win(spell_list):
    log = []
    player = Combatant(player_hp)
    boss = Combatant(boss_hp)
    turn = 0
    for spell in spell_list:
        turn += 1
        # Player turn
        player.hp -= 1
        if player.hp <= 0:
            log.append("Player died to hard mode")
            return [False, log]
        log += [
            "\nPlayer turn "+str(turn)+" start",
            "player hp: "+str(player.hp)+" mp: "+str(player.mp)+" shield: "+str(player.shield)+" recharge: "+str(player.recharge),
            "boss: hp: "+str(boss.hp)+" poison: "+str(boss.poison),
            "Casting " + spell
        ]
        player.progress()
        boss.progress()
        if spell == "mm":
            player.mp -= 53
            boss.hp -= 4
        elif spell == "drain":
            player.mp -= 73
            player.hp += 2
            boss.hp -= 2
        elif spell == "shield":
            if player.shield:
                log.append("Shield already up")
                return [False, log]
            player.mp -= 113
            player.shield = 6
        elif spell == "poison":
            if boss.poison:
                log.append("Poison already up")
                return [False, log]
            player.mp -= 173
            boss.poison = 6
        elif spell == "recharge":
            if player.recharge:
                log.append("Recharge already up")
                return [False, log]
            player.mp -= 229
            player.recharge = 5
        else:
            return [False, log]

        if player.mp < 0:
            log.append("OOM")
            return [False, log]

        if boss.hp <= 0:
            log.append("Win!")
            return [True, log]

        # Boss turn
        log += [
            "\nBoss turn "+str(turn)+" start",
            "player hp: " + str(player.hp) + " mp: " + str(player.mp) + " shield: " + str(
                player.shield) + " recharge: " + str(player.recharge),
            "boss: hp: " + str(boss.hp) + " poison: " + str(boss.poison),
        ]
        player.progress()
        boss.progress()
        player.hp -= boss.dmg - player.armor

        if player.hp <= 0:
            log.append("Player died")
            return [False, log]

    log.append("Boss not dead")
    return [False, log]


part1 = ["poison", "recharge", "shield", "poison", "mm", "mm", "mm", "mm", "mm"]


player_spells = ["poison", "recharge", "shield", "poison", "recharge", "drain", "poison", "drain", "mm"]
ul = 1295

result = player_win(player_spells)

for line in result[1]:
    print(line)

print("mp:", mp_cost(player_spells))




