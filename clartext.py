import numpy as np
# Text file data converted to string numpy array and after that into normal list alltogether
File_data1 = list(np.loadtxt("StopWords_Auditor.txt" , dtype='str'))
File_data2=list(np.loadtxt("StopWords_Currencies.txt" , usecols=0,dtype='str'))
File_data3=list(np.loadtxt("StopWords_DatesandNumbers.txt" ,usecols=0, dtype='str'))
File_data4=list(np.loadtxt("StopWords_Generic.txt" ,usecols=0, dtype='str'))
File_data5=list(np.loadtxt("StopWords_GenericLong.txt" , usecols=0,dtype='str'))
File_data6=list(np.loadtxt("StopWords_Geographic.txt" ,usecols=0,dtype='str'))
File_data7=list(np.loadtxt("StopWords_Names.txt" ,usecols=0, dtype='str'))
stopwords=File_data1+File_data2+File_data3+File_data4+File_data5+File_data6+File_data7
negative=list(np.loadtxt("negative-words.txt",dtype='str'))
positive=list(np.loadtxt("positive-words.txt",dtype='str'))
