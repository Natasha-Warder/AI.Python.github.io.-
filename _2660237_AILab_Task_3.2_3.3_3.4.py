#!/usr/bin/env python
# coding: utf-8

# ## Task 3.2 

# In[16]:


from matplotlib import pyplot 
test_picture = pyplot.imread("picture1.jpg")
print("Numpy array of the image is: ", test_picture)
pyplot.imshow(test_picture)


# In[17]:


from matplotlib import pyplot 
test_picture = pyplot.imread("picture1.jpg")
print("Numpy array of the image is: ", test_picture)
test_picture_filtered = 2*test_picture/3
pyplot.imshow(test_picture_filtered)


# ##  Task 3.3

# In[9]:


from sklearn import datasets


# In[10]:


dir(datasets)


# In[12]:


iris_data = datasets.load_iris()


# In[13]:


iris_data.DESCR


# In[14]:


print (iris_data.DESCR)


# In[16]:


iris_data.feature_names


# In[17]:


iris_data.target_names


# In[18]:


iris_data.keys()


# ##  Task 3.4

# In[21]:


from sklearn import datasets
import pandas

iris_data = datasets.load_iris()

iris_dataframe = pandas.DataFrame(data=iris_data['data'], columns = iris_data['feature_names'])


# In[22]:


iris_dataframe.head()


# In[24]:


iris_dataframe.describe()


#  ## Bias and Datasets
# 
# 
# test data used to train the AI algorithm are taken from data created by humans, therefore human bias is transferred to the AI system because this is the 'real-life' data used to train itself.
# 
# It is important to make sure sensitive data features like:gender, ethnicity (etc) and their correlations are addressed.
# 
# It is important to make sure appropriate data-labeling methods are used.
# 

# In[ ]:




