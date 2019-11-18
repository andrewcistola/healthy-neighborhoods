**** TOOLBOX - NHANES Population Counts

**Prediabetes Cost of Prevention Study**
*Merge and sorting the NHANEs Dataset to find population with undiagnosed prediabetes*
*Variables are stored in E:\NHANES\ for easy access for individual projects*
*Saved libraries correspond to years of NHANES

**Prep Code: Set Libraries;

libname NH "E:\NHANES\2015-2016\DATA";
libname PR "E:\Project";
run;

**Step 1: Sort SEQN variables;

proc sort 
data = NH.DEMO_I;
by SEQN; 
run;
proc sort 
data = NH.DIQ_I;
    by SEQN; 
run;


**Step 2: Merge Variables into one dataset;

*Megre Data by Variable;

data PR.Merge;
merge NH.DEMO_I NH.DIQ_I; 
by SEQN;
run;

*Check contents of Dataset;

proc contents data = PR.Merge;
run;

**Step Optional: Create Categorical Variables based on Conditions;

*Use Coniditons to Create New Variabe 1;

data PR.ifthen;
set PR.merge;
If DIQ010 = 1 then DMStat = 1; *1 = Diagnosed Diabetes;
Else If LBXGH = . then DMStat = 7; *7 Unknown;
run;

*Use Coniditons to Create New Variabe Varible 2;

data PR.ifthen2;
set PR.ifthen;
If RIDAGEYR > 40 and RIDAGEYR < 70 and BMXBMI > 25 then DMRisk = 1; *At risk;
Else DMRisk = 2; *Not at risk;
run;

*Get frequency of Unique Values in tables;

proc freq data = PD.ifthen;
tables DMStat DMRisk;
run;


**Step 3: Set formats and labels;

*Set formats;

proc format;                                                                                       
value Race
	1 = Mexican American
	2 = Other Hispanic
	3 = NonHispanic White
	4 = NonHispanic Black
	6 = NonHispanic Asian
	7 = Other Race Including Multi Racial;
run;

*Set lables;

data PR.ready;
set PR.merge;
format RIDRETH3 Race.;
label RIDRETH3 = "Race and Ethnicity";
run;

*Check contents of Dataset;

proc contents data = PR.ready;
run;

**Step 4: Set Weights and Clusters to create population counts;

*Sort Data by strata and cluster;

proc sort data = PR.ready;
by SDMVSTRA SDMVPSU;
run;

*Population count Using SAS, Show results as Table in SAS;

title "Population Counts in NHANES 2015-2016";
proc surveyfreq data = PR.Ready NOSUMMARY varheader = label;
tables  RIDRETH3; *variables to use in table;
strata  SDMVSTRA; *first stage strata;
cluster SDMVPSU; *first stage cluster;
weight  WTMEC2YR; *survey weight;
run;

*Population count Using SAS, Save Results to SAS Dataset;

proc surveyfreq data = PR.Ready NOSUMMARY;
tables  RIDAGYR * RIDRETH3; *variables to use in table;
ods output CrossTabs = PR.Result;
strata  SDMVSTRA; *first stage strata;
cluster SDMVPSU; *first stage cluster;
weight  WTMEC2YR; *survey weight;
run;

*Population count Using SUDAAN;

PROC descript data = PD.stat design = wr;
subpopn RIDAGEYR >= 40 and RIDAGEYR <= 70 and BMXBMI >= 25;   
nest  SDVMSTRA SDVMPSU;                                     
weight WTMEC2YR;                                                                     
var DMStat;
table
run;

**Step Extra: Export Data;

*Export SAS Dataset to CSV;

proc export data = PR.Result dbms = csv
outfile = "E:Project\nhanes_population_raw.csv"
replace;
run;


