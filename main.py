# sets is a collection of unique objects.
sample_list = [1,2,3,1,2,3]
print(sample_list)

sample_set = set(sample_list)
print(sample_set)

if 10 in sample_set:
    print("Yes! It is there")
else:
    print("No, it is not there.")

mySet = set([])
mySet.add(100)
mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(4)
mySet.add(5)
print(mySet)

mySet.remove(100)
print(mySet)

# mySet.remove(200)------- remove will throw error , if the element is not present in the set

mySet.discard(200)
print (mySet)

#Set operations
# 1) Union
# 2) Intersection
# 3) Difference
# 4) Symmetric difference

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a | b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

print (a - b)
print(b - a)
print(a.difference(b))
print(a.difference(b))

print (a ^ b)
print(a.symmetric_difference(b))