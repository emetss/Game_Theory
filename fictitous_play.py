import numpy as np
from random import choice

dummy_game=np.array([1,-1,-1,1])


class ZeroSumGame(object):
    '''A zero-sum-game specified by an array'''

    def __init__(self, i_payoffs):
        '''Constructor

        :param i_strategy: player i's strategies given as an array.
        '''

        self.i_payoffs=i_payoffs
        self.minusi_payoffs=i_payoffs*(-1)
        #splitting payoff arrays into strategies
        self.i_strategies=np.array(np.array_split(self.i_payoffs, 2))
        #building the strategies of player -i by changing presigns and swapping middle values for correct order.
        self.minusi_temp=np.copy(self.minusi_payoffs)
        self.minusi_temp[1],self.minusi_temp[2]=self.minusi_temp[2],self.minusi_temp[1]
        self.minusi_strategies=np.array(np.array_split(self.minusi_temp, 2))

        return

    def fictitiousPlay (self, epsilon_1, epsilon_2):
        '''A simulation of fictitious play that takes as parameters to epsilon values serving as convergence conditions.

        :param epsilon 1: player 1's convergence criterion.
        :param epsilon 2: player 2's convergence criterion.
        '''
        #The algorithm starts always at the strategy profile HH. Since the input will be randomly generated games, it does not matter.
        init_i_strategy=self.i_strategies[0]
        #init_i_strategy=choice(self.i_strategies)
        #print(init_i_strategy)
        #init_minusi_strategy=choice(self.minusi_strategies)
        init_minusi_strategy=self.minusi_strategies[0]
        #initializing some variables preparing the while-loop
        counter_i_strategy=1
        counter_minusi_strategy=1
        counter=0
        temp_empirical_mixed_strategy_i=1000
        temp_empirical_mixed_strategy_minusi=1000
        difference_1=1000
        difference_2=1000
        difference_1_old=1000
        difference_2_old=1000


        while difference_1>epsilon_1 or difference_2>epsilon_2:
            # increasing l
            counter+=1
            #calculating the empirical mixed strategies
            empirical_mixed_strategy_i=counter_i_strategy/counter
            empirical_mixed_strategy_minusi=counter_minusi_strategy/counter
            #calculating the expected utility for player 1:
            i_payoff_1=self.i_strategies[0][0]*empirical_mixed_strategy_minusi+self.i_strategies[0][1]*(1-empirical_mixed_strategy_minusi)
            i_payoff_2=self.i_strategies[1][0]*empirical_mixed_strategy_minusi+self.i_strategies[1][1]*(1-empirical_mixed_strategy_minusi)
            #print(i_payoff_1, i_payoff_2)
            #Choosing the best response. Heads if tie.
            if i_payoff_1>=i_payoff_2:
                i_best_response=self.i_strategies[0]
            else:
                i_best_response=self.i_strategies[1]
            #same procedure for player 2
            minusi_payoff_1=self.minusi_strategies[0][0]*empirical_mixed_strategy_i+self.minusi_strategies[0][1]*(1-empirical_mixed_strategy_i)
            minusi_payoff_2=self.minusi_strategies[1][0]*empirical_mixed_strategy_i+self.minusi_strategies[1][1]*(1-empirical_mixed_strategy_i)

            if minusi_payoff_1>=minusi_payoff_2:
                minusi_best_response=self.minusi_strategies[0]
            else:
                minusi_best_response=self.minusi_strategies[1]

            #i_strategy=i_best_response
            #print(i_strategy)
            #minus_i_strategy=minusi_best_response
            #If Heads is chosen, the number k of times this strategy was played is increased by 1
            if np.array_equal(i_best_response, init_i_strategy):
                counter_i_strategy+=1

            if np.array_equal(minusi_best_response, init_minusi_strategy):
                counter_minusi_strategy+=1

            #checking if the convergence condition is fulfilled
            difference_1_ancient=difference_1_old
            difference_2_ancient=difference_2_old
            difference_1_old=difference_1
            difference_2_old=difference_2
            difference_1=abs(temp_empirical_mixed_strategy_i-empirical_mixed_strategy_i)
            difference_2=abs(temp_empirical_mixed_strategy_minusi-empirical_mixed_strategy_minusi)
            #updating the temporary variables
            temp_empirical_mixed_strategy_i=empirical_mixed_strategy_i
            temp_empirical_mixed_strategy_minusi=empirical_mixed_strategy_minusi
            #print([temp_empirical_mixed_strategy_i,temp_empirical_mixed_strategy_minusi])

            pass

        self.nash_equilibrium=[empirical_mixed_strategy_i, 1-empirical_mixed_strategy_i, empirical_mixed_strategy_minusi, 1-empirical_mixed_strategy_minusi]
        self.counter=counter
        self.rate_of_convergence=[np.log(abs(difference_1)/abs(difference_1_old))/np.log(abs(difference_1_old)/abs(difference_1_ancient)),np.log(abs(difference_2)/abs(difference_2_old))/np.log(abs(difference_2_old)/abs(difference_2_ancient))]

        #print(self.minusi_payoffs)
        #print(self.minusi_temp)
        #print(i_strategy)
        #print(minusi_strategy)
        return

my_zerosumgame=ZeroSumGame(dummy_game)
my_zerosumgame.fictitiousPlay(0.000001, 0.000001)
#print(my_zerosumgame.i_strategy)
#print(my_zerosumgame.minusi_strategies)
#print(my_zerosumgame.i_strategies)
print(my_zerosumgame.nash_equilibrium)
print(my_zerosumgame.counter)
print(my_zerosumgame.rate_of_convergence)

