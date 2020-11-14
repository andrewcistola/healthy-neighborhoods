# Healthy Neighborhoods
A collection of public data sources at sub-state geographic layers with informative information on public health outcomes. 

## 2020 Release
The 2020 data release contains the following data sources at various levels. All metadata below applies to the `_staged` tables. Refer to specific documentation on the raw data. 

### US Census (USCensus) - American Community Survey (ACS)
Geographic layer: Zip Code <br>
Years Included: 2014-2018 5 year Percent Estimates <br>
Type of Information: Socio-economic indicators of the U.S. population <br>
Prefix: `acs_5YR2018_`<br>
Data key: `ZCTA`<br>
Subrepository: `ACS`

### Flordia Department Health (FDOH) - Top Causes of Mortality
Geographic Layer: Zip Code <br>
Years Included: 2014-2018 Population Rates<br>
Type of Information: Mortality Counts by ICD-10 Code<br>
Prefix: `fdoh_5YR2018`<br>
Data key: `ZCTA`<br>
Subrepository: `FLDOH`

### Health Resource Services Administration (HRSA) - Area Health Resource File (AHRF)
Geographic Layer: County or County Equivalent<br>
Years Included: 2014-2018 Averages or Population Rates<br>
Type of Information: Health care or Health relevant Resources Available<br>
Prefix: `ahrf_5YR2018`<br>
Data key: `FIPS`<br>
Subrepository: `AHRF`

### Beaureu of Economic Analysis (BEA) - Local GDP and Income Measures (GDP)
Geographic Layer: County or County Equivalent<br>
Years Included: 2014-2018 Averages or Population Rates<br>
Type of Information: Macroeconomic and Microeconomic measures from Tax Returns<br>
Prefix: `gdp_5YR2018`<br>
Data key: `FIPS`<br>
Subrepository: `BEA`

### Centers for Medicare and Medicaid Services (CMS) - Hospital Quality Payment Program (QPP)
Geographic Layer: Facility ID within County<br>
Years Included: 2020 Measures calculated from 2015-2018 claims<br>
Type of Information: Quality indicators and description used for Value Based Payments<br>
Prefix: `qpp_2020`<br>
Data key: `FID`<br>
Subrepository: `CMS`

## Repository Structure
The repository uses the following file organization and naming convenstions. This applies to all files in 2020 release and forward.

### File Naming Convention:
`version/subdirectory/prefix_suffix.ext`

### Subdirectories
`v#.#` All code files deployed for that specific release
<br>`_data` staged data files related to the project
<br>`_fig` graphs, images, and maps related to the project

### Suffixes:
`_code` Development code script for working in an IDE
<br>`_book` Jupyter notebook 
<br>`_stage` Data files that have been modified from raw source
<br>`_2020-01-01` Text scripts displaying results output from a script are marked with date stamp they were created
<br>`_map` 2D geographic display
<br>`_graph` 2D chart or graph representing numeric data

### PEP-8
Whenever possible code scripts follow PEP-8 standards. 

## Disclaimer
While the author (Andrew Cistola) is a Florida DOH employee and a University of Florida PhD student, these are NOT official publications by the Florida DOH, the University of Florida, or any other agency. 
No information is included in this repository that is not available to any member of the public. 
All information in this repository is available for public review and dissemination but is not to be used for making medical decisions. 
All code and data inside this repository is available for open source use per the terms of the included license. 

### allocativ
This repository is part of the larger allocativ project dedicated to prodiving analytical tools that are 'open source for public health.' Learn more at https://allocativ.com. 
