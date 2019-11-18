National Climate Assessment - Extreme Heat Events:
Heat Wave Days in May - September for years 1981-2010

Summary:
	   	

The Extreme Heat Events data available on CDC WONDER are county-level measures of the number of heat wave days in the months of May through September spanning the years 1981-2010. Reported measures are the sum, average and standard deviation of the number of heat wave days occurring in the selected time and place. Three definitions are available for heat events: 95th percentile of daily maximum air temperature, 95th percentile of daily maximum Heat Index, and 95th percentile of Net Daily Heat Stress.

Data are available by county (all counties in the combined 48 contiguous states plus the District of Columbia), and year.

Source:
	   	

These measures were developed through a collaborative project that was funded by the NASA National Climate Assessment (NCA) Program among the following organizations: NASA Marshall Space Flight Center (MSFC), Universities Space Research Association (USRA), University of Alabama in Huntsville (UAH) and CDC. The team of this project developed these measures using meteorological data from the North American Land Data Assimilation System Phase 2 (NLDAS-2), which were originally acquired as part of the mission of the NASA Earth Science Division. NLDAS-2 data are archived and distributed by the Goddard Earth Sciences (GES) Data and Information Services Center (DISC). More information about the NLDAS project and raw data can be found at http://hydro1.sci.gsfc.nasa.gov/data/s4pa/NLDAS/README.NLDAS2.pdf.

In a study funded by NCA (fully cited below), scientists at NASA MSFC/USRA developed computer programs to process the NLDAS-2 data and extract the hourly air temperature, specific humidity, and atmospheric pressure data, and compute the daily Maximum Air Temperature, Maximum Heat Index (HI), and Net Daily Heat Stress (NDHS) that were used to compute the extreme heat events measures. They also identified in a Geographic Information System (GIS) the associated geographic locations of the centroids of the gridded NLDAS-2 data in terms of the counties and states they fall into so that the data can be aggregated to these geographic levels.

Net Daily Heat Stress is defined as:

NDHS = ∑(HIi - HIhot) - ∑(Tcool - Ti)

where the summations are over the hours in the day, but only positive terms are included. In other words, the first sum, which represents the heat stress, is only calculated for hours when HIi > HIhot, and the second term, representing heat relief, only when Ti < Tcool. By these rules, NDHS is constrained to be greater than or equal to zero. The units of NDHS are degree-hours, where degrees are in Fahrenheit. HIhot = a threshold above which HI is considered a stressor, set to 90° F in this analysis, and Tcool = temperature below which relief from heat occurs, set to 75° F. Temperature is used instead of Heat Index in the second term because the HI definition is restricted to temperatures of 80° F and above.

See also Data Source Information and Additional Information.
In WONDER: 	   	You can produce tables, maps, charts, and data extracts. Obtain the sum, average and standard deviation for the number of heat waves days, as defined by these three definitions for heat events: 95th percentile of daily maximum air temperature, 95th percentile of daily maximum Heat Index, and 95th percentile of Net Daily Heat Stress. Select specific criteria to produce cross-tabulated measures of heat events. Data are organized into three levels of geographic detail: the 48 contiguous states, state, and county. You can limit your data by any of the place or time categories, and index your data by county and by year.
Contents: 	   	Heat Wave Days Data Request
Data Source Information
Additional Information
Data Request
Output: 	   	You can produce tables, maps, charts, and data extracts. Obtain the sum of the number of heat wave days, the average number of heat wave days, and the standard deviation, for three definitions for heat events: 95th percentile of Daily Maximum Air Temperature, 95th percentile of Daily Maximum Heat Index, and 95th percentile of Net Daily Heat Stress. Select specific criteria to produce cross-tabulated measures of heat events. Data are organized into three levels of geographic detail: the 48 contiguous states, state and county. You can limit and index your data by county and by year.
Variables: 	   	You can index your data by county and by year, and you can limit our data by any and all of these variables:

    Location: State, County
    Year:1981-2010 (months May - September) 

