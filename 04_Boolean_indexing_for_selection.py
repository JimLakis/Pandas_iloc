# Python v3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df
	
def adding_ID_col(df):
    ''' Creating and adding a new column to the df '''
    df['id'] = [x for x in range(df.shape[0])]
    return df


def main():
    df = load_CSV()
	df.set_index("id", inplace = True)
    

if __name__ == '__main__':
    main()
