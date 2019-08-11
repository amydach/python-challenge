#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


os.path.join("Resources","budget_data.csv")


# In[3]:


#pybudget = os.path.join("Resources","budget_data.csv")
csvpath = os.path.join("Resources","budget_data.csv")


# In[5]:


with open(csvpath, 'r') as file_handler:
     lines = file_handler.read()
     #print(lines)
#     print(type(lines))
#     print(file_handler)


# In[6]:


Total_Months=0
Total = 0
Avg_Change = 0
PL_Total = 0
float_Profits_Losses = 0

with open(csvpath,"r") as csvfile:
   csvreader=csv.reader(csvfile,delimiter=",")
   header=next(csvreader)
   #columns=len(csvreader[0])
   Date_index=header.index("Date")
   for row in csvreader:
       float_Profits_Losses= float(row[1])
       PL_Total += float_Profits_Losses
       Total += float_Profits_Losses
       Total_Months += 1
       #Avg_Change = float_Profits_Losses-(PL_Total-float_Profits_Losses)
   print("Financial Analysis")
   print("----------------------------")
   print("Total Months:" + " " + str(Total_Months))
   print("Total :" + " $" + str(Total))
   #print("Average Change :" + " $" + str(Avg_Change))    


# In[7]:


PL_Total = 0
Sum_Change = 0
Avg_Change = 0
#float_Profits_Losses = 0



with open(csvpath,"r") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   header=next(csvreader)
   Date_index=header.index("Date")
   for row in csvreader:
       budget_date=row[0]
       float_Profits_Losses= float(row[1])
       PL_Total += float_Profits_Losses
       #Sum_Change = PL_Total-float_Profits_Losses
       #Avg_Change = float_Profits_Losses-(PL_Total-float_Profits_Losses)
       #print(budget_date, float_Profits_Losses, PL_Total)

