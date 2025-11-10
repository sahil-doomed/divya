def bubblesort(studentper):
    for i in range(len(studentper)):
        for j in range(len(studentper)-1):
            if studentper[j]>studentper[j+1]:
                temp=studentper[j]
                studentper[j]=studentper[j+1]
                studentper[j+1]=temp    
    print("Final sorted array via bubble sort:",studentper)
    
def quicksort(arr,start,end):
    if start<end :
        pivotindex=partitionfun(arr,start,end)
        quicksort(arr,start,pivotindex-1)
        quicksort(arr,pivotindex+1,end)
    return arr

def partitionfun(arr,start,end):
    pivot=arr[start]
    lb=start+1
    ub=end
    while True:
        while lb<=ub and arr[lb]<=pivot:
            lb+=1
             
        while lb<=ub and arr[ub]>=pivot:
            ub-=1
            
        if lb<=ub:
            arr[ub],arr[lb]=arr[lb],arr[ub]
        else:
            break
    arr[start],arr[ub]=arr[ub],arr[start]
    return ub
studentper=[]
size=int (input("Enter the number of students:"))
for i in range (size):
    percentage=float(input("Enter percentage of a student:"))
    studentper.append(percentage)

print("The unsorted array: ",studentper)
def menu():
    while True:
        print("1:Display Bubble sort:")
        print("2:Display Quick sort:")
        choice=int(input("enter your choice:"))
        if choice==1:
            bubblesort(studentper)
            
        elif choice==2:
            sort=quicksort(studentper,0,len(studentper)-1)
            print("Sorted array:",sort)

menu()
