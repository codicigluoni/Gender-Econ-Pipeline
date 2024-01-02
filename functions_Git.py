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
	if i == 2 or (i>=2 and req_yr==2): #only two years available 
		Years.append(max(list_intersection))
		Years.append(min(list_intersection))
	if i == 1 or (i>=1 and req_yr==1): #only one year available 
		Years.append(max(list_intersection))
	if i == 0: #no years available
		print('Data not available')
		exit()

	Years.sort() #sorting years array in ascending order

	return Years

def pl0t_th1s_gr4ph(pg_stud_matrix, pg_staff_matrix, n_yr, Years):

	x = [1, 2, 3, 4, 5] #number of element in the x axis
	CB_color_cycle = ['#377eb8', '#ff7f00', '#4daf4a','#f781bf', '#a65628', '#984ea3','#999999', '#e41a1c', '#dede00'] #list of colors to make graph color blind friendly

	linestyle_str=[(0, (5, 10)),(0, (5, 5)),(0, (5, 1))] #linestyle for all years except the most recent one, which is displayed solid

	#following, the process to construct the matrix containing the percentage values previously calculated.
	#every row of the y matrix corresponds to an year for which the percentages have been calculated and each of those rows is plotted.

	for j in range(n_yr):
		if j == 0: #if this is the first year to be plotted, build the y axis matrix, which contains all the percentages calculated before
			y = [pg_stud_matrix[j][1], pg_stud_matrix[j][2], pg_staff_matrix[j][1], pg_staff_matrix[j][2], pg_staff_matrix[j][3]]
			plt.plot(x,y, color=CB_color_cycle[j], linestyle=linestyle_str[j], marker=".")
		elif j != n_yr-1: #stack every "row year" in the matrix
			row = [pg_stud_matrix[j][1], pg_stud_matrix[j][2], pg_staff_matrix[j][1], pg_staff_matrix[j][2], pg_staff_matrix[j][3]]
			y = np.vstack([y,row])
			plt.plot(x,y[j], color=CB_color_cycle[j], linestyle=linestyle_str[j], marker=".")
		elif j == n_yr-1: #custom formatting for the most recent year
			row = [pg_stud_matrix[j][1], pg_stud_matrix[j][2], pg_staff_matrix[j][1], pg_staff_matrix[j][2], pg_staff_matrix[j][3]]
			y = np.vstack([y,row])
			plt.plot(x,y[j], color=CB_color_cycle[j], marker=".")

	labels = ['Triennale', 'Magistrale', 'Ricercatrici', 'P. Associate', 'P. Ordinarie'] #define x values name

	plt.title("Leaky Pipeline in percentuale")
	plt.ylabel("Presenza femminile in %")
	plt.legend([Years[k] for k in range(n_yr)]) #display the legend referring to the years of interest
	plt.grid() #add a grid on the graph background
	plt.xticks (x, labels) #rename x values
	plt.ylim(bottom=0) #make the graph start from 0 on y axis

	plt.gcf().set_size_inches(12, 6) #set graph size 
	plt.savefig('graph.png', bbox_inches='tight', dpi=200) #save graph
	plt.clf() #clear the graph


def pl0t_th1s_gr4ph_abs(abs_stud_matrix, abs_staff_matrix, n_yr, Years):

	x = [1, 2, 3, 4, 5] #number of element in the x axis
	CB_color_cycle = ['#377eb8', '#ff7f00', '#4daf4a','#f781bf', '#a65628', '#984ea3','#999999', '#e41a1c', '#dede00'] #list of colors to make graph color blind friendly

	linestyle_str=[(0, (5, 10)),(0, (5, 5)),(0, (5, 1))] #linestyle for all years except the most recent one, which is displayed solid

	#following, the process to construct the matrix containing the percentage values previously calculated.
	#every row of the y matrix corresponds to an year for which the percentages have been calculated and each of those rows is plotted.

	for j in range(n_yr):
		if j == 0: #if this is the first year to be plotted, build the y axis matrix, which contains all the percentages calculated before
			y = [abs_stud_matrix[j][1], abs_stud_matrix[j][2], abs_staff_matrix[j][1], abs_staff_matrix[j][2], abs_staff_matrix[j][3]]
			plt.plot(x,y, color=CB_color_cycle[j], linestyle=linestyle_str[j], marker=".")
		elif j != n_yr-1: #stack every "row year" in the matrix
			row = [abs_stud_matrix[j][1], abs_stud_matrix[j][2], abs_staff_matrix[j][1], abs_staff_matrix[j][2], abs_staff_matrix[j][3]]
			y = np.vstack([y,row])
			plt.plot(x,y[j], color=CB_color_cycle[j], linestyle=linestyle_str[j], marker=".")
		elif j == n_yr-1: #custom formatting for the most recent year
			row = [abs_stud_matrix[j][1], abs_stud_matrix[j][2], abs_staff_matrix[j][1], abs_staff_matrix[j][2], abs_staff_matrix[j][3]]
			y = np.vstack([y,row])
			plt.plot(x,y[j], color=CB_color_cycle[j], marker=".")

	labels = ['Triennale', 'Magistrale', 'Ricercatrici', 'P. Associate', 'P. Ordinarie'] #define x values name

	plt.title("Leaky Pipeline in valore assoluto")
	plt.ylabel("Presenza femminile in valore assoluto")
	plt.legend([Years[k] for k in range(n_yr)]) #display the legend referring to the years of interest
	plt.grid() #add a grid on the graph background
	plt.xticks (x, labels) #rename x values
	plt.ylim(bottom=0) #make the graph start from 0 on y axis

	plt.gcf().set_size_inches(12, 6) #set graph size 
	plt.savefig('graph_abs.png', bbox_inches='tight', dpi=200) #save graph
	plt.clf() #clear the graph
