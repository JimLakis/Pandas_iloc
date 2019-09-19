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
	
	
def selection_via_boolean_mapping_one_step(df):
    ''' Combining the creating of the boolean map and its use as an index for loc[] in one statement '''
    print(df.loc[df['county'] == 'Kent'])
	
	
def selection_via_boolean_mapping_more_examples(df):
    def map_and_search_display_one_column(df):
        print(df.loc[df['first_name'] == 'Eric', 'company_name'])
        # Single column argument is a naked string
        # return type: Series
        
    def map_and_search_display_one_column2(df):
        print(df.loc[df['first_name'] == 'Eric', ['company_name']])
        # Single column argument enclosed in a list
        # return type: DataFrame
        
    def map_and_search_include_only_certain_columns(df):
        print(df.loc[df['first_name'] == 'Eric', ['company_name', 'email', 'phone1']])
        # return type: DataFrame
        
    def select_on_name_and_column_range(df):
        ''' Select rows where the first_name is 'Eric'.
            Display the columns 'city' thru to 'emain'. '''
        print(df.loc[df['first_name'] == 'Eric', 'city':'email'])
    
    def select_on_email_ending_with(df):
        ''' Select rows based on email addresses ending with "hotmain.com" '''
        # df['email'] # displays email addresses
        # df['email'].str.endswith('hotmail.com') # displays boolean indexing values, true/false values
        print(df.loc[df['email'].str.endswith('hotmail.com')]) # applying the boolean index map
        
    def select_on_name_being_in_a_list(df):
        ''' Select rows based on first_name being in a list.
            Include only thier company names. '''
        print(df.loc[df['first_name'].isin(['Eric', 'Edgar', 'Michell']), 'company_name'])
    
    def select_on_values_from_different_columns(df):
        ''' Select rows based on postal codes starting with "GL52" AND
            county equal to "Gloucestershire".
            Note: parentheses required around the second search phrase. '''
        print(df.loc[df['postal'].str.startswith('GL52') & (df['county'] == 'Gloucestershire'), 'company_name'])

    #map_and_search_display_one_column(df)
    #map_and_search_display_one_column2(df)
    #map_and_search_include_only_certain_columns(df)
    #select_on_name_and_column_range(df)
    #select_on_email_ending_with(df)
    #select_on_name_being_in_a_list(df)
    select_on_values_from_different_columns(df)


def main():
    df = load_CSV()
	df = adding_ID_col(df)
	df.set_index("id", inplace = True)
	#selection_via_boolean_mapping_two_steps(df)
    #selection_via_boolean_mapping_one_step(df)
	selection_via_boolean_mapping_more_examples(df)

if __name__ == '__main__':
    main()