How? 	   	The Request screen has sections to guide you through the making a data request as step-by-step process. However, to get your first taste of how the system works, you might want to simply press any Send button, and execute the default data request. The data results for your query appear on the Table screen. After you get your data results, try the Chart and Map screens. Or export your data to a file (tab-delimited line listing) for download to your computer.
For more information, see the Quick Start Guide and the following steps:

    Organize table layout
    Select location
    Select year, month, day
    Select values for fine particulate matter
    Other options 

'By-Variables' 	   	Select variables that serve as keys (indexes) for organizing your data. See "How do I organize my data?" for more information.
Note:   To map your data, you must select at least one geographical location as a "By-Variable" for grouping your data, such as State or County.
Help: 	   	Click on any button labeled "Help", located to the right hand side of the screen at the top of each section. Each control's label, such as the "Location" label next to the Location entry box, is linked to the on-line help for that item.
Send: 	   	Sends your data request to be processed on the CDC WONDER databases. The Send buttons are located on the bottom of the Request page, and also in the upper right corner of each section, for easy access.

Step 1. Organize table layout:
Group Results By: 	   	Select up to five variables that serve as keys for grouping your data. See Group Results By below for hints.
Optional Measures: 	   	If checked, these optional measures will also appear in the results table. You must select at least one measure:

    Sum of the number of heat wave days;
    Average or mean of the number of heat wave days;
    Standard deviation of the number of heat wave days. 

The three summary measures of the number of heat wave days are available for these three definitions of heat events:

    Number of heat waved days based on Daily Maximum Air Temperature (for days above 95th percentile in the months of May - September);
    Daily Maximum Heat Index, (for days above 95th percentile in the months of May - September)
    Net Daily Heat Stress (for days above 95th percentile in the months of May - September) 

Title: 	   	Enter any desired description to display as a title with your results.
Group Results By...

Select the variables that serve as keys for grouping your data. For example, you could select to group (summarize, stratify, index) your data by Year and by County.
How?    See "How do I organize my data?" for more information.

Hints:   

    About charts:
    You cannot make charts when your data has more than two By-Variables.
    About maps:
    To make a map, you must request data with a geographic location variable, such as County, as the first "By-Variable" in the "Group Results By" box. Send your data request, then click the Map tab when you get the results. 

Number of Heat Wave Days

The average number of heat wave days summary measure is the mean value of all of the heat wave days per county that met the criteria for this cell in the results table. For example, if results are grouped by County and limited to Alabama for year 1981, then the table shows the average number of heat waves days for each of the counties in Alabama in 1981, for the months May - September.

How?

    Go to section 1. Organize table layout on the Request Form tab.
    Then select the checkbox labeled "Average number of heat wave days" under the desired measurement in the "Select Measures" heading. 

Notes:

    The average number of heat wave days summary measure is the mean value of the number of heat wave days that met the selected criteria for time and place.
    This dataset defines heat wave days based on daily air temperature, Heat Index and Net Daily Heat Stress measurements per geographic-area (14x14 kilometer square) grid covering the 48 contiguous United States (not including Alaska and Hawaii) plus the District of Columbia.
    NLDAS temperature measurements are recorded for 1/8-degree (14x14 kilometer square) geographic-area grid cells in the selected area. Temperature measurements from each grid cell are assigned to the county where the grid cell centroid is located. Some counties are so small that no centroids are located in the county; temperature measurements from the grid cell that covers the greatest county area are assigned to such counties. WONDER aggregates the grid-level measurements into counties and larger areas. The county locations are from the 2010 Federal Information Processing (FIPS) code set.
    Note that maximum Heat Index data are sparse because Heat Index data are recorded only for days when the air temperature is at or above 80 degrees Fahrenheit (26.7 degrees Celsius). See Additional Information for more information about Heat Index data. 

Standard Deviation

