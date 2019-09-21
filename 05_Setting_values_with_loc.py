# Python v3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df
    
    
def main():
    df = load_CSV()
    df.set_index("last_name", inplace=True)


if __name__ == '__main__':
    main()