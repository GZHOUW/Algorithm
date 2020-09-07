/*
Given a string s and an array of integers cost where cost[i] is the cost of deleting the character i in s.
Return the minimum cost of deletions such that there are no two identical letters next to each other.
Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

Example 1:
  Input: s = "abaac", cost = [1,2,3,4,5]
  Output: 3
  Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

Example 2:
  Input: s = "abc", cost = [1,2,3]
  Output: 0
  Explanation: You don't need to delete any character because there are no identical letters next to each other.

Example 3:
  Input: s = "aabaa", cost = [1,2,3,4,1]
  Output: 2
  Explanation: Delete the first and the last character, getting the string ("aba").


Constraints:
  s.length == cost.length
  1 <= s.length, cost.length <= 10^5
  1 <= cost[i] <= 10^4
  s contains only lowercase English letters.
*/

class Solution {
public:
    int minCost(string s, vector<int>& cost) {
        /*
        Algorithm: iterate through s, if meet repeating chars, 
        find the total cost and min cost of those chars, then
        final cost add (total cost - min cost)
        */
        if (s.size() == 1){
            return 0;
        }
        
        int final_cost = 0;
        int i=0, j, total_cost, max_cost;
        
        while (i < s.size()){
            if (s[i] == s[i+1]){ // only check the right, bc the left is already dealth with by previous iterations
                j = i;
                total_cost = cost[j];
                max_cost = cost[j];
                // Only keep the max cost char, delete the rest
                while (s[j] == s[j+1]){
                    total_cost += cost[j+1];
                    max_cost = max(max_cost, cost[j+1]);
                    j ++;
                }
                final_cost += total_cost - max_cost;
                i = j;
            }
            else{
                i ++;
            }
        }
        return final_cost;
    }
};
