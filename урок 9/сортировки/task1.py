# сортировка пузырьком
def bubble(list_nums):  
    swap_bool = True
    while swap_bool:
        swap_bool = False
        for i in range(len(list_nums) - 1):
            if list_nums[i] > list_nums[i + 1]:
                list_nums[i], list_nums[i + 1] = list_nums[i + 1], list_nums[i]
                swap_bool = True
nums = [54, 43, 3, 11, 0]   
bubble(nums)
print(nums) 