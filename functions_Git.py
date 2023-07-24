from matplotlib import pyplot as plt	
import numpy as np

def yr_interval(data_stud,data_accademic):
	Years = []

	Staff_year_list = set([staff['ANNO'] for staff in data_accademic]) #unique years in the academic list
	Stud_year_list = set([stud['AnnoA'] for stud in data_stud]) #unique years in the student list
	Stud_year_list = [int(i[:4]) for i in Stud_year_list] #truncation of years from years/years+1 format to years format (ex. 2020/2021 to 2020)
	list_intersection = list(set(Staff_year_list).intersection(Stud_year_list)) #retrieving common years between databases

	i = len(list_intersection) #number of available years
	req_yr = 4 #desired number of years to be analyzed

	#following, construction of the array that contains the years to be analyzed

	if i >= 4 and req_yr > 3:
		Years.append(max(list_intersection)) #most recent year
		Years.append(min(list_intersection)) #less recent year
		#below, the two years equally far from the years above (most recent and less recent) and between them, they lie in "the middle"
		Years.append(min(list_intersection, key=lambda x:abs(x-(int(min(list_intersection) + ((max(list_intersection)-min(list_intersection))/3)*2)))))
		Years.append(min(list_intersection, key=lambda x:abs(x-(int(min(list_intersection) + (max(list_intersection)-min(list_intersection))/3)))))
	if i >= 3 and req_yr == 3:
		Years.append(max(list_intersection))
		Years.append(min(list_intersection))
		#the year that is the nearest from the value that lies exactly in the middle between the most recent year and the less recent year
		Years.append(min(list_intersection, key=lambda x:abs(x-(int(min(list_intersection) + (max(list_intersection)-min(list_intersection))/2)))))
	if i == 2: #only two years available 
		Years.append(max(list_intersection))
		Years.append(min(list_intersection))
	if i == 1: #only one year available 
		Years.append(max(list_intersection))
	if i == 0: #no years available
		print('Data not available')
		exit()

	Years.sort() #sorting years array in ascending order

	return Years

def pl0t_th1s_gr4ph(pg_stud_matrix, pg_staff_matrix, n_yr, Years):

	x = [1, 2, 3, 4, 5] #number of element in the x axis

	#following, the process to construct the matrix containing the percentage values previously calculated.
	#every row of the y matrix corresponds to an year for which the percentages have been calculated and each of those rows is plotted.

	for j in range(n_yr):
		if j == 0: #if this is the first year to be plotted, build the y axis matrix, which contains all the percentages calculated before
			y = [pg_stud_matrix[j][1], pg_stud_matrix[j][2], pg_staff_matrix[j][1], pg_staff_matrix[j][2], pg_staff_matrix[j][3]]
			plt.plot(x,y)
		else: #stack every "row year" in the matrix
			row = [pg_stud_matrix[j][1], pg_stud_matrix[j][2], pg_staff_matrix[j][1], pg_staff_matrix[j][2], pg_staff_matrix[j][3]]
			y = np.vstack([y,row])
			plt.plot(x,y[j])

	labels = ['Triennale', 'Magistrale', 'Ricercatore', 'P. Associato', 'P. Ordinario'] #define x values name

	plt.title("Leaky Pipeline")
	plt.ylabel("Presenza femminile in %")
	plt.legend([Years[k] for k in range(n_yr)]) #display the legend referring to the years of interest
	plt.grid()
	plt.xticks (x, labels) #rename x values

	plt.gcf().set_size_inches(12, 6) #set graph size 
	plt.savefig('graph.png', bbox_inches='tight', dpi=200) #save graph