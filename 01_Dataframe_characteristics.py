# Python v3.6


import pandas as pd


def load_CSV():
	''' Reading in the CSV file, creating a DataFrame.
	The CSV file was obtained from https://www.briandunning.com/sample-data/ '''
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df

	
def dimensions(df):
	''' Determining the dimensions of df, rows by columns'''
    print(df.shape[:])
    
	
def header(df):
	''' Listing the column headers of the df '''
    print(df.head(0))

	
def types_returned_from_rows(df):
    ''' Returning data types for a single row verses multiple rows. '''
    def single_row(df):
        ''' Returning a single row's data type yields a Series '''
        print(f"Type of a single row returned: {type(df.iloc[0])}")
    
    def multiple_rows(df):
        ''' Returning multiple row's data type yields a DataFrame '''
        print(f"Type of multiple rows returned: {type(df.iloc[0:4])}")
        
    single_row(df)
    multiple_rows(df)
    
    
def main():
    df = load_CSV()
    dimensions(df)
    header(df)
	types_returned_from_rows(df)
    

if __name__ == '__main__':
    main()
    
