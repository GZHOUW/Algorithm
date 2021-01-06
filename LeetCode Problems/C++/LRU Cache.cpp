/*
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Could you do get and put in O(1) time complexity?

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
At most 3 * 104 calls will be made to get and put.
*/

#include <vector>
#include <map>
using namespace std;

struct DoubleListNode {
	int val;
	int key;
	DoubleListNode* prev;
	DoubleListNode* next;

	DoubleListNode(int k, int v) {
		val = v;
		key = k;
		next = nullptr;
		prev = nullptr;
	}
};

class LRUCache {
public:
	LRUCache(int capacity) {
		capacity_ = capacity;
		cur_num = 0;
		DH = new DoubleListNode(0, 0); // Dummy head
		DT = new DoubleListNode(0, 0); // Dummy tail
		DH->next = DT;
		DT->prev = DH;
	}

	int get(int key) {
		//for (auto& t : cache_){
		//   cout << t.first << " " << t.second->val<<endl;

		//}   
		//cout << "-------------" <<endl;
		if (cache_.find(key) != cache_.end()) {
			// Put cache_[key] to the front, then return its val
			remove(cache_[key]);
			addFront(cache_[key]);
			return cache_[key]->val;
		}
		else {
			return -1;
		}
	}

	void put(int key, int value) {
		// If exist, capacity doesnt matter, simply update val
		if (cache_.find(key) != cache_.end()) {
			// update value and move front
			cache_[key]->val = value;
			// Move to front
			remove(cache_[key]);
			addFront(cache_[key]);
		}
		else {
			// Doesn't exist, need to create new
			DoubleListNode* new_node = new DoubleListNode(key, value);

			// If not exceeding capacity, add to dict and LL
			if (cur_num + 1 <= capacity_) {
				cur_num += 1;
			}
			else { // Capacity full
				cache_.erase(DT->prev->key);
				remove(DT->prev); //remove most recent
			}

			addFront(new_node); // place front   
			cache_[key] = new_node;// add to cache_
		}
	}

private:
	int capacity_;
	int cur_num; // current number of elements
	map<int, DoubleListNode*> cache_;
	DoubleListNode* DH;
	DoubleListNode* DT;

	void remove(DoubleListNode* node) {
		// Remove the node then add it to the front
		node->prev->next = node->next;
		node->next->prev = node->prev;
	}

	void addFront(DoubleListNode* node) {
		node->prev = DH;
		node->next = DH->next;
		DH->next->prev = node;
		DH->next = node;
	}
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
