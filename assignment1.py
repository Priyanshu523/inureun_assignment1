#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#comma-separated sequence on a single line.
lower_range=2000
upper_range=3200
for i in range(lower_range,upper_range):
    if i%7==0 and i%5!=0:
        print(i,end=",")
    else:
        pass


# In[19]:


#Write a Python program to accept the user's first and last name and then getting them printed in
#the the reverse order with a space between first name and last name.

first_name=str(input())
last_name=str(input())
first_name=str(first_name)[::-1]
last_name=str(last_name)[::-1]
print(first_name,last_name)


# In[1]:


#Write a Python program to find the volume of a sphere with diameter 12 cm.
n=12
v=(4/3)*(22/7)*n**3
print(v)


# In[2]:


#task2
#Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list.
values=input().split(",")
print(values)


# In[3]:


#Create the below pattern using nested for loop in Python.
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print() 
for i in range(5):
    for j in range(4-i):
        print("*",end=" ")
    print()     


# In[3]:


#Write a Python program to reverse a word after accepting the input from the user.
#Sample Output:
#Input word: AcadGild
#Output: dilGdacA
s=input()
s=s[::-1]
strlst = list(s)
strlst[1], strlst[2] = strlst[2], strlst[1]
"".join(strlst)


# In[17]:


#Write a Python Program to print the given string in the format specified in the sample output.
#WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
#SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
#its citizens
n="WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"
p=n[:24]
q=n[25:87]
s=n[88:128]
t=n[128:148]
print(p)
print("       "+q+"!")
print("                  "+s)
print("                    "+t)


# In[ ]:





# In[ ]:




