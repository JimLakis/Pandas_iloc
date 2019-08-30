# Python 3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df
	
def select_rows(df):
    def single_row_return_series(df):
        ''' Selecting a single row. Output is a Series. '''
		print(f"Selecting the first row: {df.iloc[0]}")
		#print(f"Selecting the second row: {df.iloc[1]}")
		#print(f"Selecting the last row: {df.iloc[-1]}")
		
	single_row_return_series(df)
		

def main():
	df = load_CSV()
	select_rows(df)


if __name__ == "__main__":
	main()