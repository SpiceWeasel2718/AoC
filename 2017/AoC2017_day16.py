class Solution:
    def __init__(self):
        with open("input_files/AoC2017_day16_input.txt") as f:
            self.input_text = f.read()

    def part1(self):
        moves = self.input_text.split(',')

        ind_perm = {i: i for i in range(16)}
        name_perm = {chr(97+i): chr(97+i) for i in range(16)}

        for move in moves:
            if move.startswith('s'):
                t = int(move[1:])
                ind_perm = {k: ind_perm[(k-t) % 16] for k in ind_perm}
            elif move.startswith('x'):
                t = tuple(int(n) for n in move[1:].split('/'))
                ind_perm[t[0]], ind_perm[t[1]] = ind_perm[t[1]], ind_perm[t[0]]
            else:
                t = move[1:].split('/')
                name_perm[t[0]], name_perm[t[1]] = name_perm[t[1]], name_perm[t[0]]
        
        name_perm = {name_perm[c]: c for c in name_perm}
        
        dancers = tuple(chr(97+i) for i in range(16))
        dancers = tuple(dancers[ind_perm[i]] for i in range(16))
        dancers = tuple(name_perm[c] for c in dancers)

        print(''.join(dancers))


    def part2(self):
        moves = self.input_text.split(',')

        ind_perm = {i: i for i in range(16)}
        name_perm = {chr(97+i): chr(97+i) for i in range(16)}

        for move in moves:
            if move.startswith('s'):
                t = int(move[1:])
                ind_perm = {k: ind_perm[(k-t) % 16] for k in ind_perm}
            elif move.startswith('x'):
                t = tuple(int(n) for n in move[1:].split('/'))
                ind_perm[t[0]], ind_perm[t[1]] = ind_perm[t[1]], ind_perm[t[0]]
            else:
                t = move[1:].split('/')
                name_perm[t[0]], name_perm[t[1]] = name_perm[t[1]], name_perm[t[0]]
        
        name_perm = {name_perm[c]: c for c in name_perm}
        
        dancers = tuple(chr(97+i) for i in range(16))

        ind_record = [dancers]
        step = tuple(dancers[ind_perm[i]] for i in range(16))
        
        while step != dancers:
            ind_record.append(step)
            step = tuple(step[ind_perm[i]] for i in range(16))

        name_record = [dancers]
        step = tuple(name_perm[c] for c in dancers)

        while step != dancers:
            name_record.append(step)
            step = tuple(name_perm[c] for c in step)
        
        for i in range(1000000000 % len(ind_record)):
            dancers = tuple(dancers[ind_perm[i]] for i in range(16))
        for i in range(1000000000 % len(name_record)):
            dancers = tuple(name_perm[c] for c in dancers)

        print(''.join(dancers))
        

Solution().part2()