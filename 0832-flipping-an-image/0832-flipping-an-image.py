class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        a=len(image)
        b=len(image[0])
        for i in range(a):
            for j in range(b):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
        for k in image:
            k.reverse()
        return image
        