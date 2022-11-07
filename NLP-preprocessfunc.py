#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
# regEX function which clean sentences from symbols and trim it.
def preprocess(text):
    text = re.sub(r'[^\w\s\']',' ', text)
    text = re.sub(' +', ' ', text)
    return text.strip().lower()

