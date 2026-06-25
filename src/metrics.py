
import numpy as np 


def sharpe(PL) : 

    MeanPL = np.mean(PL)
    sharpe = MeanPL/np.std(PL)*np.sqrt(252)

    return sharpe 

def max_drawdown(PL):
    cumulative_equity = np.cumsum(PL)
    peak = np.maximum.accumulate(cumulative_equity)
    max_drawdown = min(cumulative_equity - peak)
    return max_drawdown 


def Turnovers(signals): 
    return  (np.count_nonzero(np.diff(signals)))/len(signals)
    
        
    
