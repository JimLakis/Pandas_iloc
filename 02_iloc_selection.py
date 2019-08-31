# Python 3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df


def select_rows(df):
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
        
    def select_multiple_rows(df):
        ''' Selecting multiple rows.
            Output's data type is a DataFrame. '''
        print(f"Selecting the first ten rows: {df.iloc[0:11]}")
        
    #single_row_return_series(df)
    #single_row_return_dataframe(df)
    select_multiple_rows(df)
    

def select_columns(df):
    ''' iloc[] format notes:
            first index value/s is a place holder for rows,
            second index value/s is for the columns,
            seperated by a comma.
            example: df.iloc[rows , columns] '''
    def single_column(df):
        ''' Selecting a column. 
            Output's data type is a Series.'''
        #print(f"df.iloc[:,0] - first column:\n{df.iloc[:,0]}")
        #print(f"df.iloc[:,1] - second column:\n{df.iloc[:,1]}")
        print(f"df.iloc[:,-1] - last column:\n{df.iloc[:,-1]}")
    
    def multiple_columns(df):
        ''' Selecting multiple columns. 
            Output's data type is a DataFrame.'''
        print(f"df.iloc[:,0:2] - first three columns:\n{df.iloc[:,0:3]}")
    
    #single_column(df)
    multiple_columns(df)


def select_combinations(df):
    ''' Select the intersection of rows and columns.
        iloc[] format notes:
            Again, the first index value/s is for rows, the second index value/s is for columns, separated by a comma.
            With multiple rows and columns selected however, those two indexes need to be enclosed in lists.
            example: df.iloc[[rows] , [columns]] '''
    def specific_multiple_rows_columns(df):
        print(f"df.iloc[[0,2],[0,4]]\nFirst and fifth columns of the first and third rows.\n{df.iloc[[0,2],[0,4]]}")
    
    def range_rows_columns(df):
        print(f"df.iloc[0:2,0:3]\nFirst three columns of the first two rows.\n{df.iloc[0:2,0:3]}")

    #specific_multiple_rows_columns(df)
    range_rows_columns(df)
    

def main():
    df = load_CSV()
    #select_rows(df)
    #select_columns(df)
	select_combinations(df)


if __name__ == "__main__":
    main()