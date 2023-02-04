def part1(input_text):
    bits = ''.join([format(int(c, 16), '0>4b') for c in input_text.rstrip()])

    def parse_packet(packet):
        version = int(packet[:3], 2)
        type_id = int(packet[3:6], 2)
        i = 6
        
        match type_id:
            case 4:
                literal = []

                while packet[i] == '1':
                    i += 5
                    literal.append(packet[i-4:i])
                i += 5    
                literal.append(packet[i-4:i])
                
                return [version, type_id, int(''.join(literal), 2)], i

            case _:
                length_type_id = int(packet[i], 2)
                sub_packets = []
                
                if length_type_id:
                    i += 12
                    n_packets = int(packet[i-11:i], 2)
                    
                    for __ in range(n_packets):
                        sub_packet, j = parse_packet(packet[i:])
                        i += j
                        sub_packets.append(sub_packet)
                    
                else:
                    i += 16
                    end_pos = i + int(packet[i-15:i], 2)
                    
                    while i < end_pos:
                        sub_packet, j = parse_packet(packet[i:])
                        i += j
                        sub_packets.append(sub_packet)
                        
                return [version, type_id, sub_packets], i

    
    packet, i = parse_packet(bits)
    
    def version_sum(packet):
        if packet[1] == 4:
            return packet[0]
        else:
            return packet[0] + sum(version_sum(sp) for sp in packet[2])


    return version_sum(packet)


def part2(input_text):
    bits = ''.join([format(int(c, 16), '0>4b') for c in input_text.rstrip()])

    def parse_packet(packet):
        version = int(packet[:3], 2)
        type_id = int(packet[3:6], 2)
        i = 6
        
        if type_id == 4:
            literal = []

            while packet[i] == '1':
                i += 5
                literal.append(packet[i-4:i])
            i += 5    
            literal.append(packet[i-4:i])
            
            return [version, type_id, int(''.join(literal), 2)], i

        else:
            length_type_id = int(packet[i], 2)
            sub_packets = []
            
            if length_type_id:
                i += 12
                n_packets = int(packet[i-11:i], 2)
                
                for __ in range(n_packets):
                    sub_packet, j = parse_packet(packet[i:])
                    i += j
                    sub_packets.append(sub_packet)
                
            else:
                i += 16
                end_pos = i + int(packet[i-15:i], 2)
                
                while i < end_pos:
                    sub_packet, j = parse_packet(packet[i:])
                    i += j
                    sub_packets.append(sub_packet)
                    
            return [version, type_id, sub_packets], i

    
    packet, i = parse_packet(bits)
    
    def evaluate_packet(packet):
        match packet[1]:
            case 0:
                return sum(evaluate_packet(sp) for sp in packet[2])
            case 1:
                prod = 1
                for sp in packet[2]:
                    prod *= evaluate_packet(sp)
                return prod
            case 2:
                return min(evaluate_packet(sp) for sp in packet[2])
            case 3:
                return max(evaluate_packet(sp) for sp in packet[2])
            case 4:
                return packet[2]
            case 5:
                return evaluate_packet(packet[2][0]) > evaluate_packet(packet[2][1])
            case 6:
                return evaluate_packet(packet[2][0]) < evaluate_packet(packet[2][1])
            case 7:
                return evaluate_packet(packet[2][0]) == evaluate_packet(packet[2][1])


    return evaluate_packet(packet)


if __name__ == '__main__':
    with open('./input_files/AoC2021_day16_input.txt') as f:
        input_text = f.read()
    
    print('part 1:', part1(input_text))
    print('part 2:', part2(input_text))

    time_execution = 0

    if time_execution:
        import timeit
        for part in ['part1', 'part2']:
            timer = timeit.Timer(f'{part}(input_text)', globals=globals())
            n, time = timer.autorange()
            print(f'{part} took {time/n:.5f} seconds on average when run {n} times')