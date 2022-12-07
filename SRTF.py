##########################################
# University of Information Technology 	 #	 
# IT007 Operating System                 #                                
# Nhóm Ubuntu, 21520430_2152115_21521938 #         
# File: task2-SRTF.py                    #    
##########################################

n = int(input('Enter total number of process: '))  

#Tạo mảng theo n
Process = [0] * (n+1)
ArrivalTime = [0] * (n+1)
BurstTime = [0] * (n+1)
StartTime = [0] * (n+1)
resTime = [0] * (n + 1)

finishTime = [0] * (n + 1)
turnTime = [0] * (n + 1)
waitTime = [0] * (n + 1)

#Nhập vào mảng
for i in range(n):  
    print("\n")
    BurstTime[i] = int(input('Enter the burst time for process {} : '.format(i + 1)))
    ArrivalTime[i] = int(input('Enter the arrival time for process {} : '.format(i + 1))) 
    Process[i] = [BurstTime[i], ArrivalTime[i], i, StartTime[i]]  

#Xóa phần tử 0 
Process.pop(-1) 
finishTime.pop(-1)
waitTime.pop(-1)
turnTime.pop(-1)
BurstTime.pop(-1)  
ArrivalTime.pop(-1) 
StartTime.pop(-1)
resTime.pop(-1)
i = 0
list = []  

#Hoán đổi phần tử có arrival time = 0 lên đầu mảng
tag = Process[0]

for i in Process:
    if i[1] == 0:
        tag = i
        index = Process.index(tag) 

temp = Process[0]
Process[0] = tag
Process[index] = temp

print(Process)

#Xử lí Process
for i in range(0, sum(BurstTime)):
	l = [j for j in Process  if j[1] <= i]
	l.sort(reverse= False ,key=lambda x: x[0]) 
	Process[Process.index(l[0])][0] -= 1 
	if(Process[Process.index(l[0])][3] == 0):
		Process[Process.index(l[0])][3] = i
	for k in Process:
		if k[0] == 0:   
			t = Process.pop(Process.index(k))
			list.append([k, i + 1])	

for i in list:
    finishTime[i[0][2]] = i[1] 
    StartTime[i[0][2]] = i[0][3]

#Tính toán 
for i in range(len(finishTime)):    
	turnTime[i] = finishTime[i] - ArrivalTime[i]    
	waitTime[i] = turnTime[i] - BurstTime[i]
	resTime[i] = StartTime[i] - ArrivalTime[i]

#Xuất kết quả
print("\n")
print('ID\tBurstTime\tArrivalTime\tStartTime\tFinishTime\tResponseTime\tTurnTime\tWaitTime')
for i in range(len(finishTime)):   
	print("{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(i, BurstTime[i], ArrivalTime[i],StartTime[i], finishTime[i], resTime[i], turnTime[i], waitTime[i]))   
print('Average Waiting Time = ', sum(waitTime)/len(waitTime))  
print('Average Turnaround Time = ', round(sum(turnTime)/len(turnTime), 3))    
print('Average Response Time = ', round(sum(resTime)/len(resTime), 3))
