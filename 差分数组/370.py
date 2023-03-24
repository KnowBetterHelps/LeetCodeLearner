class Solution:
    def increase(self, diff, update):
        diff[update[0]] += update[2]
        if update[1]+1 < len(diff):
            diff[update[1]+1] -= update[2]
        return diff
    
    def results(self, base, diff):
        base[0] = diff[0]
        for i in range(1, len(diff)):
            base[i] = base[i-1] + diff[i]
        return base

    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        base = [0 for i in range(length)]
        diff = base
        for i in range(len(updates)):
            diff = self.increase(diff, updates[i])
        
        #这里不需要将base
        return self.results(base, diff)