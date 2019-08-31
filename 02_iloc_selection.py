# Python 3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df

	
def select_row(df):
    def single_row_return_series(df):
        ''' Selecting a single row.
            Output's data type is a Series. '''
        print(f"Selecting the first row: {df.iloc[0]}")
        #print(f"Selecting the second row: {df.iloc[1]}")
        #print(f"Selecting the last row: {df.iloc[-1]}")
        print(type(df.loc[0])) # returns: <class 'pandas.core.series.Series'>
        
    def single_row_return_dataframe(df):
        ''' Selecting a single row.
            Forcing the return of a single row's data type to be a DataFrame by enclosing the index in a list. '''
        print(f"Selecting the second row: {df.iloc[[1]]}")
        print(type(df.loc[[1]])) # returns: <class 'pandas.core.frame.DataFrame'>
        
    #single_row_return_series(df)
    single_row_return_dataframe(df)
        

def select_multiple_rows(df):
	''' Selecting multiple rows.
		Output's data type is a DataFrame. '''
	print(f"Selecting the first ten rows: {df.iloc[0:11]}")

		
def main():
    df = load_CSV()
    #select_rows(df)
    multiple_rows(df)


if __name__ == "__main__":
    main()