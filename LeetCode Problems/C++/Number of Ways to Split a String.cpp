/*
Given a binary string s (a string consisting only of '0's and '1's), we can split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).
Return the number of ways s can be split such that the number of characters '1' is the same in s1, s2, and s3.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: s = "10101"
    Output: 4
    Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
    "1|010|1"
    "1|01|01"
    "10|10|1"
    "10|1|01"

Example 2:
    Input: s = "1001"
    Output: 0

Example 3:
    Input: s = "0000"
    Output: 3
    Explanation: There are three ways to split s in 3 parts.
    "0|0|00"
    "0|00|0"
    "00|0|0"

Example 4:
    Input: s = "100100010100110"
    Output: 12

Constraints:
s[i] == '0' or s[i] == '1'
3 <= s.length <= 10^5
*/

class Solution {
public:
    int numWays(string s) {
        /*
        Algorithm: get the number of total ones, divide by 3 ---> num_of_ones
            group s into 3 so that 1st START with 1, 3rd group END with 1, and each contain num_of_ones 1s
            Ex: "100100010100110" --> 1001, 101, 110
            count the number of zeros between 1st and 2nd group --> zeros12
            count the number of zeros between 2nd and 3rd group --> zeros23
            res = (zeros12+1)  *  (zeros23+1)
        */
        long long mod=1000000007;
        long long ans;
        int num_ones = 0, group_ones, cur_ones = 0, g1_end, g2_start, g2_end, g3_start;
        for (int i = 0; i < s.size(); i++){
            if (s[i] == '1'){
                num_ones += 1;
            }
        }
        
        if (num_ones % 3 != 0){ // cannot divide by 3, no solution
            return 0; 
        }
        else if (num_ones == 0){
            long long n = s.size() - 2;
            ans =  (          (n*(n+1))%mod /2)%mod;
            return (int) ans;
        }
        else{
            group_ones = num_ones / 3; // the number of 1s in each group
            
            for (int i = 0; i < s.size(); i++){
                if (s[i] == '1'){
                    cur_ones += 1;

                    if (cur_ones == group_ones){
                        g1_end = i;
                    }
                    if (cur_ones == group_ones + 1){
                        g2_start = i;
                    }
                    if (cur_ones == 2*group_ones){
                        g2_end = i;
                    }
                    if (cur_ones == 2*group_ones + 1){
                        g3_start = i;
                    }
                }
            }
            ans =  (((g2_start - g1_end)%mod) * ((g3_start - g2_end)%mod)%mod);
            return (int) ans;
        }
    }
};
