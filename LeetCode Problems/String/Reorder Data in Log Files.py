'''
You have an array of logs.  Each log is a space delimited string of words.For each log, the first word in each log is an alphanumeric identifier.  Then, either:
Each word after the identifier will consist only of lowercase letters, or; Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  
The digit-logs should be put in their original order. Return the final order of the logs.

Example 1:
    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Constraints:
    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    logs[i] is guaranteed to have an identifier, and a word after the identifier.
'''

class Solution:
    def reorderLogFiles(self, logs):
        
        # divide logs into two parts, one for digits, the other for letters
        digits = []
        letters = []
        for log in logs:
            if log[-1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        # Lambda functions: f = lambda x: x+10 ---> f(5) --> 15
        
        # when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[0]) 
        
        #sort by suffix
        letters.sort(key = lambda x: x.split()[1:])
        
        result = letters + digits  # put digit logs after letter logs
        return result
