class summranges(object):
    def summaryRanges(self, nums):
        outputlist = []
        firstiteration = 'yes'
        i = 0
        while i < len(nums):
            if i < len(nums) - 1:
                checknext = nums[i+1]
            elif i == len(nums) -1:
                checknext = "none"


            if firstiteration == 'yes':
                firstiteration = 'no'
                initialnumba = nums[i]

            if checknext == nums[i] + 1:
                i += 1
            elif checknext != nums[i] +1 and initialnumba != nums[i]:
                outputlist.append(str(initialnumba) + "->" + str(nums[i]))
                firstiteration = 'yes'
                i += 1
            elif initialnumba == nums[i] or checknext == "none":
                outputlist.append(str(initialnumba))
                firstiteration = 'yes'
                i += 1
        return outputlist

result = summranges().summaryRanges([0,1,2,4,5,7])
print(result)