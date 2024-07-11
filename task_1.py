# Write a Python function that takes a list of integers and returns a new list that
# contains the top k elements in the list.

n = int(input("Enter the len of list : "))
k = int(input("Enter the k elements : "))

d = []

for i in range(n):
    tmp = int(input("Enter the values : "))
    d.append(tmp)

print("Before sorting values : ",d)
d.sort(reverse=True)
print("After sorting values : ",d)

print("result : ", d[:k])