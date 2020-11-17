# Ввод: 10 20 30
nums_str_lst = input().split() # "10 20 30".split() = ["10", "20", "30"]
nums = []
for i in range(len(nums_str_lst)):
    nums.append(int(nums_str_lst[i])) #[10, 20, 30]


print("Sum:", sum(nums))

ans_strs = []
for i in range(len(nums)):
    ans_strs.append(str(nums[i]))
print(", ".join(ans_strs))