class Solution:
    def maxArea(self, height: List[int]) -> int:
        #T(C(N)=O(N)) and S(C(N)=O(N)) as it requires Memory's size declare at Each iteration
        l,r=0,len(height)-1#variables intialize and Length declare
        area=0#area Inintlize
        while l<r:#Iterating upto Left and Right left level
            area=max(area,(r-l)*(min(height[l],height[r])))#Calculting Area
            if height[l]<height[r]:l+=1# Continer's Left Level Increment 
            else:r-=1#Container's Right Level Decrement
        return area#Printing Ares
