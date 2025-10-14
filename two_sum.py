def two_sum_easy(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums2 = [2, 7, 11, 15]

target = 9

def two_sum(nums, target):
    seen = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]  # what we need
        print(str(i))

        print("compliment: " + str(target) + " - " + str(nums[i]) + " = " + str(target - nums[i]))

        # seen?
        if complement in seen:
            print("complement's position in seen dictionary: " + str(seen[complement]))
            return [seen[complement], i]
        
        # Remember this number and its position
        seen[nums[i]] = i
        print("seen: " + str(seen))

if __name__ == "__main__":
    nums1 = [25, 7, 11, 2]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print()