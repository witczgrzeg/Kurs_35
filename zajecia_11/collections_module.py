from collections import defaultdict, Counter


very_long_string = "This is a very long string that we will use to demonstrate the DefaultDict functionality in Python. "

counter_dict = {}
default_counter_dict = defaultdict(int)

# for letter in very_long_string:
#     default_counter_dict[letter] += 1
#
# print(default_counter_dict)

counter = Counter(very_long_string)
print(counter)