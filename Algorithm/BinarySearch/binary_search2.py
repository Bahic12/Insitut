from binary_search import binary_search
mylist1 = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
mylist2 = [45,65,12,11,95,65,15,34,25,2,7,85,94,19,67]
mylist2.sort()
print(binary_search(mylist1,15))
print(binary_search(mylist2,25))
fruits = ['apple','fig','peach','quince','Cherry']
fruits.sort()
print(binary_search(fruits,'fig'))