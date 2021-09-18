#!/usr/bin/env python
# coding: utf-8

# ### Write a Python function to sum all the numbers in a list.
# 
# 
# #### Sample List : (8, 2, 3, 0, 7)
# 
# #### Expected Output : 20
# 
# 
# Explanation:
# 
# Summation should like 8+2+3+0+7 = 20

# In[1]:


def funlist (Listofno):

    Sumofno = 0


    for num in Listofno:
        Sumofno = Sumofno + num
    return Sumofno


# In[2]:


funlist([10,20,36,54])


# In[9]:


def funlist1 (Listofno1):
    return sum(Listofno1)


# In[10]:


funlist1([10,20,36,54])


# ### Write a Python program to reverse a string.
# 
# 
# #### Sample String : "1234abcd"
# 
# #### Expected Output : "dcba4321"

# In[4]:


def funString(Samplestring):
    print(Samplestring[::-1])


# In[5]:


funString("1234abcd")


# In[6]:


funString("Salil is of age 26.")


# ### Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# 
# 
# #### Sample String : 'The quick Brow Fox'
# 
# #### Expected Output :
# 
# No. of Upper case characters : 3
# 
# No. of Lower case Characters : 12

# In[7]:


def funstring(SampleString):
    countupper = 0
    countlower = 0
    for char in SampleString:
        if char.isalpha():
            if char.isupper():
                countupper = countupper+1
            else:
                countlower = countlower+1
    print("The number of upper case:",countupper) 
    print("The number of lower case:",countlower)


# In[8]:


funstring("Hi I am Salil Banerjee")


# In[ ]:




