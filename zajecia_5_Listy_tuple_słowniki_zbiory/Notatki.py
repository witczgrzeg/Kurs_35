sample_set = {"a", "b", "c"}
sample_list = ["a", "b", "c"]
print(f"sample list: {sample_list}")
print(f"sample set{sample_set}")
print("set:{} list: {}".format(len(sample_set), len(sample_list)))
sample_set.add("c")
sample_list.append("c")
print("set:{} list: {}".format(len(sample_set), len(sample_list)))
print(f"sample list po dodaniu: {sample_list}")
print(f"sample set po dodaniu: {sample_set}")