#List
list = [1,2,3,4,5]
list.append(6)
list.insert(0, 0)
list[1] = 10
print("List: ",list)

#Tuple
tuple = (1,2,3,4,5)

#Set
set = {1,2,0,3,4,5}
set.add(6)
set.remove(1)
set.add(2)
print("Set: ",set)

my_dict = {"a": 1, "b": 2}
my_dict["a"] = 99
my_dict.update({"c": 3})
my_dict["d"] = 4
my_dict.pop("b", None)

print("Dictionary: ", my_dict)