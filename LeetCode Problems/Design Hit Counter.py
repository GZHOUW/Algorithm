'''
Design a hit counter which counts the number of hits received in the past 5 minutes.
Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system 
in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();
// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
'''

class HitCounter:
    '''
    Algorithm:
    init: initialize an array of the first 300 seconds, each element is [timestamp, hits]
    hit: update the array so that the array contains [300 seconds ago: current second]
         add one to current second's hits
    getHits: update the array so that the array contains [300 seconds ago: current second]
             get the number of hits of current timestamp (certainly in the array)
    '''
    def __init__(self):
        self.record = [[i,0] for i in range(1,301)] # second, number of hits at that second

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        diff = timestamp - self.record[-1][0]
        if diff > 300:
            self.record = [[i,0] for i in range(timestamp-299, timestamp+1)]
        elif  0 < diff <= 300:
            self.record = self.record[diff:] + [[i,0] for i in range(timestamp-diff+1, timestamp+1)]
        
        for i in range(300):
            if self.record[i][0] == timestamp:
                self.record[i][1] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        diff = timestamp - self.record[-1][0]
        
        if diff > 300:
            self.record = [[i,0] for i in range(timestamp-299, timestamp+1)]
        elif  0 < diff <= 300:
            self.record = self.record[diff:] + [[i,0] for i in range(timestamp-diff+1, timestamp+1)]
           
        n_hits = 0
        for hit in self.record:
            n_hits += hit[1]
        return n_hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
