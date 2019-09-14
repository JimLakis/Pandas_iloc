# Python v3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df
	
def adding_ID_col(df):
    ''' Creating and adding a new column to the df '''
    df['id'] = [x for x in range(df.shape[0])]
    return df
	
	
def selection_via_boolean_mapping_two_steps(df):
    ''' Boolean mapping in two steps.
        First create the boolean map Series.
        Second utilize the mapping values to make selections. '''
    def boolean_mapping(df):
        ''' Producing a Series of mapping values, ie. True/False '''
        s = df['county'] == 'Kent'
        return s
    
    def loc_selection_based_on_mapping(s):
        ''' Applying mapping values in loc[] selection.
            Return value is a DataFrame.  '''
        print(df.loc[s])
    
    s = boolean_mapping(df)
    loc_selection_based_on_mapping(s)


def main():
    df = load_CSV()
	df = adding_ID_col(df)
	df.set_index("id", inplace = True)
	selection_via_boolean_mapping_two_steps(df)
    

if __name__ == '__main__':
    main()
