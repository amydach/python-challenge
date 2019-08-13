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


candidates_votes=[]
with open(csvpath, 'r') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    header = next(csvreader)
    #print(f" CSV Header: {csv_header}")
    Voter_index=header.index("Voter ID")
    Candidate_index=header.index("Candidate")
    for row in csvreader:
        #Voter=row[Voter_index]
        candidates_votes.append(row[Candidate_index])
        #row_count=sum(1 for row in csvreader)+1
        #print("```text")
        #print("Election Results")
        #print("----------------------------")
        #print("Total Votes:" + " " + str(row_count))


# In[6]:


candidate_list=list(set(candidates_votes))
candidate_list


# In[7]:


#Percentage of votes each candidate won
total_votes=len(candidates_votes)
total_votes


# In[8]:


votes_per_candidate=[]
for candidate in candidate_list:
    votes_per_candidate.append(candidates_votes.count(candidate))
    votes_per_candidate

percentages=[round(100*vote/total_votes,4) for vote in votes_per_candidate]
percentages


# In[9]:


#print("```text")
#print("Election Results")
#print("----------------------------")
#print("Total Votes:" + " " + str(total_votes))


# In[10]:


for i in range(0,len(candidate_list)):
    print(f"The candidate {candidate_list[i]} has {votes_per_candidate[i]} votes and {percentages[i]} %")


# In[11]:


max_votes = max(votes_per_candidate)

for row in range(0,len(candidate_list)):
    Total = max_votes
    f=open("txt","w+")
    with open('txt','w') as out:
        line1 = ("```text")
        line2 = ("Election Results")
        line3 = ("----------------------------")
        line4 = ("Total Votes: " + " " + str(total_votes))
        line5 = ("----------------------------")
        line6 = ("The candidate " + str(candidate_list[0]) + " has " + str(votes_per_candidate[0]) + " votes " + str(percentages[0])+ "%")
        line7 = ("The candidate " + str(candidate_list[1]) + " has " + str(votes_per_candidate[1]) + " votes " + str(percentages[1])+ "%")
        line8 = ("The candidate " + str(candidate_list[2]) + " has " + str(votes_per_candidate[2]) + " votes " + str(percentages[2])+ "%")
        line9 = ("The candidate " + str(candidate_list[3]) + " has " + str(votes_per_candidate[3]) + " votes " + str(percentages[3])+ "%")
        line10 = ("----------------------------")
        line11 = ("Winner:" + " " + str(Total))
        line12 = ("----------------------------")
        line13 = ("````")
        out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13))
f.close()
# I know that candidates s/b ranked in descending order, but can't figure it out.
# I know the winner s/b Khan, but can't get the corresponding name to appear as winner.
# I can't figure out how to get the candidate list to output to the txt, so I give up.
# So, I have hard coded the row number of each candidate in the list in lines 6-9, which is not the best but provides the results.

