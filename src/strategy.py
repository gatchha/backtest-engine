import numpy as np 
import pandas as pd 

def strategy_shift(X):

    positions = pd.Series(np.where(X.rolling(20).mean() > X.rolling(50).mean(), 1, 0),index = X.index)
    return positions.shift(1)

def strategy(X):
    positions = pd.Series(np.where(X.rolling(20).mean() > X.rolling(50).mean(), 1, 0),index=X.index)
    return positions


