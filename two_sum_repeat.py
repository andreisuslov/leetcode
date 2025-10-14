def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
def two_sum_fast(nums, target):
    seen = {}
    for i in range(len(nums)):
        print(str(seen))
        print(i)

        compliment = target - nums[i]
        print(compliment)
        if compliment in seen:
            print("yes")
            return [seen[compliment], nums[i]]
        seen[nums[i]] = i

if __name__ == "__main__":
    nums = [0, 1, 3, 6, 15, 10]
    target = 21

    print(str(two_sum(nums, target)))
    print(str(two_sum_fast(nums, target)))