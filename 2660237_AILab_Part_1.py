#!/usr/bin/env python
# coding: utf-8

# # Week 1: Intro to Python, Anaconda & Jupyter Notebook
# 
# Excercise to familiarise myself with Jupyter Notebook and its relationship to Python.
# 
# a) I chose this course to familiarise myself with new coding languages and learn to navigate new software. I'm hoping that studying AI and engaging in practical work will help me to created informed opinions about AI advancements and apply knowledge to other areas of passion such as web design, digitised art and communications. 
# 
# b)I have limited exposure to AI as an academic subject or using a language like Python. Although I'm practically unfamiliar with this topic, I have a personal interest in the function of neural networks and knowledge based systems impact beyond digital environments. 
# 
# c)My expectations for this course are:
# - to learn basic python
# - to adequately navigate anaconda and Jupyter notebook
# - to understand the function of practical work within real life scenarios 
# - to link ideas about AI to other areas of information studies this year
# - to read more about the positive and negative developments/impacts of AI

# In[2]:


message = "Hello, World!"

print (message)


# In[9]:


message = "How are you? "

print (message + message*3)


# In[12]:


message = "Hello there!"

print (message[4])


# In[1]:


from IPython.display import * 


# In[2]:


YouTubeVideo("BrWOEofKfZs")


# In[ ]:


import webbrowser
import requests

#this is printing
print("Shall we hunt down an old website?")
site = input("Type a website URL: ")
era = input("Type year, month, and date, e.g., 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser.")
    webbrowser.open(old_site)
except:
    print("Sorry, could not find the site.")

