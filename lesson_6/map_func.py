nums = [1, 2, 3, 4, 5, 6, 7, 9, 8]


def odd_even(num):
    if num % 2 == 0:
        return 'even'
    if num % 2 == 1:
        return 'odd'


parity = list(map(odd_even, nums))
res = {}
for i in range(0, len(nums)):
    res[nums[i]] = parity[i]
print(res)
