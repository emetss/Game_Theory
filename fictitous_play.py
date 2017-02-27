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
        #self.minusi_strategy=np.random.choice(self.minusi_payoffs)

        return
        pass

    def fictitiousPlay (self, epsilon):
        init_i_strategy=choice(self.i_strategies)
        init_minusi_strategy=choice(self.minusi_strategies)
        init_i_payoff=[x for x in init_i_strategy if -x in init_minusi_strategy][0]
        #print(init_i_payoff)
        counter_i_strategy=1
        counter_minusi_strategy=1
        counter=0
        while something>epsilon:
            counter+=1
            empirical_mixed_strategy_i=counter_i_strategy/counter
            empirical_mixed_strategy_minusi=counter_minusi_strategy/counter
            i_payoff_1=[x for x in self.i_strategies[0] if -x in init_minusi_strategy][0]*empirical_mixed_strategy_minusi
            i_payoff_2=[x for x in self.i_strategies[1] if -x in init_minusi_strategy][0]*empirical_mixed_strategy_minusi

            minusi_payoff=[x for x in minusi_strategy if -x in i_strategy][0]

            if empirical_mixed_strategy_minusi*
            i_strategy=empirical_mixed_strategy_minusi*

            if minus_i_strategy==init_minusi_strategy:
                counter_minusi_strategy+=1
            if i_strategy==init_i_strategy:
                counter_i_strategy+=1
            pass



        #print(self.minusi_payoffs)
        #print(self.minusi_temp)
        #print(i_strategy)
        #print(minusi_strategy)
        return

my_zerosumgame=ZeroSumGame(dummy_game)
my_zerosumgame.fictitiousPlay(1)
#print(my_zerosumgame.i_strategy)
print(my_zerosumgame.minusi_strategies)
print(my_zerosumgame.i_strategies)
