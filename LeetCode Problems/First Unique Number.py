class FirstUnique:

    def __init__(self, nums):
        self.nums = nums
        self.occur = dict()
        for i in range(len(nums)):
            if nums[i] in self.occur:
                self.occur[nums[i]] += 1
            else:
                self.occur[nums[i]] = 1

    def showFirstUnique(self):
        for key in self.occur:
            if self.occur[key] == 1:
                return key
        return -1


    def add(self, value):
        if value in self.occur:
            self.occur[value] += 1
        else:
            self.occur[value] = 1


a = FirstUnique([7,7,7,7,7,7])
a.add(7)
a.add(3)
a.add(3)
a.add(7)
a.add(17)
print(a.showFirstUnique())
