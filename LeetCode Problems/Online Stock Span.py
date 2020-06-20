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
