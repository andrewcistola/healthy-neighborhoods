https://www.census.gov/programs-surveys/popest/geographies/reference-files.html

Raw Downloads - all-geocodes-v2019.xlsx

Data used to stage - all-geocodes-v2019.xlsx

Staged data - FIPS_staged.csv

1. Deleted rows 1-4
2. Deleted rows with summary 10 (Country) 40 (State), 61 (township), 162 (village)
3. Deleted columns A, D, E, F
4. Used TEXT formula to add leading zeros to State and Column (00, and 000)
5. Used CONCAT to combine state and county codes into five digits and named County
6. Deleted original County Column
5. Renamed Area Name as Name

Downloaded July 10 2020