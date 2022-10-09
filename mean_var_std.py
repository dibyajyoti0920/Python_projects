#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
def calculate(data):
    data_arr = np.array(data)
    data_arr_reshaped = data_arr.reshape(3,3)
    r1=data_arr_reshaped[0:1,:]
    r2=data_arr_reshaped[1:2,:]
    r3=data_arr_reshaped[2:3,:]
    c1=data_arr_reshaped[:,0:1]
    c2=data_arr_reshaped[:,1:2]
    c3=data_arr_reshaped[:,2:3]
    mean_r1 = r1.mean()
    mean_r2 = r2.mean()
    mean_r3 = r3.mean()
    mean_c1 = c1.mean()
    mean_c2 = c2.mean()
    mean_c3 = c3.mean()
    mean_f = data_arr.mean()
    var_r1 = r1.var()
    var_r2 = r2.var()
    var_r3 = r3.var()
    var_c1 = c1.var()
    var_c2 = c2.var()
    var_c3 = c3.var()
    var_f = data_arr.var()
    std_r1 = r1.std()
    std_r2 = r2.std()
    std_r3 = r3.std()
    std_c1 = c1.std()
    std_c2 = c2.std()
    std_c3 = c3.std()
    std_f = data_arr.std()
    max_r1 = r1.max()
    max_r2 = r2.max()
    max_r3 = r3.max()
    max_c1 = c1.max()
    max_c2 = c2.max()
    max_c3 = c3.max()
    max_f = data_arr.max()
    min_r1 = r1.min()
    min_r2 = r2.min()
    min_r3 = r3.min()
    min_c1 = c1.min()
    min_c2 = c2.min()
    min_c3 = c3.min()
    sum_r1 = r1.sum()
    sum_r2 = r2.sum()
    sum_r3 = r3.sum()
    sum_c1 = c1.sum()
    sum_c2 = c2.sum()
    sum_c3 = c3.sum()
    sum_f = data_arr.sum()
    min_f = data_arr.min()
    result = {'mean':[[mean_r1,mean_r2,mean_r3],[mean_c1,mean_c2,mean_c3],[mean_f]],'variance':[[var_r1,var_r2,var_r3],[var_c1,var_c2,var_c3],[var_f]],'standard deviation':[[std_r1,std_r2,std_r3],[std_c1,std_c2,std_c3],[std_f]],
             'max':[[max_r1,max_r2,max_r3],[max_c1,max_c2,max_c3],[max_f]],'min':[[min_r1,min_r2,min_r3],[min_c1,min_c2,min_c3],[min_f]],'sum':[[sum_r1,sum_r2,sum_r3],[sum_c1,sum_c2,sum_c3],[sum_f]]}
    return result
    


# In[30]:


calculate([1,2,3,4,5,6,7,8,9])


# In[ ]:




