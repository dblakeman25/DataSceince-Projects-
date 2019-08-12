#!/usr/bin/env python
# coding: utf-8

# # App Profile Recommendation for Google Play and App Store 

# The aim of this project is to find out what apps are most profitable for Google Play and the App Store. 
# 
# This pseudo company only builds apps that are free to download and install, and the main source of revenue comes from in-app ads. This means that revenue is greatly influenced by the number of users. 
# 
# The goal is to analyze the data, help the team of developers understand what apps attract more users and make data-driven decisions.
# 
# Documentation for datas source:
# https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps/home

# In[35]:


from csv import reader
#The IOS App Store dataset
open_file_Apple = open('AppleStore.csv')
read_file_Apple = reader(open_file_Apple)
ios = list(read_file_Apple)

#The Android Google Store dataset
open_file_Google = open('googleplaystore.csv')
read_file_Google = reader(open_file_Google)
android = list(read_file_Google)


# In[36]:


#Column Headers
ios_header = ios[0]
android_header = android[0]
# Row of IOS and Android without the header row.
ios = ios[1:]
android = android[1:]

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        
explore_data(ios,0,3,True)
explore_data(android,0,3,True)

# iOS_Dataset:
# ---------------
# Number of Rows = 7196
# Number of Columns 16
# ______________________

# Android_Dataset:
# ----------------
# Number of Rows = 10841
# Number of Columns = 13


# In[37]:


# Print headers of columns. 
print(ios_header)
print(android_header)

# Columns that could help us with our analysis:

#For iOS - 'track_name', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user rating', and 'prime_genre'
#For Android = 'App', Category','Rating', 'Reviews', 'Installs','Price','Genre'


# # Data Cleaning
#    _______________________

# In[38]:


# There is an issue with one of the rows not having the right amount of information. 
#This row needs to be deleted.
#To determine the proble row:

print(len(android_header))
for row in android:
    header_length = len(android_header)
    row_length = len(row)
    if row_length != header_length:
        print(row)
        print(android.index(row))


print(android[0])  
print('\n')
print(android[10472])
print('\n')
print(android[10473])
# Comparing the header to row 10472(determined from above code not having the right length of row data),
#and row 10473 (has the right amount of row data)
# Row 10472 has to be deleted 

#del andriod[10472] # Don't run this more than once   
# Row 10472 has been deleted 


# In[49]:


print(len(android))
# The number of rows for Android has gone from 10842 tro 1041 rows.
for row in ios:
    iheader_length = len(ios_header)
    irow_length = len(row)
    if irow_length != iheader_length:
        print(ios.index(row))
        
# Checked the number of row data in comparison to the column header. All rows have the correct number of row dataset.

        



# In[40]:


# The Google Play dataset has a few duplicate enteries.
# An example of a duplicate entry is:

for app in android:
    name = app[0]
    if name == 'Facebook':
        print(app)
        
# Facebook has two enteries which means it has a duplicate entry.

#Another duplicate entry:

for app in android:
    name = app[0]
    if name == 'Google Ads':
        print(app)
#Google Ads has three entries.

# To find the number of apps with duplicate entries:

unique_entry = []
duplicate_entry = []

for app in android:
    name = app[0]
    if name in unique_entry:
        duplicate_entry.append(name)
    else:
        unique_entry.append(name)
        
print('Number of duplicate apps enteries are:' ,len(duplicate_entry))
# There are 1181 duplicate apps enteries
print('/n')
print('Some apps with duplicate enteries are: ', duplicate_entry[:10])

#Some apps with duplicate enteries are:  
#['Quick PDF Scanner + OCR FREE', 'Box', 'Google My Business', 'ZOOM Cloud Meetings', 'join.me - Simple Meetings', 'Box', 'Zenefits', 'Google Ads', 'Google My Business', 'Slack']



# In[48]:


# We do not want multiple enteries for each app. To determine which entry for each app to keep
# We have to choose the entry that has the higher number of revie
#For example, Facebook has two enteries:
# Entry1 - ['Facebook', 'SOCIAL', '4.1', '78158306', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'August 3, 2018', 'Varies with device', 'Varies with device']
# Entry2 - ['Facebook', 'SOCIAL', '4.1', '78128208', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'August 3, 2018', 'Varies with device', 'Varies with device']

# Column 4 in the header represents the number of reviews:
print(android_header)
#['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']
#So we would be keeping 'Entry1' because it has more reviews.



# In[ ]:




