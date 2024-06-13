#Program 1 Gymnastics
#This program takes all gymnists scores finds the average for each one and gives a final score then finds who got first, second and third
#Daniel Jaffe
#Date Last Motified 5/22/24

#This subroutine takes the gymnists average score removing the lowest and the highest

def gymaverage(scores):
    
    #Splits each line into a seperate array then remove the names, sorts the array and removes the min and max values.
    arrsort =[]
    arr_of_players = []
    for line in scores:
        line = line.rstrip("\n")
        arrline = line.split(",")
        name = arrline[0]
        arrline.remove(arrline[0])
        # Convert scores to floats for accurate sorting and calculations
        arrline = [float(score) for score in arrline]
        # Remove the lowest and highest scores (excluding 10s at the end)
        arrline.sort(key=lambda x: (x==10,x))
        arrline.remove(arrline[0])
        arrline.remove(arrline[8])
        #Finding the average and removing the highest and lowest scores
        total = 0
        i = 0
        while i < 8:
            total = total + float(arrline[i])
            i +=1
        avg = total/8
        placed = (f"['{name}',{avg:.4f}]")
        arr_of_players.append(placed)
        #Used ChatGPT to use this function
        array_list =[eval(item) for item in arr_of_players]
        #Used chatGPT to fiqure out how to sort using the second thing in the array
        sorted_array_list = sorted(array_list,key = lambda x: x[1])
        sorted_array_list.reverse()
        points_earned= (f"{name} earned {avg:.4f}")
        print(points_earned)
        arrsort.append(avg)
        
        #Determining who is first second and third
        #Look this function up at freeCodeCamp
        arrsort.sort(reverse = True)
        arrsort.append(avg)
    
    #Making sure the duplicates are removed
    array_first = []
    array_second= []
    array_third = []
    
    i = 0
    while i < len(sorted_array_list):
        if sorted_array_list[i][1] == sorted_array_list[i+1][1]:
            array_first.append(sorted_array_list[i])
            i +=1
        else:
            array_first.append(sorted_array_list[i])
            i +=1
            break
    
    while i < len(sorted_array_list):
        if sorted_array_list[i][1] == sorted_array_list[i+1][1]:
            array_second.append(sorted_array_list[i])
            i +=1
        else:
            array_second.append(sorted_array_list[i])
            i +=1
            break
    
    while i < len(sorted_array_list):
        if sorted_array_list[i][1] == sorted_array_list[i+1][1]:
            array_third.append(sorted_array_list[i])
            i +=1
        else:
            array_third.append(sorted_array_list[i])
            i +=1
            break

    i = 0
    while i < len(array_first):
        print(f"First place goes to {array_first[i][0]} with a score of {array_first[i][1]}.")
        i +=1
        
    i = 0    
    while i < len(array_second):
        print(f"Second place goes to {array_second[i][0]} with a score of {array_second[i][1]}.")         
        i+=1
        
    i = 0    
    while i < len(array_third):
        print(f"Third place goes to {array_third[i][0]} with a score of {array_third[i][1]}.")         
        i+=1
        
#Main Program
scores = open("scores.csv","r")
gymaverage(scores)