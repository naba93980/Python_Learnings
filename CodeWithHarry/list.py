# lists are mutable // kinda array in js

a = [2, 4, 1, 5, True, "Naba", 4, 7];
print(a)
print(type(a));

a[2]=10;
print(a);

# list slicing
friends = ["naba","modak","good","man","very good","kinda"];
print(friends[0:4]);
print(friends[3::-1]);  # ['man', 'good', 'modak', 'naba'];

b=[5,34,34,6,1,6,4356,7,8];
b.sort(); # sorts the list
print(b) 
b.reverse(); #reverses the list
print(b)
b.append(6666); #adds 6666 at the end of the list
print(b)
b.insert(2,45453); #inserts 45453 at index 2
print(b)
b.pop(4); #removes element at index 4
print(b);
b.remove(6666); #removes 6666 from the list
print(b);
