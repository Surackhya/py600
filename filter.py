nums = [8,2,1,3,5,6]

# lambda function is used with map() and filter()

even = filter(lambda x: x%2 == 0, nums)
even = list(even)
print(f"even = {even}")

