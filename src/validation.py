

def validation(X, split): 
    df_train = X.iloc[:int(len(X)*split)]
    df_test = X.iloc[int(len(X)*split):]
    return df_train,df_test
