'''
Reverse bits of a given 32 bits unsigned integer.

Example 1:
    Input: 00000010100101000001111010011100
    Output: 00111001011110000010100101000000
    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
    so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
    Input: 11111111111111111111111111111101
    Output: 10111111111111111111111111111111
    Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, 
    so return 3221225471 which its binary representation is 10111111111111111111111111111111.
'''

class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            lastBit = n & 1
            n = n >> 1
            lastBit = lastBit << (32-(i+1)) # move the bit to front
            res +=  lastBit
        return res
    
    def reverseBitsNoLoop(self, n):
        '''
        1). Break the original 32-bit into 2 blocks of 16 bits, and switch them.
        2). Break the 16-bits block into 2 blocks of 8 bits. Similarly, we switch the position of the 8-bits blocks
        3). Break the blocks into smaller blocks, until we reach the level with the block of 1 bit.
        4). At each of the above steps, we merge the intermediate results into a single integer which serves as the input for the next step.
        '''
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) # 11111111000000001111111100000000
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4) # 00001111000011110000111100001111
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2) # 11001100110011001100110011001100
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1) # 01010101010101010101010101010101
        return n
