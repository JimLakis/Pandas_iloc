# Python 3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df
    
    
def set_index_on_column_inplace(df):
    ''' NOTE: inplace = True can not be utilized within a function as in this example '''
    df.set_index("email", inplace=True)


def set_index_on_column(df):
    ''' Setting the index WITHOUT inplace argument is acceptable within a function definition '''
    df2 = df.set_index("last_name")
    return df2


def main():
    df = load_CSV()
    #df.set_index("last_name", inplace=True)
    set_index_on_column_inplace(df)
    df2 = set_index_on_column(df)
    
    print(df.head(1))
    print(df2.head(1))


if __name__ == "__main__":
    main()