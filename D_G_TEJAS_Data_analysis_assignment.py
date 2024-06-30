#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Create a list with elements [1, 2, 3, 4, 5]
my_list = [1, 2, 3, 4, 5]

# Append 6 to the list
my_list.append(6)

# Remove the element 3 from the list
my_list.remove(3)

# Set the element at index 0 to 10
my_list[0] = 10

# Print the list
print("updated list:" ,my_list)


# In[12]:


# Create a dictionary with initial key-value pairs
my_dict = {'name': 'Tejas', 'age': 25, 'city': 'Delhi'}

# Add a new key-value pair (6, 'f')
my_dict['Gender'] = 'Male'

# Remove the key-value pair with key 3
del my_dict['age']

# Change the value of the key 1 to 'z'
my_dict['city'] = 'Mumbai'

# Print the dictionary
print("updated_dict:",my_dict)


# In[14]:


# Create a set with initial elements
my_set = {1, 2, 3, 4, 5}

# Add the element 6 to the set
my_set.add(6)

# Remove the element 3 from the set
my_set.remove(3)

# Remove the element 1 and add the element 10 (since sets do not support indexing)
my_set.discard(1)
my_set.add(10)

# Print the set
print("updated set:",my_set)


# In[ ]:




