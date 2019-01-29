#! usr/bin/env/python3

# OG Filename: create_monthly_folders.py 
# Function: creates one folder for each month in the given directory
# Format: YYYY-MM_Month | 2019-01_January

import os, calendar

os.chdir('/Users/IMac/Documents/PYR_Admin/Online_Campaigns') # target directory for folders

target_year = '2019'
# calendar.month_name - array with months of year;  [0] = ''
# calendar.month_abbr - abbreviated months of year; [0] = ''

for m in range(1, 13):

    print(calendar.month_name[m])
    print(calendar.month_abbr[m])

    # dir_name = f'{target_year}-{m_num}_{m_str}'