The standard deviation shows the variation from the average or mean value that occurs in the county-level values that meet the place and time criteria that define the table cell. A low standard deviation value indicates that most data values are close to the mean, and a high standard deviation value indicates the data are spread over a large range of values. For example, for the District of Columbia or year years 1981-2010, the standard deviation compares the 30 years of values, as the district represents the equivalent of one county in any single year. For Alabama for any single year, the standard deviation compares the number of heat waves days in the 67 counties in Alabama. For any single county in a single year, there is only one value representing the number of heat wave days, and the standard deviation is thus zero.

How? Select the checkbox labeled "Standard Deviation" under the "Optional Measures" heading in section 1. Organize table layout on the Request Form.

Notes:

    This dataset contains the number of heat wave days per year, summarized to the county-level, from 14 kilometer square grid cells covering the 48 contiguous United States (not including Alaska and Hawaii) plus the District of Columbia.
    This dataset defines heat wave days based on daily air temperature, Heat Index and Net Daily Heat Stress measurements per geographic-area (14x14 kilometer square) grid covering the 48 contiguous United States (not including Alaska and Hawaii) plus the District of Columbia.
    NLDAS temperature measurements are recorded for 1/8-degree (14x14 kilometer square) geographic-area grid cells in the selected area. Temperature measurements from each grid cell are assigned to the county where the grid cell centroid is located. Some counties are so small that no centroids are located in the county; temperature measurements from the grid cell that covers the greatest county area are assigned to such counties. WONDER aggregates the grid-level measurements into counties and larger areas. The county locations are from the 2010 Federal Information Processing (FIPS) code set.
    Note that maximum Heat Index data are sparse because Heat Index data are recorded only for days when the air temperature is at or above 80 degrees Fahrenheit (26.7 degrees Celsius). See Additional Information for more information about Heat Index data. 

Step 2. Select location and year:
Select the place and time of interest:

    Location:   the 48 contiguous United States plus District of Columbia by State, and County
    Year:  1981-2010 

Location

Data are available for the United States by State and County. Select the location(s) for the query. Any number of locations can be specified here.
How?

    See "How do I use a Finder?" for more information.
    See Finder Tool help for more hints. 

Hints:

    The default is all values (the United States).
    The Advanced mode let you easily pick several items from different parts of the list. Items are not selected until you click the "Move" button in Advanced mode. You may also enter values by hand, one code per line, in the Advanced mode. Use the Finder to see the correct code format. For example, 05 is the Arkansas state code.
    The "plus" symbol, "+" indicates that you can open the item, to see more items below it.
    The results to a search are shown in blue, and indicated by ">". 

State
For state level data, you can select any combination of individual states. When the Location Finder selection is at the default, the query includes the 48 contiguous United States and the District of Columbia, Alaska and Hawaii are not included in these data.
How?  

    See Location above for instructions.
    See also Group Results By in Step 1. 

Notes:  

    The states and the District of Columbia are identified by both state name and Federal Information Processing Standard (FIPS) codes in data extracts. See About FIPS Codes below. 

County
County-level data are available for the 48 contiguous United States and the District of Columbia. For county level data, you can select any combination of individual counties, or group by County. When the Location Finder selection is at the default "all" setting, the query includes data for the 48 contiguous United States and the District of Columbia. Alaska and Hawaii are not included in these data.
How?  

    See Location above for instructions.
    See also Group Results By in Step 1. 

