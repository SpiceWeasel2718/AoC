"""
Input:

The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant.

Part 1:
move Pmg and Pmc to floor 2 (end step 1)
1:
2:Coc, Cmc, Ruc, Puc
3:E, Pmg, Pmc, Cog, Cmg, Rug, Pug
4:

use Pmc to move Puc to floor 4 and Coc to floor 2 (step 5)
1:Puc
2:Cmc, Ruc
3:E, Pmg, Pmc, Cog, Coc, Cmg, Rug, Pug
4:

move Cmg, Rug to floor 3, move Cmc, Ruc to floor 4, move Cmc back to floor 3, move Rug back to floor 2 (step 9)
1:Ruc, Puc
2:Cmg, Cmc
3:E, Pmg, Pmc, Cog, Coc, Rug, Pug
4:

move Rug, Pug to floor 4, move Rug, Ruc to floor 3, move Cmg, Rug to floor 4, use Puc to move Ruc to floor 4 (step 15)
1:E, Cmg, Rug, Ruc, Pug, Puc
2:Cmc
3:Pmg, Pmc, Cog, Coc
4:

move Cmg to floor 2, move Pmc, Coc to floor 2, move Pmc back to floor 2, move Cog, Cmg to floor 4 (step 21)
1:E, Cog, Cmg, Rug, Ruc, Pug, Puc
2:Coc, Cmc
3:Pmg, Pmc
4:

use Puc to move Cmc to floor 4, use Cog to move Pmc to floor 4, use Puc to move Pmc, Coc to floor 4 (step 33)


Part 2:
move the extra components from floor 1 to floor 2 and just extend the strategy used in part 1 (57 steps)
"""









