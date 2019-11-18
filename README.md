# Python_Data_Pre_Processing

Data Pre-processing in Python
S.No	Column Name:	Issues Found
1.	Age	: Negative values (619) and zeros – 2669 records
2.	Workclass and Occupation:
    i)	Categories names are mismatching with the default values. E.g. special characters, spaces are added, no spaces within two words
    ii)	Missing values with character ?
3.	Fnlwgt:	minimum value : 13769, max value : 1484705
4.	Education-num:	Is wrongly mapped for some records 
5.	Capital Gain	Has only value 0. This column can be dropped
6.	Captial Loss	28736 records have 0 value.
