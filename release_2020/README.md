# Healthy Neighborhoods
A collection of public data sources at sub-state geographic layers with informative information on public health outcomes. 

## 2020 Release
The 2020 data release contains the following data sources at various levels. All metadata below applies to the `_staged` tables. Refer to specific documentation on the raw data. 

### US Census - American Community Survey (ACS)
Type of Information: ACS socio-economic indicators of the U.S. population `acs_`<br>
Years Included: 5 year 2014-2018 percent estimates `5Y2018_`<br>
Geographic Layer: Zip Code `ZCTA_`<br>
Status: Staged from raw data as comma delinated `staged.csv`
Filename: `acs_5Y2018_ZCTA_staged.csv`

### Flordia Department Health - Vital Statistics Top Causes of Mortality (FLDOH)
Type of Information: VTLS by ICD-10 Code `fldoh_`<br>
Years Included: 5 year 2014-2018 Population Rates`5Y2018_`<br>
Geographic Layer: Zip Code `ZCTA_`<br>
Status: Staged from raw data as comma delinated `staged.csv`
Filename: `fldoh_5Y2018_ZCTA_staged.csv`

### Health Resource Services Administration - Area Health Resource File (AHRF)
Type of Information: AHRF Rates for health care occupations, facilties, and outcomes `ahrf_`<br>
Years Included: 5 year 2014-2018 Population Rates`5Y2018_`<br>
Geographic Layer: County or Equivalents `FIPS_`<br>
Status: Staged from raw data as comma delinated `staged.csv`
Filename: `ahrf_5Y2018_FIPS_staged.csv`

### Beaureu of Economic Analysis - Local GDP and Income Measures (BEA)
Type of Information: BEA collected economic indicators `bea_`<br>
Years Included: 5 year 2014-2018 median values `5Y2018_`<br>
Geographic Layer: County or Equivalents `FIPS_`<br>
Status: Staged from raw data as comma delinated `staged.csv`
Filename: `bea_5Y2018_FIPS_staged.csv`

### Centers for Medicare and Medicaid Services - Quality Payment Program (CMS)
Type of Information: QPP hospital description and indicators for Value Based Payments `cms_`<br>
Years Included: 2020 release using claims from 2015-2018 `2020_`<br>
Geographic Layer: County or Equivalents `FIPS_`<br>
Status: Staged from raw data as comma delinated `staged.csv`<br>
Filename: `cms_2020_FIPS_staged.csv`

### Repository contents:
`FLDOH` Code and raw data for FLDOH<br>
`ACS` Code and raw data for ACS<br>
`AHRF` Code and raw data for AHRF<br>
`BEA` Code and raw data for BEA<br>
`CMS` Code and raw data for CMS<br>
`SHAPE` Shape and crosswalk files for standard geographies and labels<br>
`acs_5Y2018_ZCTA_staged.csv` ACS file ready for use<br>
`fldoh_5Y2018_ZCTA_staged.csv` FLV file ready for use<br>
`ahrf_5Y2018_FIPS_staged.csv` AHRF file ready for use<br>
`bea_5Y2018_FIPS_staged.csv` BEA file ready for use<br>
`cms_2020_FIPS_staged.csv` CMS file ready for use<br>

### Notes for use:
- Each csv file is ready to be joined to a table of your choice. 
- The table use the common label `ZCTA` for Zip Codes, and `FIPS` for County
- In order to work with geographi labels leading with `0`, `ZCTA` and `FIPS` are appended to the front of each value in the column (ex. `ZCTA3260`)
- Raw files, code for staging, and documentation are available with the subrepository folders

## Disclaimer
While the author (Andrew Cistola) is a Florida DOH employee and a University of Florida PhD student, these are NOT official publications by the Florida DOH, the University of Florida, or any other agency. 
No information is included in this repository that is not available to any member of the public. 
All information in this repository is available for public review and dissemination but is not to be used for making medical decisions. 
All code and data inside this repository is available for open source use per the terms of the included license. 

### allocativ
This repository is part of the larger allocativ project dedicated to prodiving analytical tools that are 'open source for public health.' Learn more at https://allocativ.com. 
