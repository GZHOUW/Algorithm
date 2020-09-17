/*
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

Example 2:
    Input: "cbbd"
    Output: "bb"
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    /*
    Algorithm:
    for s + dist = e, str[s:e] will be palindromic if (str[s] == str[e] and str[s + 1:e - 1] is palindromic)
    */
    string longestPalindrome(string s) {
        if (s.length() <= 1) return s;
        vector<vector<bool>> dp(s.length(), vector<bool> (s.length(), false));
        int maxLen = 0;
        string res;
        
        for (int start=dp.size()-1; start>=0; start--){
            for (int end =dp[0].size()-1;end>=0; end--){
                if (start == end){
                    dp[start][end] = true; // char of length 1, must be panlindrome
                    if (end - start + 1 > maxLen){ // 1 > 0
                        maxLen = end - start + 1; // 1
                        res = s.substr(start, maxLen); // current char
                    }
                }
                // start and end equal, might be palindrome
                else if (end > start && s[start] == s[end]){
                    
                    if (end - start == 1){ // substring of two same letters, must be palindrome
                        dp[start][end] = true;
                        if (end - start + 1 > maxLen){
                            maxLen = end - start + 1;
                            res = s.substr(start, maxLen);
                        }
                    }
                    else{ // see if the substring in between is palindrome
                        if (start < dp.size()-1){
                            dp[start][end] = dp[start+1][end-1]; 
                            if (dp[start][end]==true && end - start + 1 > maxLen){
                                maxLen = end - start + 1;
                                res = s.substr(start, maxLen);
                            }
                        } 
                    }
                }
            }
        }
        return res;
    }
};

int main(){
    
}