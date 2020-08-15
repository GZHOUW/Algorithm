'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

class Solution:
    def minMeetingRooms(self, intervals):
        '''
        Algorithm: go through all the intervals, and see if current interval can be added to 
                    a existing room, if not, create a new room for current interval
                    return the final number of rooms created
        '''
        if not intervals:
            return 0
        intervals.sort()
        room_num = 1
        rooms = [  [] for _ in intervals]
        rooms[0].append(intervals[0])
        for i in range(1, len(intervals)):
            for j in range(len(rooms)):
                if rooms[j] != []:
                    last_int = rooms[j][-1]
                    # append to current room if no overlap
                    if intervals[i][0] >= last_int[1]:
                        rooms[j].append(intervals[i])
                        break
                else:
                    rooms[j].append(intervals[i])
                    room_num = j+1
                    break               
        return room_num
    def minMeetingRoomsHeap(self, intervals):
        '''
        Heap Method: 
        '''
        if not intervals:
            return 0

        rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:
            # If the existing room with earliest ending time (rooms[0]) ends before cur's start, replace that room's meeting with cur
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)

            # If a new room is to be assigned, then add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(rooms)
