'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.
'''

def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    dx =  coordinates[1][0] - coordinates[0][0]
    dy =  coordinates[1][1] - coordinates[0][1]

    # dy/dx = (y[i] - y[i-1])/(x[i] - x[i-1]) cannot use division because of zero division error
    # dx * (y[i] - y[i-1]) = dy * (x[i] - x[i-1]) use multiplication instead
    for i in range(2, len(coordinates)):
        if dx * (coordinates[i][1] - coordinates[i-1][1]) != dy * (coordinates[i][0] - coordinates[i-1][0]):
            return False
    return True
