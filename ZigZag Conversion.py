'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    zzList = []
    for i in range(numRows):
        zzList.append([])
    length = len(s)
    s_idx = 0
    col_idx = 0
    # add column by column
    while s_idx < length:
        if col_idx % (numRows - 1) == 0: # remainder = 0, fill all rows
            for i in range(numRows):
                try:
                    zzList[i].append(s[s_idx])
                    s_idx += 1
                except IndexError: # ends at last column
                    zzList[i].append('')
            col_idx += 1
        else: 
            for i in range(numRows):
                if i == numRows - col_idx % (numRows - 1) - 1:
                    zzList[i].append(s[s_idx])
                    s_idx += 1
                else:
                    zzList[i].append('')
            col_idx += 1

    result = ''
    for i in range(len(zzList)):
        for j in range(len(zzList[0])):
            if zzList[i][j] != '':
                result += zzList[i][j]

    return result
