def selectionsort(studentper):
    for i in range(len(studentper)-1):
        small=i
        for j in range(i+1,len(studentper)):
            if studentper[small]>studentper[j]:
                small=j
        if small!=i:
            temp=studentper[i]
            studentper[i]=studentper[small]
            studentper[small]=temp

    print("The final sorted array via selection sort:",studentper)
    
def insertionsort(arr,l):
    for i in range (1,l):
        temp=arr[i]
        j=i-1
        while j>=0 and temp<=arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    print( f"The sorted array via insertion sort:{arr}")



studentper=[]
size=int (input("Enter the number of students:"))
for i in range (size):
    percentage=float(input("Enter percentage of a student:"))
    studentper.append(percentage)

print("The unsorted array: ",studentper)
def menu():
    while True:
        print("1:Display Selection sort:")
        print("2:Display Insertion sort:")
        
        choice=int(input("enter your choice:"))
        if choice==1:
            selectionsort(studentper)
            
        elif choice==2:
            insertionsort(studentper,size)

menu()
