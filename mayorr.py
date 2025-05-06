from random import choice, seed 
from pandas import read_csv as rc

df = rc('Nomen.csv')
names = df.names.tolist()
def select(n):
    seed(n)
    winner = choice(names)
    return(winner)
