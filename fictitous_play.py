import numpy as np
from random import choice

dummy_game=np.array([1,-1,2,-2])


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
        difference_1=5
        difference_2=5


        while difference_1>epsilon_1 or difference_2>epsilon_2:
            counter+=1
            empirical_mixed_strategy_i=counter_i_strategy/counter
            empirical_mixed_strategy_minusi=counter_minusi_strategy/counter
            i_payoff_1=self.i_strategies[0][0]*empirical_mixed_strategy_minusi+self.i_strategies[0][1]*(1-empirical_mixed_strategy_minusi)
            i_payoff_2=self.i_strategies[1][0]*empirical_mixed_strategy_minusi+self.i_strategies[1][1]*(1-empirical_mixed_strategy_minusi)
            #print(i_payoff_1, i_payoff_2)
            if i_payoff_1>=i_payoff_2:
                i_best_response=self.i_strategies[0]
            else:
                i_best_response=self.i_strategies[1]

            minusi_payoff_1=self.minusi_strategies[0][0]*empirical_mixed_strategy_i+self.minusi_strategies[0][1]*(1-empirical_mixed_strategy_i)
            minusi_payoff_2=self.minusi_strategies[1][0]*empirical_mixed_strategy_i+self.minusi_strategies[1][1]*(1-empirical_mixed_strategy_i)

            if minusi_payoff_1>=minusi_payoff_2:
                minusi_best_response=self.minusi_strategies[0]
            else:
                minusi_best_response=self.minusi_strategies[1]

            i_strategy=i_best_response
            #print(i_strategy)
            minus_i_strategy=minusi_best_response

            if np.array_equal(i_strategy, init_i_strategy):
                counter_i_strategy+=1

            if np.array_equal(minus_i_strategy, init_minusi_strategy):
                counter_minusi_strategy+=1

            difference_1=abs(temp_empirical_mixed_strategy_i-empirical_mixed_strategy_i)
            difference_2=abs(temp_empirical_mixed_strategy_minusi-empirical_mixed_strategy_minusi)
            #print(difference_1)
            #print(difference_2)

            temp_empirical_mixed_strategy_i=empirical_mixed_strategy_i
            temp_empirical_mixed_strategy_minusi=empirical_mixed_strategy_minusi
            #print([temp_empirical_mixed_strategy_i,temp_empirical_mixed_strategy_minusi])

            pass

        self.nash_equilibrium=[empirical_mixed_strategy_i, 1-empirical_mixed_strategy_i, empirical_mixed_strategy_minusi, 1-empirical_mixed_strategy_minusi]

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

