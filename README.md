# pandas-for-beginners-2022

Some Pandas beginner tutorials and Pandas documentation is out of date with new versions. This 2022 Pandas beginner tutorial code is meant to show how to work with simple data structures and read/write with spreadsheet files.

To use Pandas, make sure Python3 is installed with python3 --version. Refer to Python.org for any issues with installing Python3 and for instructions.

Install Pandas with the installation tutorial on the Pandas.pydata.org website: https://pandas.pydata.org/docs/getting_started/install.html

Create a new folder with a file.py file in your favorite code editor. If you don't have one, VS Code is recommended. VS Code has a Python extension by Microsoft that helps with writing Python code and comes with features like Intellisense.

Make sure to include the line "import pandas as pd" at the top of your main python file. This lists Pandas as a dependency to trigger errors if Pandas is not installed before trying to run Pandas functions and also lists "pd" as the keyword for designating functions as coming from the Pandas library.

Example:
pd.read_csv() - pd is short for Pandas and the interpreter looks for the read_csv() function in the Pandas library.

NOTE: Pandas documentation on their website can be out-of-date with the most recent versions. One important note is that Pandas cannot read .xlsx files, only csv files, so the read_xlsx() and to_xlsx() functions DO NOT WORK. Only read_csv() and to_csv() are supported for security reasons.

Read through the main.py file in this repository to get an understanding of the very basics of Pandas, including Pandas data structures data frames and series and reading from and writing to spreadsheet files.
