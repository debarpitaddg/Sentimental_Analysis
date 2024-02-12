from web_scraping import d
import pandas as pd
import numpy as np
title=[]
for key in d.keys():
    title.append(key)
a1=d[title[0]]
a2=d[title[1]]
a3=d[title[2]]
a4=d[title[3]]
a5=d[title[4]]
a6=d[title[5]]
a7=d[title[6]]
a8=d[title[7]]
a9=d[title[8]]
a10=d[title[9]]
a11=d[title[10]]
a12=d[title[11]]
a13=d[title[12]]
a14=d[title[13]]
a15=d[title[14]]

# Create DataFrame from multiple lists
df = pd.DataFrame(list(zip(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15)), columns=title)

#convert into excel
df.to_excel("output.xlsx",index=False)
print("Dictionary converted into excel...")
