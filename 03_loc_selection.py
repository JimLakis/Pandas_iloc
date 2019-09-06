# Python v3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df

    
def select_on_row_values(df):
    def select_on_single_row_values_output_series(df):
        ''' Passing one index value as a single string returns ouput type as a Series '''
        print(f"df.loc['Zigomalas']: \n{df.loc['Zigomalas']}")
        #print(type(df.loc['Zigomalas']))
    
    def select_on_single_row_values_output_dataframe(df):
        ''' Passing one index value as a single string returns ouput type as a Series '''
        print(f"df.loc[['Zigomalas']]: \n{df.loc[['Zigomalas']]}")
        #print(type(df.loc[['Zigomalas']]))
        
    def select_on_multiple_row_values(df):
        ''' Passing two or more indexes, argument must be enclosed in a list.
            Returned data type is a DataFrame. '''
        print(f"df.loc[['Zigomalas','Veness']] \n: {df.loc[['Zigomalas','Veness']]}")

    #select_on_single_row_values_output_series(df)
    #select_on_single_row_values_output_dataframe(df)
    select_on_multiple_row_values(df)
    
    
def main():
    df = load_CSV()
    df.set_index("last_name", inplace=True)
    select_on_row_values(df)


if __name__ == '__main__':
    main()