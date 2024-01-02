from matplotlib import pyplot as plt	
import time
import json
import requests
import pandas as pd 
import numpy as np
import os 
from functions_Git import *
from csv import writer

#<!!! The following code is intended to be interpreted carefully reading the README.md file at https://github.com/codicigluoni/Gender-Econ-Pipeline !!!>#

########################### First Sector: Enviroment Set Up ###########################

# Academic Staff, retrieving data from database
response = requests.get('http://dati.ustat.miur.it/api/3/action/datastore_search?resource_id=92f2008d-958f-4e9c-ae5c-7a3dd418cd57&filters={%22AREA_SD%22:%2213%20-%20Scienze%20economiche%20e%20statistiche%22,%20%22CODICE_ATENEO%22:%22TTTTT%22}&limit=10000')
staff_response_json = json.loads(response.text)
data_academic = staff_response_json['result']['records'] #saving data for academics discarding non necessary information

# Studenti , retrieving data from database
stud_response = requests.get('http://dati.ustat.miur.it/api/3/action/datastore_search?resource_id=373294ff-b051-4ec1-996f-e52078640279&filters={%22ClasseNUMERO%22:[%22L-33%22,%22LM-56%22]}&limit=10000')
stud_response_json = json.loads(stud_response.text)
data_stud = stud_response_json['result']['records'] #saving data for students discarding non necessary information

Years = yr_interval(data_stud, data_academic) #function to extract year for which to analyze data

########################### Second Sector: Previous analysis check ###########################

flag = 0
n_yr = len(Years) #saving the number of years to be analyzed

path = os.path.dirname(os.path.realpath(__file__)) #getting file path
isExist = os.path.exists(path + '\\years.csv') #detecting if file years.csv exists


if  isExist: #if file exists, check if years evaluated are the same

	prv_years_data = pd.read_csv('years.csv') #extract years previously analized and saving it to list
	prv_yr = prv_years_data.yr.tolist()
	if Years == prv_yr:
		flag=1
		print('Years already evaluated')
		exit() #years have been already evaluated, do not run the code

########################### Third Sector: Data Analysis ###########################

