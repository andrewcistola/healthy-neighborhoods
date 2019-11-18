

Task 2a: How to Generate Population Counts in SUDAAN

In this example, you will use SUDAAN to combine age subgroups and generate population estimates for high blood pressure (HBP) by sex and race/ethnicity for persons 20 years and older.  The method outlined in this module uses a SAS data file with CPS population totals. The process for combining subgroups and calculating population estimates is then automated using the code outlined below. 

Alternatively, you can use the CPS population totals located on the respective survey cycle NHANES web page (referred to in Key Concepts), plus the results from a proc descript or proc crosstab procedure and manually calculate population estimates within a spreadsheet.  If you choose this option, you will need to define the age, race/ethnicity and gender subgroups of interest and calculate population totals within the spreadsheet on your own.

 
Step 1: Calculate Prevalence of the Health Condition of Interest

The proc descript procedure in SUDAAN and additional SAS code will be used to generate population estimates using the 3-step process outlined below. 

In Step 1 of this method you will calculate the prevalence of the health condition of interest (i.e., HBP) by each sub-domain of interest (i.e., sex and race/ethnicity) using the  proc descript procedure.  You will need to use appropriate weights, especially when combining across survey cycles.

 

The health outcome must be coded as a dichotomous variable (0, 100) for absence (0) or presence (100) of the health condition of interest. (HBPX).

 

hbpx= . ;

if hbp= 1 then hbpx= 100 ;

e lse if hbp= 2 then hbpx= 0 ;

 

Similar to the proc descript procedure used in Task 1, you will output the results to a SAS data file using the output statement, as shown below.  Population estimates will not be age- standardized so that they reflect the true population sampled.

 
Info iconIMPORTANT NOTE

ese programs use variable formats listed in the Tutorial Formats page. You may need to format the variables in your dataset the same way to reproduce results presented in the tutorial.

 
SUDAAN Procedure for Generating Prevalence Rates Statements 	Explanation
proc sort data=analysis_data ;

 by sdmvstra sdmvpsu;

run ;
	

Use the proc sort procedure to sort the dataset by strata (sdmvstra) and PSU (sdmvpsu).

PROC descript data=analysis_data design=wr noprint mean

atlevel1=1 atlevel2= 2 ;
	

Use proc descript to generate means and specify the sample design using the design option WR (with replacement).
subpopn ridageyr >=20 ;  	

Use the subpopn statement to select sample persons 20 years and older (ridageyr >=20) because only those individuals are of interest in this example.

Note: For accurate estimates, it is preferable to use the subpopn statement in SUDAAN to select a subpopulation for analysis, rather than to select the study population in the SAS program while preparing the data file. 
NEST  sdmvstra sdmvpsu;  	

Use the nest statement with strata (sdmvstra) and PSU (sdmvpsu) to account for the design effects.
WEIGHT wtmec4yr; 	

Use the weight statement to account for the unequal probability of sampling and non-response.  In this example, the MEC weight for 4 years of data (wtmec4yr) is used.
subgroup  riagendr age race ; 	

Use the subgroup statement to list the categorical variables for which estimates are requested.  These names will also appear in the table statement below. In this example, gender (riagendr), age (age), and race-ethnicity (race) are of interest.
levels   2 3 4; 	

Use the levels statement to define the number of categories in each of the subgroup variables. The level must be an integer greater than 0. This example has two genders, three age groups, and four race-ethnicity groups.
var hbpx ; 	

Use the var statement to name the variable(s) to be analyzed. In this example, the high blood pressure variable (hbpx) is used.
table riagendr * race ; 	

Use the table statement to specify cross-tabulations for which estimates are requested. If a table statement is not present, a one-dimensional distribution is generated for each variable in the subgroup statement. In this example, the estimates are for gender (riagendr) by race-ethnicity (race).

OUTPUT    NSUM MEAN SEMEAN   atlev2 atlev1 /

