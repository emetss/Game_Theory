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
twocounter=0
hundredcounter=0
for i in range (1000):
    instance_of_generator = Generator()
    some_game = instance_of_generator.no_constraints()
    my_zerosumgame2=fp.ZeroSumGame(some_game)
    my_zerosumgame2.fictitiousPlay(0.0001, 0.0001)
    # if my_zerosumgame2.counter==2:
    #     twocounter+=1
    # if my_zerosumgame2.counter==101:
    #     hundredcounter+=1
    #if 1 not in my_zerosumgame2.nash_equilibrium:
    #if float("Inf") in my_zerosumgame2.rate_of_convergence:
    if filter(lambda x: x>=0.99, my_zerosumgame2.nash_equilibrium)!=[]:
        data_no_constraints.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.counter, my_zerosumgame2.rate_of_convergence])

    #print(some_game)
    #print(my_zerosumgame2.nash_equilibrium)
    #print(my_zerosumgame2.counter)
    #print(my_zerosumgame2.rate_of_convergence)

#print(twocounter/hundredcounter)
x=[]
y=[]
n_it=[]
for i in data_no_constraints:
    x.append(i[2])
    y.append(i[3])
    n_it.append(i[4])
    #print(i)
#print("")

plt.plot(n_it, 'ro')
plt.show()
plt.scatter(x, y)
plt.title("No Constraints")
plt.show()

data_no_strictly_dominant_strategies=[]
for i in range (1000):
    instance_of_generator = Generator()
    some_game = instance_of_generator.no_strictly_dominant_strategies()
    my_zerosumgame2=fp.ZeroSumGame(some_game)
    my_zerosumgame2.fictitiousPlay(0.0001, 0.0001)
    data_no_strictly_dominant_strategies.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.rate_of_convergence])

    #print(some_game)
    #print(my_zerosumgame2.nash_equilibrium)
    #print(my_zerosumgame2.counter)
    #print(my_zerosumgame2.rate_of_convergence)

#print(data_no_strictly_dominant_strategies)

x_prime=[]
y_prime=[]
n_it=[]
for i in data_no_strictly_dominant_strategies:
    x_prime.append(i[2])
    y_prime.append(i[3])
    n_it.append(i[4])
    #print(i)

plt.plot(n_it, 'ro')
plt.show()

plt.scatter(x_prime, y_prime)
plt.title("No Strictly Dominant Strategies")
plt.show()
#print("")

data_no_NE_in_dominant_strategies=[]
for i in range (1):
    instance_of_generator = Generator()
    some_game = instance_of_generator.no_NE_in_dominant_strategies()
    my_zerosumgame2=fp.ZeroSumGame(some_game)
    my_zerosumgame2.fictitiousPlay(0.0001, 0.0001)
    data_no_NE_in_dominant_strategies.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.rate_of_convergence])

    #print(some_game)
    #print(my_zerosumgame2.nash_equilibrium)
    #print(my_zerosumgame2.counter)
    #print(my_zerosumgame2.rate_of_convergence)


x_pprime=[]
y_pprime=[]
for i in data_no_NE_in_dominant_strategies:
    x_pprime.append(i[2])
    y_pprime.append(i[3])
    #print(i)

plt.scatter(x_pprime, y_pprime)
plt.title("No NE in Strictly Dominant Strategies")
plt.show()


data_NE_in_dominant_strategies=[]
for i in range (1000):
    instance_of_generator = Generator()
    some_game = instance_of_generator.NE_in_dominant_strategies()
    my_zerosumgame2=fp.ZeroSumGame(some_game)
    my_zerosumgame2.fictitiousPlay(0.0001, 0.0001)
    data_NE_in_dominant_strategies.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.rate_of_convergence])

    #print(some_game)
    #print(my_zerosumgame2.nash_equilibrium)
    #print(my_zerosumgame2.counter)
    #print(my_zerosumgame2.rate_of_convergence)

x_ppprime=[]
y_ppprime=[]
for i in data_NE_in_dominant_strategies:
    x_ppprime.append(i[2])
    y_ppprime.append(i[3])
    #print(i)
#print("")

plt.scatter(x_ppprime, y_ppprime)
plt.title("NE in Dominant Strategies")
plt.show()

data_exactly_one_dominant_strategy=[]
for i in range (1):
    instance_of_generator = Generator()
    some_game = instance_of_generator.exactly_one_dominant_strategy()
    my_zerosumgame2=fp.ZeroSumGame(some_game)
    my_zerosumgame2.fictitiousPlay(0.0001, 0.0001)
    data_exactly_one_dominant_strategy.append([list(some_game),my_zerosumgame2.nash_equilibrium,my_zerosumgame2.counter_row,my_zerosumgame2.counter_col,my_zerosumgame2.rate_of_convergence])

    #print(some_game)
    #print(my_zerosumgame2.nash_equilibrium)
    #print(my_zerosumgame2.counter)
    #print(my_zerosumgame2.rate_of_convergence)

x_pppprime=[]
y_pppprime=[]
for i in data_exactly_one_dominant_strategy:
    x_pppprime.append(i[2])
    y_pppprime.append(i[3])
    #print(i)
#print("")

plt.scatter(x_ppprime, y_ppprime)
plt.title("Exactly one Dominant Strategy")
plt.show()
