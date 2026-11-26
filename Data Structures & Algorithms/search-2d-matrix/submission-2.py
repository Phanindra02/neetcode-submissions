class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        for i in mat:
            if i[-1]==target:
                return True
            
            elif i[0]==target:
                return True 
            
            elif i[-1]>target and i[0]<target:
                l,r=0,len(i)-1
                while l<=r:
                    mid=(l+r)//2
                    if i[mid]==target:
                        return True
                    
                    elif i[mid]>target:
                        r=mid-1
                    
                    else:
                        l=mid+1
        return False