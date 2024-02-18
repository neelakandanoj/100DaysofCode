# Array

import array as ar
arr=ar.array('i',[1,2,3,4,5]) #int
arr1=ar.array('f',[1,2,3.4,4])  # float
arr2=ar.array('u',['a','b','c']) #char
print(arr2[1])

#Acessing
arr=ar.array('i',[1,2,3,4,5])
print(f"Accesing element {arr[4]}")

#Inserting
arr=ar.array('i',[1,2,3,4,5])
arr.insert(0,9)
print(f"Inserting element {arr}")

#Popping[index] 
arr=ar.array('i',[1,2,3,4,5])
arr.pop(3)
print("Pop",arr)

#Searching index of the elements
arr=ar.array('i',[7,2,1,55,44,2,1,3])
find=3
for i in range(0,len(arr)):
    if arr[i]==find:
        print(f"Element {find} is finded in index of {arr.index(find)}")
    



