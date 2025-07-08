# ability of object an adapt the code to the code to the type of data processing

# class dog:
#     def sound(self):
#         print("bow bow")
# class cat:
#     def sound(self):
#         print("meow meow")
#     def makesound(animaltype):
#         animaltype.sound()
# catobj=cat()
# dogobj=dog()


class Solution(object):
    def maxArea(self, height):
        res=0
        l,r=0,len(height)-1
        while l<r:
            area=(r-1)*min(height[l],height[r])
            res=max(res,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res