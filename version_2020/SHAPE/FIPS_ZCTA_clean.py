# allocativ
# Healthy Neighborhoods
# State County Zip Key Join Code

## Step 1: Import Libraries and Data

### Import Python libraries
import os # Operating system navigation

### Import data science libraries
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'

### Set working directory
os.chdir("C:/Users/drewc/GitHub/allocativ") # Set wd to project repository

## Step 2: Clean D4D Crosswalk

### Import datasets from csv files
df_D4D = pd.read_csv("hnb/FIPS/D4D/ZIP-COUNTY-FIPS_2017-06.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Convert numeric to character
df_D4D['STCOUNTYFP'] = df_D4D['STCOUNTYFP'].astype("str") # Change data type of column in data frame

### Add leading zeros
df_D4D['STCOUNTYFP'] = df_D4D['STCOUNTYFP'].str.rjust(5, "0") # add leading zeros of character column using rjust() function

### Add labels to codes
df_D4D["FIPS"] = "FIPS"+ df_D4D['STCOUNTYFP'] # Combine string with column

### Modify Names
df_D4D["Name"] = df_D4D["COUNTYNAME"] # Add single column
df_D4D["ST"] = df_D4D["STATE"] # Add single column

### Remove Territories
df_D4D = df_D4D[df_D4D.ST != "PR"] # Drop rows by condition
df_D4D = df_D4D[df_D4D.ST != "GU"] # Drop rows by condition
df_D4D = df_D4D[df_D4D.ST != "VI"] # Drop rows by condition
df_D4D = df_D4D[df_D4D.ST != "VI"] # Drop rows by condition

### Remove unwanted columns
df_D4D = df_D4D.filter(["FIPS", "ST", "Name", "STCOUNTYFP"]) # Keep only selected columns
df_D4D = df_D4D.drop_duplicates(keep = "first", inplace = False) # Drop all dupliacted values

### Verify
df_D4D.info() # Get class, memory, and column info: names, data types, obs.
df_D4D.head() # Print first 5 observations

## Step 3: Clean HUD to connect ZCTA and FIPS

### Import datasets from csv files
df_HUD = pd.read_csv("hnb/FIPS/HUD/ZIP_COUNTY_032020.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Convert numeric to character
df_HUD['ZIP'] = df_HUD['ZIP'].astype("str") # Change data type of column in data frame
df_HUD['STCOUNTYFP'] = df_HUD['COUNTY'].astype("str") # Change data type of column in data frame

### Add leading zeros
df_HUD['ZIP'] = df_HUD['ZIP'].str.rjust(5, "0") # add leading zeros of character column using rjust() function
df_HUD['STCOUNTYFP'] = df_HUD['STCOUNTYFP'].str.rjust(5, "0") # add leading zeros of character column using rjust() function

### Add labels to codes
df_HUD["ZCTA"] = "ZCTA"+ df_HUD['ZIP'] # Combine string with column
df_HUD["FIPS"] = "FIPS"+ df_HUD['STCOUNTYFP'] # Combine string with column

### Select Zip codes with max ratio
df_HUD = df_HUD.filter(["FIPS", "ZCTA", "TOT_RATIO", "ZIP"]) # Keep only selected columns
df_HUD = df_HUD.sort_values(by = ["ZCTA", "TOT_RATIO"], ascending = False) # Sort Columns by Value
df_HUD = df_HUD.drop_duplicates(subset = "ZCTA", keep = "first", inplace = False) # Drop all dupliacted values
df_HUD = df_HUD.drop(columns = ["TOT_RATIO"]) # Drop Unwanted Columns

### Verify
df_HUD.info() # Get class, memory, and column info: names, data types, obs.
df_HUD.head() # Print first 5 observations

## Step 4: Join to create ZCTA FIPS key

### Join with population data from ACS
df_key = pd.merge(df_HUD, df_D4D, on = "FIPS", how = "left") # Join by column while keeping only items that exist in both, select outer or left for other options

### Verify
df_key.info() # Get class, memory, and column info: names, data types, obs.
df_key.head() # Print first 5 observations

## Step 5: Create alternate labels

### Create state labels
states = {'ST':  ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MS', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
        'State': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
        } # Create pandas dataframe by hand by creating arrays of same lenght with lables and saving as object
df_states = pd.DataFrame (states, columns = ['ST','State']) # Create data frame in pandas

### Join with population data from ACS
df_label = pd.merge(df_key, df_states, on = "ST", how = "left") # Join by column while keeping only items that exist in both, select outer or left for other options

### Create alternate county name column
df_label["County"] = df_label["Name"] # Add new column based on existing
df_label['Name'] = df_label['Name'].str.replace(" County","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" Parish","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" City","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" Census Area","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" Borough","") # Strip all spaces from column in data frame
df_label['Name'] = df_label['Name'].str.replace(" and","") # Strip all spaces from column in data frame

### Create Uppercase label columns
df_label['NAME'] = df_label['Name'].str.upper() # Change column to uppercase
df_label['COUNTY'] = df_label['County'].str.upper() # Change column to uppercase
df_label['STATE'] = df_label['State'].str.upper() # Change column to uppercase

### Clean NA values
df_label = df_label.dropna() # Drop all rows with NA values

### Order columns alphabetically
df_label = df_label.reindex(sorted(df_label.columns), axis=1) # order columns alphabetically
df_label =  df_label.rename(columns = {"County": "COUNTY_L", "Name": "NAME_L", "State": "STATE_L"}) # Rename multiple columns in place

### Verify
df_label.info() # Get class, memory, and column info: names, data types, obs.
df_label.head() # Print first 5 observations

## Step 6: Export to database

### Order
df_hnb = df_label.rename(columns = {"County": "COUNTY_L", "Name": "NAME_L", "State": "STATE_L"}) # Rename multiple columns in place

### Write to CSV
df_hnb.to_csv(r"hnb/FIPS/FIPS_ZCTA_key.csv") # Clean in excel and select variable

### Conenct to database
con = sqlite3.connect('hnb/_database/HNB.db') # Save Connect to SQLite database as item
df_hnb.to_sql('FIPS_ZCTA_key', sqlite3.connect('hnb/_database/HNB.db'), if_exists = 'replace', index = False)