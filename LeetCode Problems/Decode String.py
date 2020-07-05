class Solution:
    def decodeString(self, s):
        '''
        s = "3[a2[c]]" 
        '''
        stack = []; curNum = 0; curStr = ''
        for char in s:
            if char == '[':
                stack.append(curStr) # append even when empty so that stack is always [str,num,str,num,...]
                stack.append(curNum)
                
                # reset str and num
                curStr = ''
                curNum = 0
            elif char == ']':
                # in a2[c], 'a' is prevStr, 2 is num, 'c' is curStr
                # stack = [a,2]
                num = stack.pop() # the number that is on the left of last '['
                prevStr = stack.pop() # the string that is on the left of last '['
                curStr = prevStr + num*curStr # update curStr
            elif char.isdigit():
                curNum = curNum*10 + int(char)
            else:
                curStr += char
        return curStr 