Notes:  

    The county values represent the spatial averages of data from 14x14 kilometer square (1/8 degree) geographic area grid cells. Grids cells are associated with the county that includes the grid centroid. For small counties where no grid centroid fell within county boundaries, county data are aggregated from grids where most of the grid area fell within county boundaries.
    Counties and the District of Columbia are identified by both county name and FIPS codes in data extracts. The county locations are from the 2010 FIPS code set.
    About FIPS Codes:   The FIPS state and county codes were established by the National Bureau of Standards, U.S. Department of Commerce in 1968. This standard set of codes provides names and codes for counties and county equivalents of the 50 states of the United States and the District of Columbia. Counties are considered to be the "first order subdivisions" of each state, regardless of their local designation (county, parish, borough, census area). Washington, D.C.; the consolidated government of Columbus City, Georgia; the independent cities of the states of Maryland, Missouri, Nevada, and Virginia; and the census areas and boroughs of Alaska are identified as county equivalents. The system is standard throughout the Federal Government. The state codes are ascending, two-digit numbers; the county codes are ascending three-digit numbers. For both the state and county codes, space has been left for new states or counties. Some changes in the FIPS codes and county boundaries have occurred since 1968. See Location Updates for information on how these changes affect the data.
    About County Changes:   Comparable measures may be misleading for counties with changing boundaries. See Location Updates for information on how these changes affect the data. Due to boundary changes, data are available for some counties for a limited period of time. The following county-level constraints apply to the data:
        Alaska: data for Alaska are not included here.
        Arizona: La Paz County
        Heat Waves Days are available for the area for all years 1981-2010. Population estimates are available for La Paz County, Arizona (FIPS code 04012) for 1994 and later years. Prior to 1994, population estimates for La Paz are aggregated with those for Yuma, Arizona (FIPS code 04027).
        Colorado: Broomfield County
        Heat Waves Days are available for the area for all years 1981-2010. Population estimates for Broomfield county, Colorado (FIPS code 08014) are available for 2003 and later years. Prior to 2003, population estimates for Broomfield county are attributed to four adjacent counties: Adams (FIPS code 08001), Boulder (FIPS code 08013), Jefferson (FIPS code 08059), and Weld (FIPS code 08123). Populations for these four counties are reduced in 2003 due to the formation of Broomfield county.
        Hawaii: data for Hawaii are not included here.
        Montana: Park County Heat Waves Days are available for the area for all years 1981-2010. Population estimates for Park county, Montana (FIPS code 30067) include aggregated population estimates from adjacent Yellowstone National Park, Montana (FIPS code 30113) for years 1981-1988. Beginning in 1989, population estimates for the Montana portion of Yellowstone National Park (former county equivalent FIPS code 30113) are included in Gallatin, Montana (FIPS code 30031) and Park, Montana (FIPS code 30067).
        New Mexico: Cibola County
        Heat Waves Days are available for the area for all years 1981-2010. Population estimates for Cibola county, New Mexico (FIPS code 35006) are available for 1989 and later years. Prior to 1989, population estimates for Cibola county are aggregated with Valencia county, New Mexico (FIPS code 35061).
        Virginia: Alleghany County
        Heat Waves Days are available for the area for all years 1981-2010. Population estimates for Clifton Forge City, Virginia (FIPS code 51560) are aggregated with Alleghany County, Virginia (FIPS code 51005) for all years 1981-2010.
        Virginia: Halifax County
        Heat Waves Days are available for the area for all years 1981-2010. Population estimates for South Boston City, Virginia (FIPS code 51780) are aggregated with Halifax County, Virginia (FIPS code 51083) for all years 1981-2010. 

Year
Select any single year or combination of years from 1981-2010. The data represents the number of heat wave days in the period May through September in the selected year(s).
How?   See "How do I select items from the list box?"

Step 3. Other options:
Export Results: 	   	If checked query results are exported to a local file. More information on how to import this file into other applications can be found here.
How? See "How do I use a checkbox?"
Show Totals: 	   	If checked totals and sub-totals will appear in the results table.
How? See "How do I use a checkbox?"
Show Zero Values: 	   	If checked, rows containing zero counts are included in the results table. If unchecked, zero count rows are not included.
How? See "How do I use a checkbox?"
Precision: 	   	Select the precision for rate calculations. When the rate calculated for a small numerator (incidence count) is zero, you may increase the precision to reveal the rate by showing more numbers to the right of the decimal point.
How? See "How do I select items from the list box?"
Data Access Timeout: 	   	This value specifies the maximum time to wait for the data access for a query to complete. If the data access takes too long to complete, a message will be displayed and you can increase the timeout or simplify your request. If you can't complete a request using the maximum timeout, contact user support and we will try to run a custom data request for you.
How? See "How do I select items from the list box?"
Data Source Information
Data Sources: 	   	

