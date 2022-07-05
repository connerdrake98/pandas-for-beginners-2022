import pandas as pd
# pd is the agreed alias for pandas, so loading pandas as pd is assumed standard practice


# Data Frame - Two-dimensional data
df1 = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print("-----DATA FRAME-----")
print(df1)
# see file: "table_representation" to see a table representation of this data.

# Series - One-Dimensional data. Result of selecting one column of a data frame
ages = df1["Age"]
print("-----SERIES SELECTED FROM DATA FRAME-----")
print(ages)
# series representation:
# 0    22
# 1    35
# 2    58
# Name: Age, dtype: int64

# You can also create a series from scratch:
treeHeights = pd.Series([20, 36, 54, 71, 42], name = "Tree Heights")
print("-----SERIES-----")
print(treeHeights)

# get max value of something
print("-----MAX AGE-----:")
print(df1["Age"].max()) # prints 58
print("-----MAX TREE HEIGHT-----")
print(treeHeights.max()) # prints 71

print("-----STATS: DF->AGES-----")
print(df1.describe()) # prints some stats about the ages series in df. It by default does not take into account the textual data, so it ignores the other columns.

print("--------STATS: TREE HEIGHTS--------")
print(treeHeights.describe()) # prints some stats about treeHeights

# read_ methods are used to read data to pandas data structures
csv_test_df = pd.read_csv("csv-test.csv")
txt_test_df = pd.read_csv("txt-test.txt.csv")
# display the data structures
print("-----CSV TEST DATA FRAME FROM FILE-----")
print(csv_test_df);# reading data into a data frame
print("-----TXT TEST DATA FRAME FROM FILE-----")
print(txt_test_df)

print("-----TEST PRINT HEAD 3 OF CSV-----")
print(csv_test_df.head(3)) # prints first 3 rows
print("-----TEST PRINT TAIL 3 OF TXT-----")
print(txt_test_df.tail(3)) # prints last 3 rows
# note: always uses data types int64, float64, and sttring (object)

# to_ methods are used to store data.
df1.to_csv("df1.csv", index=False)
# DO NOT USE THE TO_EXCEL FUNCTION. This function is no longer supported.
# index = False does not save the indices into the file

# Reading written csv file
df1_csv_read = pd.read_csv("df1.csv")
print("-----READING WRITTEN CSV FILE TEST-----")
print(df1_csv_read.head(3))
print(pd.read_csv("df1.csv").head()) # this works too, but is inefficient for multiple calls because pandas has to keep re-running the read function. Only efficient for ONE-TIME reads.