FILENAME=nh9902 FILETYPE=SAS REPLACE;

run ;
	

Use an output statement to output the number of observations (nsum), mean (mean), standard error of the mean (semean), number of strata (atlev1), and number of PSUs (atlev2) to a SAS file named nh9902.

 

These data will be fed into a SAS program where degrees of freedom, t-statistics, and 95% confidence limits will be calculated for each prevalence estimate, as shown below. Values also will be labeled and formatted.

 
Calculate Degrees of Freedom, T-statistic, and Confidence Intervals from SAS Output Dataset Statements 	Explanation

DATA nh9902c; SET nh9902;

df=atlev2-atlev1;
	

Use the data statement to create a new dataset (nH9902c) from the SAS dataset created in Step 1 above (nh9902).

Calculate the degrees of freedom (df) by subtracting the  number of strata (atlev1) from the number of PSU (atlev2).

tcritl=tinv( .025 ,df);

tcritu=tinv(.975 ,df);
	

Use these statements to calculate the t-statistics (tcritl and tcritu) based on the calculated degrees of freedom (df).

ll=round((mean+tcritl*semean),.01 );

ul=round((mean+tcritu*semean),.01 );
	

Use these statements to calculate the lower limit (ll), and upper limit (ul) for the Wald 95% confidence intervals.

percent=round(mean,.01 );

sepercent=round(semean,.01 );

run ;
	

Use these statements to round the estimates and rename them to percent and sepercent.

 
Step 2: Combine CPS Population Totals

In this step, you will combine appropriate CPS population totals across survey cycles AND across years of age to reflect the subpopulation of interest (i.e., those 20 and older by sex and race). 

 

In this module, CPS population totals are supplied as a SAS dataset with values for: age (CTUTAGE) ranging from 0 to 85+ years ; gender (CTUTGNDR); race/ethnicity (CTUTRACE), where 1= non-Hispanic white, 2=non-Hispanic black, 3=Mexican American and 4=other; race/ethnicity (CTUTRETH), where 1=Mexican American, 2=non-Hispanic other, 3=non-Hispanic white, 4=non-Hispanic black, 5=other Hispanic;  ethnicity (CTUTHISP) where 1=Hispanic and 2=non-Hispanic; survey cycle (CTUTSRVY); and the population total (CTUTPOPT).  Appropriate age, race/ethnicity, and gender groups were created in a previous step. 

 

The proc descript procedure in SUDAAN will be used to calculate CPS population totals for the sub-domains of interest (i.e., sex and race/ethnicity) for the subpopulation of interest (age 20 and older).  In this case, no sample design factors or weights need to be used.  The design specified is SRS (simple random sampling).   The variable is CTUTPOPT (the population totals).  Subgroup totals are output to another SAS data set (pt9902) for use in the next step.  Nothing is printed.

 
SUDAAN Procedure to Calculate CPS Population Totals Statements 	Explanation
PROC descript data= nh.cpstot9902 design=srs noprint means; 	

Use proc descript to generate means and specify the sample design using the design option SRS (simple random sample). Use the SAS-supplied dataset (cpstot9902) to read the CPS population totals.
SUBPOPN ctutage >= 20 ; 

 
	

Use the subpopn statement to select sample persons 20 years and older (ctutage>=20) because only those individuals are of interest in this example.

Note: For accurate estimates, it is preferable to use the subpopn statement in SUDAAN to select a subpopulation for analysis, rather than to select the study population in the SAS program while preparing the data file. 
SUBGROUP ctutgndr ctutrace ;   	

Use the subgroup statement to list the categorical variables for which estimates are requested.  These names will also appear in the table statement below. In this example, gender (ctutgndr) and race-ethnicity (ctutrace) are of interest.
LEVELS 2 4 ;  	

Use the levels statement to define the number of categories in each of the subgroup variables. The level must be an integer greater than 0. This example has two genders and four race-ethnicity groups.
VAR ctutpopt; 	

