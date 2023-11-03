# mine
class Solution:
    def reverseWords(self, s: str) -> str:
        #initialization
        stack = []
        word = ""
        res = ""
        for char in s:
            #put words in s into variable:word
            if char != ' ':
                word += char
            #spilt by space to get singal word
            if char == ' ' and word:
                stack.append(word)
                word = ""
        #add the last word if the last char in s is not space
        if word and word[0] != ' ':
            stack.append(word)
        #get the output str
        while stack:
            res = res + stack.pop() + " "
        #delete the last char " " in res
        res = res[:-1]
        return res

        '''
        #it's very easy when using library function
        word = str.split()
        word.reverse()
        return ' '.join(word)
        '''