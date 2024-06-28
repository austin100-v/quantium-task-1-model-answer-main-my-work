import pandas as pd
import glob

# define the path to the data folder 
data_path= "data/*.csv"

# read all csv files into a list of DataFrames
all_files = glob.glob(data_path)
data_frames = []

for files in all_files:
    df = pd.read_csv(file) # type: ignore
    data_frames.append(df)

# Concatenate all DataFrames into one 
combined_df = pd.concat(data_frames, ignore_index= True) 

# filter rows where the product is 'pink morsels'
pink_morsels_df = combined_df[combined_df['product'] == 'Pink Morsels']

# calculate sales by multiplying quantity and price
pink_morsels_df['sales'] = pink_morsels_df['quantity'] * pink_morsels_df['price']

# select the required columns 
final_df = pink_morsels_df [['sales', 'date', 'region']]

# save the final data frame to a new csv file
final_df.to_csv('formatted_sales_data.csv', index=False)

print("formatted csv file has been created successfully")
