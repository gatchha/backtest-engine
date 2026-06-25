import numpy as np 
import pandas as pd 

def cost(positions,fees_bps,slippage_bps) : 
    transaction_cost = (np.abs(pd.Series(positions).diff())*(fees_bps+slippage_bps))/10000
    return transaction_cost