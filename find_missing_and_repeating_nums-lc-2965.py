class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n=len(grid)
        a=[]
        b=[]
        freq={}
        for row in grid:
            for i in row:
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
        for key,value in freq.items():
            if value > 1:
                a.append(key)


        for i in range(1,n*n+1):
            if i not in freq:
                b.append(i)


        req=a+b
        return req