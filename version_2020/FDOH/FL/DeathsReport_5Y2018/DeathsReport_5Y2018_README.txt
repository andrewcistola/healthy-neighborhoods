http://www.flhealthcharts.com/FLQUERY/Death/DeathCount.aspx

Raw download - FloridaDeathsReport.xls

Download date - 15 July 2020

Saved report from online query tool - OlapReportSet.xml

Staged Data - FL_113_stage.csv

Steps taken to stage - 

1. Delete row 1-3,1542-1543
2. Delete column T, U
3. Insered row above row 1 as copy of row 1
4. Used formula =RIGHT(B2,LEN(B2)-FIND(" (",B2)) on row 1
5. Changed names Benign, Abnormal, SIDS
6. Used formula =SUBSTITUTE(Text, "(", "") and =SUBSTITUTE(B3, ")", "") and =SUBSTITUTE(B2, "-", "_") on row 1
7. Added column with ZCTA in front of ZIP
8. saved as FL_113_stage.csv
9. transposed row 1 and 2 as FL_113_key.csv

Notes - 

Zip codes appear multiple times based on how they fall between counties
Counts refer to the individual deaths recorded within each county for a given zip code


Staged Data - FL_113_mort_stage.csv

Steps taken to stage - 
1. Used FL_113_mort_stage.py to join population data from 2014-2018 ACS data and group sum zip codes
2. Used forumla =B2/$R2*1000 to create population adjusted mortality rates
3. Added "_R1000" to feature labels to denote population rate per 1000k

