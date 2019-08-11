#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


os.path.join("Resources","election_data.csv")


# In[3]:


csvpath = os.path.join("Resources","election_data.csv")


# In[4]:


with open(csvpath, 'r') as file_handler:
     lines = file_handler.read()
     #print(lines)
     print(type(lines))
     print(file_handler)


# In[5]:


with open(csvpath, 'r') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    header = next(csvreader)
    #print(f" CSV Header: {csv_header}")
    Voter_index=header.index("Voter ID")
    for row in csvreader:
        Voter=row[Voter_index]
        row_count=sum(1 for row in csvreader)+1
        print("```text")
        print("Election Results")
        print("----------------------------")
        print("Total Votes:" + " " + str(Voter))


# In[6]:


with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    Candidate_index=header.index("Candidate")
    for row in csvreader:
        Candidate=row[Candidate_index]
        #print(Candidate)

