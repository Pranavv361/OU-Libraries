# Open Access Designations Analysis

## Overview
This Python script analyzes open access designations in a dataset of journal articles stored in an Excel file. It counts the number of articles with different open access designations and creates separate spreadsheets for each designation in a new Excel file.

## Usage
1. Clone this repository: `git clone https://github.com/Pranavv361/Open-Access-Analysis.git`
2. Install the necessary dependencies: `pip install pandas openpyxl xlrd xlwt xlsxwriter`
3. Place your Excel file containing journal article data in the same directory as the script. Ensure that the file name matches the one specified in the script (`savedrecs.xls`).
4. Run the Python script: `python open_access_analysis.py`
5. After execution, you will find a new Excel file named `New_File.xlsx` in the same directory, containing separate spreadsheets for each open access designation.

## Description
This script first reads the Excel file containing journal article data and selects only the necessary columns for analysis. It then counts the number of articles with each open access designation and stores them in separate sublists. These sublists are used to create separate spreadsheets for each open access designation in a new Excel file using the pandas library.

## Requirements
- Python 3.x
- Pandas
- Openpyxl
- Xlrd
- Xlwt
- Xlsxwriter

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
