#Add this at the top of your code to import the function
# from clean_data import clean_data


import pandas as pd

def clean_data(df):
  
    columns_to_encode = ["Income_type",
                        "Education_type",
                        "Family_status",
                        "Housing_type",
                        "Occupation_type"]
    # LabelEncoder
    # Documentation: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
    # Create an instance of the label encoder
    le = LabelEncoder()
    
    # Fit and transform the label encoder for each column
    for column in columns_to_encode:
        df[column] = le.fit_transform(df[column])

    # drop the unique ID column
    df = df.drop(columns=['ID'])
   
    #Scale the 'Total income' column
    


    # Return the cleaned DataFrame
    return df
