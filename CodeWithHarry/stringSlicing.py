# strings are immutable

greeting = "Good_Morning";
name = "Harry";
# print(type(name));
c = greeting + name
print(c);
print(c[0:(len((c))-1):2]);
print(c[0::2]);
print(c[7:0:-1])  # roM_doo
print(c[:2:-1])  # yrraHgninroM_d


# cannot mutate  a string but can rerturn a new string with string.replace()

story = "once upon a time there was a youtuber named Naba";

# String Functions

# print(len(story));

# print(story.endswith("notes"));

# print(story.count("c"));

# print(story.capitalize());

# print(story.find("upon"));

print(story.replace("Harry", "CodeWithHarry"));

