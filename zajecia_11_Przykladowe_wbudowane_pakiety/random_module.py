import random

for number in range(6):
    print(random.randint(1, 60))

names_list = ["adam", "konrad", "tomek", "wojtek", "michal"]
for x in range(len(names_list)):
    selected_name = random.choices(names_list, k=1)
    print(selected_name[0])
    names_list.remove(selected_name[0])
