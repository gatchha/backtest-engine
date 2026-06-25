import pandas as pd
import numpy as np 
from costs import cost

def engine(positions, prix,fees_bps = 0,slippage_bps = 0):
    PL = pd.Series(positions)*(pd.Series(prix).pct_change())-cost(positions,fees_bps, slippage_bps) 
    cumulative_equity = np.cumsum(PL)
    return PL , cumulative_equity
