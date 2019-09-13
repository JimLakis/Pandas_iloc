# Python 3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df
	
	
def set_index_on_column_inplace(df):
    ''' NOTE: inplace = True can not be utilized within a function as in this example '''
    # df.set_index("last_name", inplace=True)
    # See below in main() for where indexing takes place inplace...
    # Note: The column utilzed as the index now is NOT displayed in its normal position for display purposes.
    # Note: inplace = True makes the changes to current dataframe. Without this argument, another df is created in memory.
    pass


def set_index_on_column(df):
    ''' Setting the index WITHOUT inplace argument is acceptable within a function definition '''
    df = df.set_index("last_name")
    return df


def main():
    df = load_CSV()
    #df.set_index("last_name", inplace=True)
    df = set_index_on_column(df)


if __name__ == "__main__":
    main()