Use the var statement to name the variable(s) to be analyzed. In this example, the population total variable (ctutpopt) is used.
TABLES ctutgndr*ctutrace ; 	

Use the table statement to specify cross-tabulations for which estimates are requested. If a table statement is not present, a one-dimensional distribution is generated for each variable on the subgroup statement. In this example, the estimates are for gender (ctutgndr) by race-ethnicity (ctutrace).
OUTPUT total / FILENAME=pt9902 FILETYPE=SAS REPLACE;

Run ;
	

Use an output statement to output the total number of observations to a SAS file named pt9902.

 
Step 3: Multiply Prevalence Estimates with CPS Population Totals

In this last step, you will multiply prevalence estimates with corresponding CPS population totals to estimate the total number of non-institutionalized U.S. citizens affected with HBP.

 

Note that the datasets produced in Step 1 and Step 2 will be sorted on the sub-domain variables and merged.  The new dataset will be used in the final SAS program.  Percent prevalence estimates as well as lower and upper 95% confidence limits will be multiplied to the corresponding population total for that subgroup.  Results will be rounded, formatted, and printed in SAS.
Calculate Population Estimates from SAS Output Dataset Statements 	Explanation
proc sort data =nh9902c; by riagendr race; run ; 

proc sort data =pt9902(rename=(ctutgndr=riagendr ctutrace=race));
by riagendr race;
run ;
	

Use the proc sort procedure to sort the two datasets by sex and race. In the second dataset, rename the CPS total race and gender (ctutrace and ctutgndr) variables to match the variable names used in the original dataset.

data comb;

merge nh9902c( in =a) pt9902 ;

by riagendr race ;

if a ;
	

Use the data statement to create a new dataset (comb) by merging the SAS datasets created previously (nh9902c and pt9902).

 

popmean=(percent/100 )*total ;

popl=ll/100 *total ;

popu=ul/100 *total  ;
	

Use these statements to calculate the population counts by applying the population totals (total) to the prevalence estimate (percent) and the 95% confidence interval limits.

poplr=round(popl,1000 );

popur=round(popu,1000 );

popmeanr=round(popmean,1000 );

totalr=round(total,1000 ) ;
	

Use these statements to round and format the estimates to the nearest thousand.

proc print noobs split = '/' double ;

var   riagendr race percent sepercent  ll ul df nsum

totalr popmeanr poplr popur ;

format race racefmt.   riagendr sexfmt.   nsum 5.0 percent 5.2 sepercent 5.2

ll 4.2 ul 4.2   df 2.0 ;

label   

percent='%' / 'with' / 'high' / 'bp'

nsum='Num' / 'bp' / 'status'

sepercent='Std' / 'error'

ll='Lower' / '95 %' / 'Wald' / 'CI'

ul='Upper' / '95 %' / 'Wald' / 'CI'

df='degrees' / 'of' / 'freedom'

popmeanr='Pop' / 'Est' / 'US' / 'with' / 'high' / 'bp'

totalr='Pop' / 'total' / 'US'

poplr='Pop Est' / 'Lower' / '95 %' / 'WALD' / 'CI'

popur='Pop Est' / 'Upper' / '95 %' / 'WALD' / 'CI' ;

title1 'Prevalence of persons with high Bp - US, 1999-2002' ;

title2 'Percent and population estimates of number with high Bp-Wald CI' ;

run ;
	

Use the proc print procedure to print the variables of interest.

Highlights from the output include:

    Nearly 58 million non-institutionalized U.S. adults have high blood pressure, with approximately 26 million adult men and 32 million adult women affected.
    The number of non-institutionalized U.S. adults with hypertension, by race/ethnicity, is as follows: approximately 42.7 million non-Hispanic whites, 8.1 million non-Hispanic Blacks, and 2.4 million Mexican-Americans. 

 

close window icon Close Window
