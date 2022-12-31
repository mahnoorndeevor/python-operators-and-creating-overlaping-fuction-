import operator
a,b=0,1
print(operator.and_(a,b))

print(operator.xor(a,b))

print(operator.invert(a))
print(operator.or_(a,b))



def overlapping(list1, list2):
 
  
 for item in list1:
     if item in list2:
        print("overlapping",item)
     else:
        print("not overlapping",item)
        if item in list3:
            print("overlapping",item)
        else:
            print("not overlap",item)
 return
 
list1 = [9, 5, 3, 4, 8]
list2 = [6, 7, 8, 9]
list3 = [7, 4, 6, 8, 3]
print(overlapping(list2, list3))

def overlapping(list1, list2):
 
  for item in list1:
    for item2 in list2:
      if item==item2:
        print("overlapping of list1 element: ",item," with list2 element: ", item2)
      # else:
      #   print("not overlapping")
  return 0
list1 = [9, 5, 3, 4, 8]
list2 = [6, 7, 8, 9]
print(overlapping(list1, list2))

def overlapping(list1, list2):
 
  for item in list1:
    for item2 in list2:
      if item==item2:
        print("overlapping of list1 element: ",item," at position",list1.index(item)," with list2 element: ", item2," at position",list2.index(item2))
      # else:
      #   print("not overlapping")
  return 0;
list1 = [9, 5, 3, 4, 8]
list2 = [6, 7, 8, 9]
print(overlapping(list1, list2))

def overlapping(list1, list2):
 
  for item in list1:
    for item2 in list2:
      if item==item2:
        # print("overlapping of list1 element: ",item," at position",list1.index(item)," with list2 element: ", item2," at position",list2.index(item2))
        print("Item[",list1.index(item),"] overlap with Item2[",list2.index(item2),"] with value",item)
      # else:
      #   print("not overlapping")
  return 0
list1 = [9, 5, 3, 4, 8]
list2 = [6, 7, 8, 9]
print(overlapping(list1, list2))

