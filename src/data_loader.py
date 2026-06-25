import yfinance as yf 
import pandas as pd



def load_data(ticker, start, end) : 
    df = yf.download(ticker,start = start, end = end)
    df = df["Close"].dropna().squeeze().sort_index()
    df = df[~df.index.duplicated()]
    return df
    

def detect_gap(df) :
    print (f"Gap détecté : {df.index[df.index.diff() > pd.Timedelta(days=5)].tolist()}")