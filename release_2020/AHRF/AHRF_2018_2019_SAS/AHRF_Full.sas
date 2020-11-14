libname HRSA "C:\Users\drewc\GitHub\allocativ\hnb\HRSA\AHRF\AHRF_2018_2019_SAS";


PROC EXPORT 
DATA = HRSA.Ahrf2019 
OUTFILE = 'C:\Users\drewc\GitHub\allocativ\hnb\HRSA\AHRF\AHRF_2018_2019_SAS\AHRF_full.xlsx'
DBMS = XLSX
LABEL
REPLACE;
RUN;

