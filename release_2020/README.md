# Healthy Neighborhoods
A collection of public data sources at sub-state geographic layers with informative information on public health outcomes. 

## 2020 Release
The 2020 data release contains the following data sources at various levels. All metadata below applies to the `_staged` tables. Refer to specific documentation on the raw data. 

### US Census (USC) - American Community Survey (ACS)
Type of Information: ACS socio-economic indicators of the U.S. population `acs_`<br>
Years Included: 5 year 2014-2018 percent estimates `5Y2018_`<br>
Geographic Layer: Zip Code `ZCTA_`<br>
Scope: U.S. states, territories, districts
Status: Staged from raw data as comma delinated `staged.csv`
Filename: `acs_5Y2018_ZCTA_staged.csv`

### Centers for Medicare and Medicaid Services (CMS) - Health Services Area File for Medicare Fee for Service (FFS)
Type of Information: QPP hospital description and indicators for Value Based Payments `ffs_`<br>
Years Included: 2020 release using claims from 2015-2018 `2020_`<br>
Geographic Layer: Zip Code `ZCTA_`<br>
Scope: U.S. states, territories, districts
Status: Staged from raw data as comma delinated `staged.csv`<br>
Filename: `ffs_2020_FIPS_staged.csv`

### Flordia Department Health (FLDOH) - Vital Statistics Top Causes of Mortality (FLV)
Type of Information: VTLS by ICD-10 Code `flv_`<br>
Years Included: 5 year 2014-2018 Population Rates`5Y2018_`<br>
Geographic Layer: Zip Code `ZCTA_`<br>
Scope: Florida
Status: Staged from raw data as comma delinated `staged.csv`
Filename: `flv_5Y2018_ZCTA_staged.csv`

### Health Resource Services Administration (HRSA) - Area Health Resource File (AHRF)
Type of Information: AHRF Rates for health care occupations, facilties, and outcomes `ahrf_`<br>
Years Included: 5 year 2014-2018 Population Rates`5Y2018_`<br>
Geographic Layer: County or Equivalents `FIPS_`<br>
Scope: U.S. states, territories, districts
Status: Staged from raw data as comma delinated `staged.csv`
Filename: `ahrf_5Y2018_FIPS_staged.csv`

### Centers for Medicare and Medicaid Services (CMS) - Quality Payment Program (QPP)
Type of Information: QPP hospital description and indicators for Value Based Payments `qpp_`<br>
Years Included: 2020 release using claims from 2015-2018 `2020_`<br>
Geographic Layer: County or Equivalents `FIPS_`<br>
Scope: U.S. states, territories, districts
Status: Staged from raw data as comma delinated `staged.csv`<br>
Filename: `qpp_2020_FIPS_staged.csv`

### Repository contents:
`shape` Shape files for standard geographies<br>
`labels` Feature lables for selected tables
`acs_5Y2018_ZCTA_staged.csv` ACS file ready for use<br>
`flv_5Y2018_ZCTA_staged.csv` FLV file ready for use<br>
`ffs_5Y2018_ZCTA_staged.csv` FFS file ready for use<br>
`ahrf_5Y2018_FIPS_staged.csv` AHRF file ready for use<br>
`qpp_2020_FIPS_staged.csv` QPP file ready for use<br>

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
