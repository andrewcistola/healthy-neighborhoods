# Healthy Neighborhoods
A collection of public data sources at sub-state geographic layers with informative information on public health outcomes. 

## About this Repository
For many public health research studies, data needs to be collected from a variety of public sources and the process can consume much of the research project. The Healthy Neighbrohoods Repository is an assembly of open access data from public sources that provide social, economic and environmental data below the state level The library consists of collected tables that connect the different data sources by the geographic identifier for a given year range. These tables are able to be analyzed using basic machine learning variable reduction techniques to develop models for informing further research, to inform evidence based screening methods, and to create risk assessment instruments.

## 2020 Release
The 2020 data release contains data from the following sources:<br>
<br>
US Census - American Community Survey<br>
Flordia Department Health - Florida Vital Statistics Top Causes of Mortality<br>
Centers for Medicare and Medicaid Services - Service Area File for Medicare Fee for Service<br>
Health Resource Services Administration - Area Health Resource File<br>
Centers for Medicare and Medicaid Services - Quality Payment Program<br>
<br>
The 2020 release can be accessed by downloading the 'hnb_2020.zip' file listed under 'Releases'

## Repository Contents
`release_2020` All files included in the 2020 Release<br>
`_archive` Old files from previous years<br>
`_raw` Collected raw data, documentation, and code for staging<br>
`allocativ_2.1.yml` Conda environment for use with repositories in the allocativ project<br>

## Repository Structure
The repository uses the following file organization.

### Subdirectories
`_data` staged data files related to the project<br>
`_fig` graphs, images, and maps related to the project<br>
`_archive` old files no longer used<br>
`_raw` raw data files, documentation, and code used for staging data<br>
`project` Files related to specifc project<br>
`README` Description, directory, notes

### File Naming:
`topic_prefix_suffix.ext`

### Topics:
Topics are assigned based on content and listed in the directory README

### Prefixes:
`alpha_` First draft of script, continuting with greek alphabet
`omega_` Final draft of script
`
### Suffixes:
`_code` Development code script for working in an IDE<br>
`_book` Jupyter notebook <br>
`_stage` Data files that have been modified from raw source<br>
`_2020-01-01` Text scripts with results output with date it was run<br>
`_map` 2D geographic display<br>
`_graph` 2D chart or graph representing numeric data

## Style:
Code scripts use the following style:

### PEP-8
Whenever possible code scripts follow PEP-8 standards. 

### Elective options:
Python and R code scripts use the following elective options:<br>
`=` for variable defintions (no `<-`)<br>
`''` for all character strings or arguments (no `""`) <br>
A single space is provided between each element ex. `columns = 'COlA'`<br>

### Naming Conventions:
Python and R code scripts use the following variable naming conventions:<br>
<br>
data frames: `df_xx`<br>
list: `l_xx`<br>
arrays: `a_xx`<br>
feature tables: `df_X`<br>
target tables: `df_Y`<br>


## Disclaimer
While the author (Andrew Cistola) is a Florida DOH employee and a University of Florida PhD student, these are NOT official publications by the Florida DOH, the University of Florida, or any other agency. 
No information is included in this repository that is not available to any member of the public. 
All information in this repository is available for public review and dissemination but is not to be used for making medical decisions. 
All code and data inside this repository is available for open source use per the terms of the included license. 

### allocativ
This repository is part of the larger allocativ project dedicated to prodiving analytical tools that are 'open source for public health.' Learn more at https://allocativ.com. 