if isExist and flag == 0 or not isExist: #if file exists and evaluated years are different or file does not exist

	pd.DataFrame(Years, columns=['yr']).to_csv('years.csv') #save new analyzed years  

	pg_staff_matrix = np.ones((n_yr,4)) #create matrix for female percentage regarding academic staff
	abs_staff_matrix = np.ones((n_yr,4)) #create matrix for female absolute values regarding academic staff

	i=0

	for yr in Years: #for every chosen year to be analyzed, do the following

		#declaring variables to calculate percentage of women for each academic position

		tot_res = 0
		tot_res_f = 0

		tot_assoc = 0
		tot_assoc_f = 0

		tot_ord = 0
		tot_ord_f = 0

		for staff in data_academic: #for each element in the database
			if staff['ANNO'] == yr:
				if staff['COD_QUALIFICA'] == '1PO':
					tot_ord = tot_ord + staff['N_AcStaff'] #calculating total number of Ordinary Professors in our field of interest
					if staff['GENERE'] == 'F':
						tot_ord_f = tot_ord_f + staff['N_AcStaff']  #calculating total number of female Ordinary Professors
				if staff['COD_QUALIFICA'] == '2PA':
					tot_assoc = tot_assoc + staff['N_AcStaff'] #calculating total number of Associate Professors
					if staff['GENERE'] == 'F':
						tot_assoc_f = tot_assoc_f + staff['N_AcStaff'] #calculating total number of female Associate Professors
				if staff['COD_QUALIFICA'] == '3RTD' or staff['COD_QUALIFICA'] == '3RU' or staff['COD_QUALIFICA'] == '4AR':
					tot_res = tot_res + staff['N_AcStaff'] #calculating total number of Reasearchers
					if staff['GENERE'] == 'F':
						tot_res_f = tot_res_f + staff['N_AcStaff'] #calculating total number of female Reasearchers

		#calculating percentages and absolute values and storing them in their matrixes, a row for each year

		pg_staff_matrix[i][0] = yr
		pg_staff_matrix[i][1] =  (tot_res_f/tot_res)*100
		pg_staff_matrix[i][2] = (tot_assoc_f/tot_assoc)*100
		pg_staff_matrix[i][3] = (tot_ord_f/tot_ord)*100

		abs_staff_matrix[i][0] = yr
		abs_staff_matrix[i][1] =  tot_res_f
		abs_staff_matrix[i][2] = tot_assoc_f
		abs_staff_matrix[i][3] = tot_ord_f
		i = i + 1

	pg_stud_matrix = np.ones((n_yr,3)) #create matrix for female percentage regarding students
	abs_stud_matrix = np.ones((n_yr,3)) #create matrix for female absolute values regarding students

	i=0

	for yr in Years: #for every chosen year to be analyzed, do the following

		#declaring variables to calculate percentage of women for Triennale (Bachelor) and Magistrale (Master)

		tot_trien = 0;
		tot_trien_f = 0;

		tot_mag = 0;
		tot_mag_f = 0;

		for stud in data_stud: #for each element in the database
			y = stud['AnnoA']
			formatted_y = int(y[:4]) #formatting years of database to be compared to years previously stored, ex. from 2021/2022 to 2021
			if formatted_y == yr:
				if stud['ClasseNUMERO'] == 'L-33':
					tot_trien = tot_trien + stud['Isc'] #calculating total number of Bachelor students
					if stud['SESSO'] == 'F':
						tot_trien_f = tot_trien_f + stud['Isc'] #calculating total number of female Bachelor students
				if stud['ClasseNUMERO'] == 'LM-56':
					tot_mag = tot_mag + stud['Isc'] #calculating total number of Master students
					if stud['SESSO'] == 'F':
						tot_mag_f = tot_mag_f + stud['Isc'] #calculating total number of female Master students

		#calculating percentages and absolute values and storing them in their matrixes, a row for each year

		pg_stud_matrix[i][0] = yr
		pg_stud_matrix[i][1] = (tot_trien_f/tot_trien)*100
		pg_stud_matrix[i][2] = (tot_mag_f/tot_mag)*100

		abs_stud_matrix[i][0] = yr
		abs_stud_matrix[i][1] = tot_trien_f
		abs_stud_matrix[i][2] = tot_mag_f
		i = i + 1

	#Saving data as csv

	fmt='%d','%1.3f','%1.3f','%1.3f','%1.3f','%1.3f' #format required for years and percentages in data_merge
	header_stud = ['Anno','Triennale	', 'Magistrale	', 'Ricercatrice', 'P. Associate', 'P. Ordinarie'] #create header
	pg_staff_matrix_merge = np.delete(pg_staff_matrix, 0, 1) #delete the year column since in the merge only one is required and it is contained in pg_stud_matrix
	data_merge= np.hstack((pg_stud_matrix,pg_staff_matrix_merge)) #merge the percentages matrix
	np.savetxt('data.csv', data_merge, delimiter=',', fmt=fmt) #save percentages as csv
	np.savetxt('fulldata.csv', [header_stud] ,delimiter=',',fmt="%s") #save header as csv

	with open('data.csv', 'r') as f1: 
		original = f1.read()

	with open('fulldata.csv', 'a') as f2:
		f2.write('\n')
		f2.write(original) #merge

	os.remove('data.csv') #delete the auxiliary file data.csv, now data with header are fully stored in fulldata.csv


	fmt='%d','%d','%d','%d','%d','%d' #format required for years and absolute values in data_merge
	header_stud = ['Anno','Triennale	', 'Magistrale	', 'Ricercatrice', 'P. Associate', 'P. Ordinarie'] #create header
	abs_staff_matrix_merge = np.delete(abs_staff_matrix, 0, 1) #delete the year column since in the merge only one is required and it is contained in pg_stud_matrix
	data_merge= np.hstack((abs_stud_matrix,abs_staff_matrix_merge)) #merge the absolute values matrix
	np.savetxt('data.csv', data_merge, delimiter=',', fmt=fmt) #save absolute values as csv
	np.savetxt('fulldata_abs.csv', [header_stud] ,delimiter=',',fmt="%s") #save header as csv

	with open('data.csv', 'r') as f1: 
		original = f1.read()

	with open('fulldata_abs.csv', 'a') as f2:
		f2.write('\n')
		f2.write(original) #merge

	os.remove('data.csv') #delete the auxiliary file data.csv, now data with header are fully stored in fulldata.csv

########################### Fourth Sector: Grafic Plot ###########################

	pl0t_th1s_gr4ph_abs(abs_stud_matrix, abs_staff_matrix, n_yr, Years) #calling the function to plot absolute values graph
	pl0t_th1s_gr4ph(pg_stud_matrix, pg_staff_matrix, n_yr, Years) #calling the function to plot percentage graph
