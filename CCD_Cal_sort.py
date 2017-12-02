#Import all files in directory called "ICCD_X_Y.txt" and averaging files with a common X. Output one file per X.
#v0.1 11/29/17 FW
#Added ability to output wavelength also.

import os
import numpy as np
import scipy as sp
import sys


filelist = []
avg_arr = []
temp_arr = []
cur_Par = 0
WL_arr = []

cent_WL = 450					#Centre wavelength of the CCD, in nm
WL_cal = 0.103					#nm per pixel
WL_int = cent_WL - 69.57		#nm offset
CCD_size = 1340					#CCD total pixel count 
file_suff = "ICCD_"				#File suffix - change here
summ_file_base = "AVG_CCD_"		#Output file base
summ_file_ext = ".txt"			#Output file extension

#Create WL array
func1 = lambda i, j: i*WL_cal+WL_int
WL_arr = np.fromfunction(np.vectorize(func1), (CCD_size,1),  dtype=int)
WL_arr = WL_arr.flatten()

#find all files with "ICCD_" start
for file in os.listdir(os.getcwd()):
	if file.startswith(file_suff):
		filelist = np.append(filelist, str(file))
	

for idx, item in enumerate(filelist):
	
	#split file name "ICCD_a_b.txt" by "_" character. a and b are used to average multiple files. 
	#tsh is "trash" variable (i.e. not needed)
	tsh, a, b = item.split("_")
	b, tsh = b.split(".")
	a = int(a)
	b = int(b)

	
	if cur_Par == 0:				#current parent filename
		cur_Par = a 				
		data_arr = np.genfromtxt(item, delimiter = '\t', usecols=(1), dtype = 'str')

	elif cur_Par == a:			#continue adding data to array
		temp_arr = np.genfromtxt(item, delimiter = '\t', usecols=(1), dtype = 'str')
		data_arr = np.vstack((data_arr,temp_arr))
		
	elif cur_Par !=a:			#end this data collection, calc mean, write file and start new array.
		if data_arr.ndim == 1:
			avg_arr = data_arr

		else :
			avg_arr = np.mean(data_arr.astype(np.float),axis=0)

		avg_arr = np.vstack((WL_arr,avg_arr))
		save_file = open(summ_file_base+str(cur_Par)+summ_file_ext, 'wb')
		np.savetxt(save_file, np.transpose(avg_arr), delimiter = '\t',fmt="%s")
		save_file.close()

		data_arr = np.genfromtxt(item, delimiter = '\t', usecols=(1), dtype = 'str')
		cur_Par = a
	
#average and save anything that is left after the loop.
if data_arr.ndim == 1:
	avg_arr = data_arr
else :
	avg_arr = np.mean(data_arr.astype(np.float),axis=0)

avg_arr = np.vstack((WL_arr,avg_arr))		
save_file = open(summ_file_base+str(a)+summ_file_ext, 'wb')
np.savetxt(save_file, np.transpose(avg_arr), delimiter = '\t',fmt="%s")
save_file.close()