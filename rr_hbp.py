task=int(input("Enter number of tasks: "))
print("Enter the constraints i.e Source,Destination,Tool Conflict,Execution Time for all ",task," tasks: ")

jobs=[]

for i in range(task):
	li=list(map(str,input().strip().split(",")))
	jobs.append(li)

for i in range(task):
	jobs[i][3]=int(jobs[i][3])

jobs.sort(key= lambda job:job[3],reverse=True)

bin_size_time=int(input("Enter the bin-size time: "))
print("---------------------------------------------------")
print("\nShowing Results for Round Robin Scheduling Scheme")
print("---------------------------------------------------")

initial_time_rr=0
increment=bin_size_time

Time_rr_start=[0]*task
Time_rr_end=[0]*task

print("Task\t Starting Time \t End Time")
print("----\t --------------\t ---------")

for i in range(task):
	Time_rr_start[i]=i*bin_size_time
	Time_rr_end[i]=Time_rr_start[i]+jobs[i][3]
	print(i+1,"\t   ",Time_rr_start[i],"\t\t ",Time_rr_end[i])
print("----------------------------------------------------\n")
print("Time Cycle when bin size time: ",bin_size_time," is ", Time_rr_end[-1])
print("                              -----    -----")
print("\nNote: The task having highest execution time is numbered as first and second highest is numbered as second and so on (In both RR and HBP)\n")

##################################################################################################################################

print("----------------------------------")
print("Results for Heuristic Bin Packing ")
print("----------------------------------")
dict_task={}

for i in range(task):
	dict_task[i]=jobs[i]

normal_pointer=0
li_counter=[]
normal_pointer=0
final_output_time=[]

for i in range(len(jobs)):
	flag=0
	for j in range(i+1,len(jobs)):
		if(jobs[i][0]!=jobs[j][1] and jobs[i][1]!=jobs[j][0] and i not in li_counter and j not in li_counter):
			concurrent_task_time1=normal_pointer+jobs[i][3]
			concurrent_task_time2=normal_pointer+jobs[j][3]
			final_output_time.append([concurrent_task_time1,concurrent_task_time2])
			normal_pointer=normal_pointer+bin_size_time
			dict_task.pop(i)
			dict_task.pop(j)
			li_counter.append(i)
			li_counter.append(j)
			flag=1
			if(len(dict_task)==0):
				break
	if(len(dict_task)==0):
		break
	if(flag==0 and i not in li_counter):	
		normal_task_time=normal_pointer+jobs[i][3]
		normal_pointer=normal_pointer+bin_size_time
		final_output_time.append([normal_task_time])
		dict_task.pop(i)
		li_counter.append(i)
		if(len(dict_task)==0):
			break

Time_start_hbp=[]
task_count=0

for i in range(len(final_output_time)):
	Time_start_hbp.append(i*bin_size_time)


for i in range(len(final_output_time)):
	if(len(final_output_time[i])==1):
		task_count=task_count+1
		print("The start time of the task ",task_count," is ",Time_start_hbp[i]," and End Time is ",final_output_time[i][0])
	else:
		task_count=task_count+1
		print("The start time of the task ",task_count," is ",Time_start_hbp[i]," and End Time is ",final_output_time[i][0])
		task_count=task_count+1		
		print("The start time of the task ",task_count," is ",Time_start_hbp[i]," and End Time is ",final_output_time[i][1])

print("\nTime Cycle when bin size time:",bin_size_time," is  ",final_output_time[-1][-1])
print("                               ----     -----")
