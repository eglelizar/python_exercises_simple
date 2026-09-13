#Given an array of integers and a target, get the indexes of the two numbers which their sum is equal to a target
#Example:
#. Input: nums = [9,2,5,6], target =7
#  Explanation: 1, 2

def getIndexesWhichValuesSumTarget(nums, target):
    lookingFor = [] # -2, 5
    indexes = {}
    results = []
    ind  = 0
    for x in nums:
        if  x in lookingFor:
            results.append (indexes[target - x])
            results.append (ind)
            return results
        numLookingFor = target - x  # 7 - 9 = -2, 7 - 2 =5
        lookingFor.append(numLookingFor)
        indexes[x] = ind
        ind = ind + 1

nums = [9,2,5,6]
target = 7
print(getIndexesWhichValuesSumTarget(nums, target))