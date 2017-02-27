import numpy as np

dummy_game=np.array([4,3,2,1])


class ZeroSumGame(object):
    '''A zero-sum-game specified by an array'''

    def __init__(self, row_payoffs):
        '''Constructor

        :param i_strategy: rowena's strategies given as an array.
        '''

        self.row_payoffs=row_payoffs
        self.col_payoffs=row_payoffs*(-1)
        #splitting payoff arrays into strategies
        self.row_strategies=np.array(np.array_split(self.row_payoffs, 2))
        #building Collin's strategies by changing presigns and swapping middle values for correct order.
        self.col_temp=np.copy(self.col_payoffs)
        self.col_temp[1],self.col_temp[2]=self.col_temp[2],self.col_temp[1]
        self.col_strategies=np.array(np.array_split(self.col_temp, 2))

        return

    def fictitiousPlay (self, epsilon_1, epsilon_2):
        '''A simulation of fictitious play that takes as parameters to epsilon values serving as convergence conditions.

        :param epsilon 1: player 1's convergence criterion.
        :param epsilon 2: player 2's convergence criterion.
        '''
        #The algorithm starts always at the strategy profile HH. Since the input will be randomly generated games, it does not matter.
        init_row_strategy=self.row_strategies[0]
        init_col_strategy=self.col_strategies[0]
        #initializing some variables preparing the while-loop
        counter_row=0
        counter_col=0
        counter_row_strategy=1
        counter_col_strategy=1
        counter=0
        temp_empirical_mixed_strategy_row=1000
        temp_empirical_mixed_strategy_col=1000
        difference_1=1000
        difference_2=1000
        difference_1_old=1000
        difference_2_old=1000


        while difference_1>epsilon_1 or difference_2>epsilon_2:
            # increasing l
            counter+=1
            if difference_1>epsilon_1:
                counter_row+=1
            if difference_2>epsilon_2:
                counter_col+=1

            #calculating the empirical mixed strategies
            empirical_mixed_strategy_row=counter_row_strategy/counter
            empirical_mixed_strategy_col=counter_col_strategy/counter
            #calculating the expected utility for player 1:
            row_payoff_1=self.row_strategies[0][0]*empirical_mixed_strategy_col+self.row_strategies[0][1]*(1-empirical_mixed_strategy_col)
            row_payoff_2=self.row_strategies[1][0]*empirical_mixed_strategy_col+self.row_strategies[1][1]*(1-empirical_mixed_strategy_col)
            #Choosing the best response. Heads if tie.
            if row_payoff_1>=row_payoff_2:
                row_best_response=self.row_strategies[0]
            else:
                row_best_response=self.row_strategies[1]
            #same procedure for player 2
            col_payoff_1=self.col_strategies[0][0]*empirical_mixed_strategy_row+self.col_strategies[0][1]*(1-empirical_mixed_strategy_row)
            col_payoff_2=self.col_strategies[1][0]*empirical_mixed_strategy_row+self.col_strategies[1][1]*(1-empirical_mixed_strategy_row)

            if col_payoff_1>=col_payoff_2:
                col_best_response=self.col_strategies[0]
            else:
                col_best_response=self.col_strategies[1]

            #If Heads is chosen, the number k of times this strategy was played is increased by 1
            if np.array_equal(row_best_response, init_row_strategy):
                counter_row_strategy+=1

            if np.array_equal(col_best_response, init_col_strategy):
                counter_col_strategy+=1

            #checking if the convergence condition is fulfilled
            difference_1_ancient=difference_1_old
            difference_2_ancient=difference_2_old
            difference_1_old=difference_1
            difference_2_old=difference_2
            difference_1=abs(temp_empirical_mixed_strategy_row-empirical_mixed_strategy_row)
            difference_2=abs(temp_empirical_mixed_strategy_col-empirical_mixed_strategy_col)
            #updating the temporary variables
            temp_empirical_mixed_strategy_row=empirical_mixed_strategy_row
            temp_empirical_mixed_strategy_col=empirical_mixed_strategy_col


            pass

        self.nash_equilibrium=[empirical_mixed_strategy_row, 1-empirical_mixed_strategy_row, empirical_mixed_strategy_col, 1-empirical_mixed_strategy_col]
        self.counter=counter
        try:
            rate_of_convergence_row=np.log(abs(difference_1)/abs(difference_1_old))/np.log(abs(difference_1_old)/abs(difference_1_ancient))
        except ZeroDivisionError:
            rate_of_convergence_row="instant"
        try:
            rate_of_convergence_col=np.log(abs(difference_2)/abs(difference_2_old))/np.log(abs(difference_2_old)/abs(difference_2_ancient))
        except ZeroDivisionError:
            rate_of_convergence_col="instant"
        self.rate_of_convergence=[rate_of_convergence_row,rate_of_convergence_col]

        print(difference_1_old)
        print(difference_1_ancient)
        print(difference_2_old)
        print(difference_1_ancient)
        print(counter_row)
        print(counter_col)
        return

my_zerosumgame=ZeroSumGame(dummy_game)
my_zerosumgame.fictitiousPlay(0.0001, 0.0001)
print(my_zerosumgame.nash_equilibrium)
print(my_zerosumgame.counter)
print(my_zerosumgame.rate_of_convergence)

