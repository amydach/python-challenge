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


# In[4]:


with open(csvpath, 'r') as file_handler:
     lines = file_handler.read()
     #print(lines)
#     print(type(lines))
#     print(file_handler)


# In[5]:


previous_profit=0
Total_Month = 0
Total = 0
monthly_changes=[]
total_months=[]


with open(csvpath,"r") as csvfile:
   csvreader=csv.reader(csvfile,delimiter=",")
   header=next(csvreader)
   #columns=len(csvreader[0])
   Date_index=header.index("Date")
   for row in csvreader:
       float_Profits_Losses= float(row[1])
       Total += float_Profits_Losses
       Total_Month += 1
       total_months.append(row[0])
       current_profit= float(row[1])
       monthly_change=current_profit - previous_profit
       monthly_changes.append(monthly_change)
       previous_profit=current_profit
   monthly_changes = monthly_changes[1:]
   #average=sum(monthly_changes)/(total_months - 1)
   increase=max(monthly_changes)
   decrease=min(monthly_changes)
   dateincrease=monthly_changes.index(increase)
   datedecrease=monthly_changes.index(decrease)
   
       
   print("Financial Analysis")
   print("----------------------------")
   print("Total Months:" + " " + str(Total_Month))
   print("Average Change: ")# + "$" + str(average))
   print("Greatest Increase: " + str(total_months[dateincrease + 1]) + " $" + str(increase))
   print("Greatest Decrease: " + str(total_months[datedecrease + 1]) + " $" + str(decrease)) 

