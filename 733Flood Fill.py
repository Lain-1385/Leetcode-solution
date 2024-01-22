class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        else:
            temp = image[sr][sc]
            image[sr][sc] = color
        if sr > 0 and image[sr-1][sc] == temp:
            self.floodFill(image, sr - 1, sc, color)
        if sc > 0 and image[sr][sc-1] == temp:
            self.floodFill(image, sr, sc - 1, color)
        if sr + 1 < len(image) and image[sr + 1][sc] == temp:
            self.floodFill(image, sr + 1, sc, color)
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == temp:
            self.floodFill(image, sr, sc + 1, color)
        return image