# Python v3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df

def how_many_rows(df):
    print(df.shape[:])
    
def header(df):
    print(df.head(0))
    
    
def main():
    df = load_CSV()
    how_many_rows(df)
    header(df)
    

if __name__ == '__main__':
    main()
    
