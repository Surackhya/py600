nums = [8,2,1,3,5,6]

# square each number:
# While True: loop infinite times run huna sakcha. Difference
# For loop chai finite time matra run huncha. Difference

# sq = []
# index = 0

# while index < len(nums): # for index in range(len(nums))

#     item = nums[index]
#     sq.append(item ** 2)
#     index = index + 1 

# print(sq)

sq = list(  map(lambda x:x**2, nums)  )
print(sq)
