# if the element (cell) is zero then set to it's corresponding row and column to zero
# using one variable for to identify is any element in the 1st column is zero
# time complexity : O(n^2)  and Space Complexity : O(1)
# using 1st row and column in matrix to keep track of which rows and columns need to set zero
class Solution:
    def setToZero(self,m:list[list[int]]):
        rows,cols=len(m),len(m[0])
        rowzero=False
        for r in range(rows):
            for c in range(cols):
                if m[r][c] == 0:
                    m[0][c]=0
                    if r>0:
                        m[r][0]=0
                    else:
                        rowzero=True
        # set elements to zero
        for r in range(1,rows):
            for c in range(1,cols):
                if m[0][c] == 0 or m[r][0] == 0:
                    m[r][c]=0

        # check for [0][0] element to modify the rows
        if m[0][0] == 0:
            for r in range(rows):
                m[r][0]=0
        # set columns to zero of 1st row
        if rowzero:
            for c in range(cols):
                m[0][c]=0

        return m 
    
res=Solution()
matrix=[[1,0,1],
        [1,0,1],
        [0,1,1]]
print(res.setToZero(matrix))