These measures were developed through a collaborative project that was funded by the NASA National Climate Assessment Program among the following organizations: NASA Marshall Space Flight Center (MSFC), Universities Space Research Association (USRA), University of Alabama in Huntsville (UAH) and CDC. The team of this project developed these measures using meteorological data from the North American Land Data Assimilation System Phase 2 (NLDAS-2), which were originally acquired as part of the mission of the NASA Earth Science Division. NLDAS-2 data are archived and distributed by the Goddard Earth Sciences (GES) Data and Information Services Center (DISC). More information about the NLDAS project and raw data can be found at http://hydro1.sci.gsfc.nasa.gov/data/s4pa/NLDAS/README.NLDAS2.pdf.

In a study funded by the NCA (fully cited below), scientists at NASA USRA developed computer programs to extract from the NLDAS-2 data the hourly air temperature, specific humidity, and atmospheric pressure data, and compute the daily Maximum Air Temperature, Maximum Heat Index, and Net Daily Heat Stress (defined above) that were used to compute the extreme heat events measures. They also identified in a GIS the associated geographic locations of the centroids of the gridded NLDAS-2 data in terms of the counties and states they fall into, so it can be aggregated to different geographic levels in CDC WONDER.

To learn more about the methods and source of the NLDAS-2 data, please reference:

    Goddard Space Flight Center (GSFC) North America Land Data Assimilation System (NLDAS) web site
    NLDAS-2 Readme file
    National Oceanic and Atmospheric Administration (NOAA) North America Land Data Assimilation System web site 

See also Data Source Citations and Additional Information below.

Additional Information
Suggested Data Source Citations: 	   	

National Climate Assessment - Extreme Heat Events: Heat Wave Days in May - September for years 1981-2010 on CDC WONDER Online Database, released 2015.

The suggested citation including the original series for the data is shown below each table, chart or map.
Contact: 	   	For data questions that are not addressed in this document, e-mail bill.crosson@nasa.gov or mohammad.alhamdan@nasa.gov.
Acknowledgements: 	   	This work was part of a collaborative study funded by the NASA NCA Program, whose team members are:

    Dr. Dale Quattrochi (PI), Earth Science Office, NASA/MSFC
    Dr. William Crosson (Co-I), USRA, NASA/MSFC
    Dr. Mohammad Al-Hamdan (Co-I), USRA, NASA/MSFC
    Mr. Maurice Estes, Jr. (Co-I), UAH, NASA/MSFC
    Ms. Sue Estes (Co-I), UAH, NASA/MSFC

Other Topics: 	   	

Reference the following topics:

    Heat event definitions:
        About Daily Maximum Air Temperature
        About Daily Maximum Heat Index
        About Heat Index Methodology
        About Net Daily Heat Stress 
    About Population Data Sources
    Locations: About County Level Changes
    Contact for Data Questions
    Suggested Citation 

About Heat Events Defined by Daily Maximum Air Temperature

Daily maximum air temperature values are spatial averages of the daily maximum air temperatures recorded for each 14 x 14 kilometer square grid cell, aggregated to the county level by simple arithmetic averaging. For each county, the 95th percentile of daily maximum air temperature was determined for all days in May - September based on NLDAS data from the period 1981-2010. Based on these percentiles, heat events for daily maximum air temperature were defined as any period of at least two consecutive days on which the county maximum air temperature reached or exceeded the 95th percentile. When this condition was met, each of the consecutive days was identified as a "heat event day" for this definition.
About Heat Events Defined by Daily Maximum Heat Index

