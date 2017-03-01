import numpy as np

import random

import fictitous_play as fp

import matplotlib.pyplot as plt



class Generator(object):

    '''Generates two-player, zero-sum games. Games are formally represented as 1x4 array. Vector entries represent row player's

     payoffs (order: top-left,top-right,bottom-left,bottom-right). Column player's payoffs is negative vector.'''



    def __init__(self, type = random):

        '''Initialize Generator class

        :param type (random, dom1, dom2, weakdom1, weakdom2)

        '''

        self.type_of_game = type



    def no_constraints(self):

        '''Generates random game with payoffs in the interval (-1000,1000) and no further constraints.'''

        tl = random.randint(-1000,1000) #Row player's top left entry

        tr = random.randint(-1000,1000)

        bl = random.randint(-1000,1000)

        br = random.randint(-1000,1000)



        game = np.array([tl,tr,bl,br], float)   #Create game-vector



        return game



    def no_strictly_dominant_strategies(self):

        '''Generates random game under the constraint that there are no strictly dominant strategies for either player.'''

        tl = 1 #Initializing with game that violates constraint

        tr = 1

        bl = 0

        br = 0

        while (tl > bl and tr > br) or (tl < bl and tr < br) or (tr > tl and br > bl) or (tr < tl and br < bl): #Condition that there is strictly dominant strategy

            tl = random.randint(-1000,1000)

            tr = random.randint(-1000,1000)

            bl = random.randint(-1000,1000)

            br = random.randint(-1000,1000)

        game = np.array([tl,tr,bl,br], float)   #Create game-vector

        return game



    def no_NE_in_dominant_strategies(self):

        '''Generates random game under the constraint that there are no NE in strictly dominant strategies.'''

        tl = 2 #Initializing with game that violates constraint

        tr = -2

        bl = 3

        br = -1

        while (tl > bl and tr > br and -tl > -tr and -bl > -br) or (tl < bl and tr < br and -tl < -tr and -bl < -br) or (tl > bl and tr > br and -tl < -tr and -bl < -br) and (tl < bl and tr < br and -tl > -tr and -bl > -br): #Condition for existence of NE

            tl = random.randint(-1000,1000) #Row player's top left entry

            tr = random.randint(-1000,1000)

            bl = random.randint(-1000,1000)

            br = random.randint(-1000,1000)

        game = np.array([tl,tr,bl,br], float)   #Create game-vector

        return game


    def NE_in_dominant_strategies(self):

        '''Generates game with NE in strictly dominant strategies.'''

        tl = 0 #Initializing with game that violates constraint

        tr = 0

        bl = 0

        br = 0

        while not((tl > tr and bl > br) and (tl > bl and tr > br)) and not((tl > tr and bl > br) and (tl < bl and tr < br)) and not((tl < tr and bl < br) and (tl > bl and tr > br)) and not((tl < tr and bl < br) and (tl < bl and tr < br)):

            tl = random.randint(-1000,1000) #Row player's top left entry

            tr = random.randint(-1000,1000)

            bl = random.randint(-1000,1000)

            br = random.randint(-1000,1000)

        game = np.array([tl, tr, bl, br], float)  # Create game-vector

        return game


    def exactly_one_dominant_strategy(self):

        '''Generates game with exactly one dominant strategy.'''

        tl = 0  # Initializing with game that violates constraint

        tr = 0

        bl = 0

        br = 0

        while not((tl > tr and bl > br) or (tl > bl and tr > br) or (tl < bl and tr < br) or (tl < tr and bl < br)):

            tl = random.randint(-1000, 1000)  # Row player's top left entry

            tr = random.randint(-1000, 1000)

            bl = random.randint(-1000, 1000)

            br = random.randint(-1000, 1000)

        game = np.array([tl, tr, bl, br], float)  # Create game-vector

        return game


data_no_constraints=[]
data_pure_nash_candidates=[]
data_without_pure_nash=[]
data_inf_rate_of_convergence=[]
twocounter=0
hundredcounter=0
for i in range (1000):
    instance_of_generator = Generator()
    some_game = instance_of_generator.no_constraints()
    my_zerosumgame2=fp.ZeroSumGame(some_game)
    my_zerosumgame2.fictitiousPlay(0.0001, 0.0001)
    data_no_constraints.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.counter, my_zerosumgame2.rate_of_convergence])
    if float("Inf") in my_zerosumgame2.rate_of_convergence:
        data_inf_rate_of_convergence.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.counter, my_zerosumgame2.rate_of_convergence])
    if list(filter(lambda x: x>=0.99, my_zerosumgame2.nash_equilibrium))!=[]:
        data_pure_nash_candidates.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.counter, my_zerosumgame2.rate_of_convergence])
    else:
        data_without_pure_nash.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.counter, my_zerosumgame2.rate_of_convergence])

n_it=[]
for i in data_no_constraints:
    n_it.append(i[4])


plt.plot(n_it, 'ro')
plt.xlabel("n")
plt.ylabel("# of Iterations")
plt.title("All Games")
plt.show()

n_it=[]
for i in data_inf_rate_of_convergence:
    n_it.append(i[4])

plt.plot(n_it, 'ro')
plt.xlabel("n")
plt.ylabel="# of Iterations"
plt.title("Games with Infinite Convergence Rate")
plt.show()

n_it=[]
for i in data_pure_nash_candidates:
    n_it.append(i[4])

plt.plot(n_it, 'ro')
plt.xlabel="n"
plt.ylabel="# of Iterations"
plt.title("Pure Nash Equilibrium Candidates")
plt.show()

n_it=[]
for i in data_without_pure_nash:
    n_it.append(i[4])

plt.plot(n_it, 'ro')
plt.xlabel="n"
plt.ylabel="# of Iterations"
plt.title("Games without Pure Nash Candidates")
plt.show()

data_no_strictly_dominant_strategies=[]
for i in range (1000):
    instance_of_generator = Generator()
    some_game = instance_of_generator.no_strictly_dominant_strategies()
    my_zerosumgame2=fp.ZeroSumGame(some_game)
    my_zerosumgame2.fictitiousPlay(0.0001, 0.0001)
    data_no_strictly_dominant_strategies.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.rate_of_convergence])

n_it=[]
for i in data_no_strictly_dominant_strategies:
    n_it.append(i[4])

plt.title("No Strictly Dominant Strategies")
plt.plot(n_it, 'ro')
plt.show()

