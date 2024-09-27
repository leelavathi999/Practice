# rotate matrix by 90 degrees
# approach used:save topleft element and start replacing back from bottomleft
# Time Complexity :O(n^2) Space Complexity : O(1)

class Solution:
    def rotateImg(self,m:list[list[int]]):
        l,r=0,len(m)-1
        while l<r:
            for i in range(l,r-l):
                top,bottom=l,r
                # save topleft
                topleft=m[top][l+i]
                # bottom left to top left
                m[top][l+i]=m[bottom-i][l]
                # bottom right to bottom left
                m[bottom-i][l]=m[bottom][r-i]
                # top right to bottom right
                m[bottom][r-i]=m[top+i][r]
                # topleft to top right
                m[top+i][r]=topleft
            l+=1
            r-=1
        return m
    

res=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(res.rotateImg(matrix))