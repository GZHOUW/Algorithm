'''
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:
    Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
    Output: [null,1,1,1,2,1,4,6]
    Explanation: 
    First, S = StockSpanner() is initialized.  Then:
    S.next(100) is called and returns 1,
    S.next(80) is called and returns 1,
    S.next(60) is called and returns 1,
    S.next(70) is called and returns 2,
    S.next(60) is called and returns 1,
    S.next(75) is called and returns 4,
    S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price
Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

'''
class StockSpanner():
    '''
    Demo:
    next(6) --> stack = [(6,1)]
    next(3) --> stack = [(6,1),(3,1)]
    next(5) --> stack = [(6,1),(5,2)]  (3,1) is popped and its span, 1, is added to the span of 5, which becomes 2
    next(1) --> stack = [(6,1),(5,2),(1,1)]
    next(9) --> stack = [(9,5)] all prices are popped becasue they are all smaller than 9
    '''
    
    def __init__(self):
        self.stack = []  # the stack keeps [largest price so far, second largest, ect], but when a large price is next, delete all smaller price

    def next(self, price):
        span = 1  # if price < prev (last element of stack), loop doesnt run
        
        while self.stack and price >= self.stack[-1][0]: # price >= prev
            span += self.stack.pop()[1]  # delete the days that have less price and get their spans
            
        self.stack.append((price, span))
        return span
