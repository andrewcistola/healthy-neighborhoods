#### Healthy Neighborhoods Project
### Nevile Subproject
## Readme: Options for Using the Random Forest in Variable Selection 

3.2.4.3.1 skleanr.ensemble.RandomForesClassifier

1000 trees is recommended for generating useful sample without taking too much time

weight all variables as equal

ideally allow each tree to go until pure

also set each tree to ony choose options that will improve gini coefficient

this will keep all defaults except for n_estimators in scikit learn

Ythat 2013 tutorial on Random Forests in Python

### RFE 

used linear coefficients for classifiers

why stepwise in this application is not irresponsible

end with 5 variables since this is most usable outcome