Daily maximum Heat Index values are spatial averages of the daily maximum Heat Indices recorded for each 14 x 14 kilometer square grid cell, aggregated to the county level by simple arithmetic averaging. For each county, the 95th percentile of daily maximum Heat Index was determined for all days in May - September based on NLDAS data from the period 1981-2010. Based on these percentiles, heat events for daily maximum Heat Index were defined as any period of at least two consecutive days on which the county maximum Heat Index reached or exceeded the 95th percentile. When this condition was met, each of the consecutive days was identified as a "heat event day" for this definition.
About Heat Index Methodology

Heat Index (HI) data are available for days with temperatures at or above 80 degrees Fahrenheit or 26.7 degrees Celsius.

The formula used to calculate the hourly Heat Index, in degrees Fahrenheit, from which the daily maximum Heat Index was computed, is:

HI = -42.379 + 2.04901523*T + 10.14333127*RH - 0.22475541*T*RH - 0.00683783*T2 - 0.05481717*RH2 + 0.00122874*T2 *RH + 0.00085282*T*RH2 - 0.00000199*T2 *RH2

where
    T = air temperature (in degrees Fahrenheit) 
    RH = relative humidity (percentage)

    The formula above is a multiple regression equation fit to the original table of theoretical values published in Steadman, R.G., 1979: The assessment of sultriness. Part I: A temperature-humidity index based on human physiology and clothing science. J. Appl. Meteor., 18, 861-873.

    The equation originates from: Lans P. Rothfusz. "The Heat Index 'Equation' (or, More Than You Ever Wanted to Know About Heat Index)", Scientific Services Division (NWS Southern Region Headquarters), 1 July 1990.
    About Heat Event Defined by Net Daily Heat Stress (NDHS)

    Daily NDHS values are spatial averages of the daily NDHS recorded for each 14 x 14 kilometer square grid cell, aggregated to the county level by simple arithmetic averaging. For each county, the 95th percentile of NDHS was determined for all days in May - September based on NLDAS data from the period 1981-2010. Based on these percentiles, heat events for NDHS were defined as any period of at least two consecutive days on which the county NDHS reached or exceeded the 95th percentile and exceeded zero. When this condition was met, each of the consecutive days was identified as a "heat event day" for this definition.

    Net Daily Heat Stress is defined as:

    NDHS = ∑(HIi - HIhot) - ∑(Tcool - Ti)

    where the summations are over the hours in the day, but only positive terms are included. In other words, the first sum, which represents the heat stress, is only calculated for hours when HIi > HIhot, and the second term, representing heat relief, only when Ti < Tcool. By these rules, NDHS is constrained to be greater than or equal to zero. The units of NDHS are degree-hours, where degrees are in Fahrenheit. HIhot = a threshold above which HI is considered a stressor, set to 90° F in this analysis, and Tcool = temperature below which relief from heat occurs, set to 75° F. Temperature is used instead of Heat Index in the second term because the HI definition is restricted to temperatures of 80° F and above.

    About Population Data Sources

    The population data are derived from U.S. Census Bureau files. The population estimates for the Census years: 1970, 1980, 1990, 2000, and 2010 are April 1, modified census counts. The population estimates for the non-Census years: 1981-89, 1991-99, and 2001-09 are intercensal estimates of the July 1, resident population. County level population estimates for years 1981-2010 are consistent with the current Compressed Mortality data collection produced by the National Center for Health Statistics. The population estimates are from the following sources:

        1981-89 Population Estimates

        County-level estimates are U.S. Census Bureau intercensal estimates of the July 1 resident population. In this Extreme Heat Event data collection, national, state population figures are the sum of county estimates.
        1990 Population Estimates

        The county population estimates are from the April 1, 1990 age-race-sex modified census counts. National and state estimates are the sum of the county census counts. The original census counts were modified by the U.S. Census Bureau to correct bias in reported age, and to assign persons who reported their race as "other" to one of the four single-race groups specified in the Office of Management and Budget (OMB) 1977 Standards on Race and Ethnicity: White, Black, American Indian or Alaska Native, and Asian or Pacific Islander.
        1991- 1999 Population Estimates

        The county population estimates are U.S. Census Bureau bridged-race intercensal estimates of the July 1, resident population, based on the 1990 census and the bridged-race 2000 census. The national and state estimates are the sum of the bridged-race county estimates. The data source is the 1990 to 1999 intercensal estimates of the July 1 resident population by year, county, 5-year age groups, bridged-race, sex, and Hispanic origin released by NCHS on April 15, 2003. For more information, see U.S. Census Populations With Bridged Race Categories.
        2000 Population Estimates

        County population estimates are from the U.S. Census Bureau April 1, bridged modified race 2000 Census counts. National, state population figures are the sum of county estimates. For more information, see U.S. Census Populations With Bridged Race Categories.
        2001 - 2009 Population Estimates

        The population estimates for 2001-2009 are July 1 resident population estimates from the U.S. Census Bureau's revised bridged-race intercensal series, based on the year 2000 and the year 2010 census counts (released by NCHS on 10/26/2012). National, state and county estimates are the sum of county estimates. For more information, see U.S. Census Populations With Bridged Race Categories.
        2010 Population Estimates

        National, state, and county population estimates are from the U.S. Census Bureau April 1, bridged modified race 2010 Census counts. The original census counts were modified by the U.S. Census Bureau to assign persons who reported their race as "other" to one of the 31 single or multiple-race groups specified in the Office of Management and Budget (OMB) 1997 Standards on Race and Ethnicity. The resulting counts were then bridged to (made consistent with) the four single-race categories (White, Black, American Indian or Alaska Native, and Asian or Pacific Islander). National, state and county estimates are the sum of county estimates. For more information, see U.S. Census Populations With Bridged Race Categories.

    Location Updates: notes about specific county-level changes in boundaries and codes

    Comparable measures may be misleading for counties with changing boundaries. The data collection may lag behind some FIPS location code changes. This dataset uses the 2010 FIPS county codes. Some places, such as independent cities and New York City boroughs are included as unique locations in the data. Some county and census tract area (CA) locations are not included, instead the data are associated with a neighboring county or the previous location name and FIPS code. The list below of county-level changes is organized alphabetically by state name and then county name.

        Alaska:
        Data are not available for the state of Alaska, nor Alaskan boroughs and census areas, in the 1981-2010 heat waves days data set.
        Arizona: La Paz County
        Population estimates are available for La Paz County, Arizona (FIPS code 04012) for 1994 and later years. Prior to 1994, population estimates for La Paz are aggregated with those for Yuma, Arizona (FIPS code 04027). Heat Waves Days are available for the area for all years 1981-2010.
        Colorado: Broomfield County
        Broomfield County, Colorado (FIPS code 08014) was created effective November 15, 2001 from parts of four counties: Adams, Boulder, Jefferson, and Weld. Heat Wave Days are available for this area, yet population data are not available for Broomfield County before 2003. Prior to year 2003, population estimates for this area are attributed to four adjacent counties: Adams (FIPS code 08001), Boulder (FIPS code 08013), Jefferson (FIPS code 08059), and Weld (FIPS code 08123). Populations for these 4 counties are reduced in 2003 due to the formation of Broomfield county.
        Florida: Miami City and Dade County
        Dade county, Florida (FIPS code 12025) was renamed Miami-Dade County and its FIPS code changed to 12086, effective November 13, 1997. The label and code, Miami-Dade County (FIPS code 12086), are used here, and the area includes Miami City.
        Hawaii:
        Data for Hawaii are not included in the 1981-2010 heat waves days data set.
        Maryland: Baltimore City and Baltimore County
        The independent city of Baltimore, Maryland has been treated as a county. Data are reported separately for Baltimore City (FIPS code 24510) and Baltimore County (FIPS code 24005).
        Missouri:
            St. Genevieve County, Missouri
            In order to achieve alphabetical consistency, the FIPS code for St. Genevieve, Missouri was changed in 1979 from 29193 to 29186. The new code (29186) is used here.
            St. Louis City and St. Louis County, Missouri
            The independent city of St. Louis, Missouri has been treated as a county. Data are reported separately for St. Louis City (FIPS code 29510) and St. Louis County (FIPS code 29189). 
        Montana: Park County Population estimates for Park county, Montana (FIPS code 30067) include aggregated population estimates from adjacent Yellowstone National Park, Montana (FIPS code 30113) for years 1981-1988. Beginning in 1989, population estimates for the Montana portion of Yellowstone National Park (former county equivalent FIPS code 30113) are included in Gallatin, Montana (FIPS code 30031) and Park, Montana (FIPS code 30067).
        Nevada: Carson City
        The independent city of Carson City, Nevada (FIPS code 32510) has been treated as a county. Data are shown separately from the adjacent counties for Carson City, Nevada.
        New Mexico: Cibola County
        Population estimates for Cibola county, New Mexico (FIPS code 35006) are available for 1989 and later years. Prior to 1989, population estimates for Cibola county are aggregated with Valencia county, New Mexico (FIPS code 35061). Heat Waves Days are available for the area for all years 1981-2010.
        New York: New York City boroughs
        The five boroughs of New York City have been treated as counties and maintained as separate entities.
        Borough 	County 	FIPS Code
        Bronx 	Bronx 	36005
        Brooklyn 	Kings 	36047
        Manhattan 	New York 	36061
        Queens 	Queens 	36081
        Staten Island   	Richmond   	36085
        Virginia independent cities:
            Clifton Forge City and Alleghany County, Virginia
            On July 1, 2001, Clifton Forge City, Virginia (FIPS code 51560), formerly an independent city, merged with Alleghany county (FIPS code 51005). Data for Clifton Forge City are aggregated with Alleghany county, Virginia (FIPS code 51005) for all years 1981-2010.
            Nansemond City and Suffolk City, Virginia
            Nansemond City, Virginia (FIPS code 51123) has been part of the independent city of Suffolk, VA (FIPS code 51800) since 1979. For all years, data for Nansemond are aggregated and reported with those for Suffolk City.
            South Boston City and Halifax County, Virginia
            Data for South Boston City, Virginia (FIPS code 51780) are aggregated with Halifax County, Virginia (FIPS code 51083) for all years 1981-2010.
            Table of Virginia's Independent Cities
            The following Virginia independent cities are treated as counties and appear on the data with the following FIPS codes:
            FIPS 	  		Independent City
            51510 	  		Alexandria city, Virginia
            51515 	  		Bedford city, Virginia
            51520 	  		Bristol city, Virginia
            51530 	  		Buena Vista city, Virginia
            51540 	  		Charlottesville city, Virginia
            51550 	  		Chesapeake city, Virginia
            51570 	  		Colonial Heights city, Virginia
            51580 	  		Covington city, Virginia
            51590 	  		Danville city, Virginia
            51595 	  		Emporia city, Virginia
            51760 	  		Richmond city, Virginia
            51770 	  		Roanoke city, Virginia
            51775 	  		Salem city, Virginia
            51790 	  		Staunton city, Virginia
            51800 	  		Suffolk city, Virginia
            51810 	  		Virginia Beach city, Virginia
            51820 	  		Waynesboro city, Virginia
            51830 	  		Williamsburg city, Virginia
            51840 	  		Winchester city, Virginia



This page last reviewed: Tuesday, January 05, 2016
This information is provided as technical reference material. Please contact us at cwus@cdc.gov to request a simple text version of this document.

    Email
    Recommend
    Tweet
    YouTube
    Instagram

    Listen
    Watch
    RSS

        About CDC Jobs Funding 
        Policies Privacy FOIA No Fear Act OIG 

    1600 Clifton Road Atlanta, GA 30329-4027 USA
    800-CDC-INFO (800-232-4636), TTY: 888-232-6348
    Email CDC-INFO
    U.S. Department of Health & Human Services
    HHS/Open
    USA.gov

