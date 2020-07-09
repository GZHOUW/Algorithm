import numpy as np
'''
Multiply two matrix using divide and conquer
:param m1: n*n integer matrix where n is a power of 2
:param m2: n*n integer matrix where n is a power of 2
:return: Z = m1*m2

Pseudo Code:
if n == 1:
    return [[ X[0][0] * Y[0][0] ]]
else:
    A,B,C,D = sub-matrices of X
    E,F,G,H = sub-matrices of Y
'''

def classicMatMult(m1,m2):
    # print("Classical Matrix Multiplication goes here.")

    # print ("Len of m1: " + str(len(m1)))
    #Base case
    if (len(m1) == len(m2) == 2):
        # print("Base case!")
        matrix = np.array([
            # [ AE + BG ] , [ AF + BH]
            [m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0], m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]],
            # [ CE + DG ] , [ CF + DH]
            [m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0], m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]]
        ])
        # print(matrix)
        return matrix
    elif(len(m1) == len(m2)):
        # Does matrix multiplication
        # m1 = [ [A, B], [C, D] ]
        ########################
        # m2 = [ [E, F], [G, H] ]
        # print(m1)
        # print(m2)

        splitSize = int(len(m1)/2)
        # print(splitSize)
        #slices the arrays more easily than classicMatMult
        A, B, C, D = m1[:splitSize, :splitSize], m1[:splitSize, splitSize:], m1[splitSize:, :splitSize], m1[splitSize:, splitSize:]
        E, F, G, H = m2[:splitSize, :splitSize], m2[:splitSize, splitSize:], m2[splitSize:, :splitSize], m2[splitSize:, splitSize:]
        # print(A,B,C,D)
        # print(E,F,G,H)

        AE = classicMatMult(A,E)
        BG = classicMatMult(B,G)
        AF = classicMatMult(A,F)
        BH = classicMatMult(B,H)
        CE = classicMatMult(C,E)
        DG = classicMatMult(D,G)
        CF = classicMatMult(C,F)
        DH = classicMatMult(D,H)

        # does the additions for the matrix
        AEpBG = np.add(AE,BG)
        # print("AEpBG: \n" + str(AEpBG))
        AFpBH = np.add(AF,BH)
        # print("AFpBH: \n" + str(AFpBH))
        CEpDG = np.add(CE,DG)
        # print("CEpDG: \n" + str(CEpDG))
        CFpDH = np.add(CF,DH)
        # print("CFpDH: \n" + str(CFpDH))

        #rebuilds the matrix
        matrix = np.array(np.concatenate([np.concatenate([AEpBG,AFpBH],axis=1),np.concatenate([CEpDG,CFpDH],axis=1)]))
        return matrix
    else:
        print("Something went wrong, sorry.")

#takes input of m1 (matrix 1) and m2 (matrix 2) and returns the product via Strassen matrix multiplication
def strassenMatMult(m1,m2):
    if (len(m1) == len(m2) == 2):
        # print("Base case!")
        matrix = np.array([
            # [ AE + BG ] , [ AF + BH]
            [m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0], m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]],
            # [ CE + DG ] , [ CF + DH]
            [m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0], m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]]
        ])
        # print(matrix)
        return matrix
    elif (len(m1) == len(m2)):
        splitSize = int(len(m1)/2)
        # print(splitSize)
        #slices the arrays more easily than classicMatMult
        A, B, C, D = m1[:splitSize, :splitSize], m1[:splitSize, splitSize:], m1[splitSize:, :splitSize], m1[splitSize:, splitSize:]
        E, F, G, H = m2[:splitSize, :splitSize], m2[:splitSize, splitSize:], m2[splitSize:, :splitSize], m2[splitSize:, splitSize:]
        # print(A,B,C,D)
        # print(E,F,G,H)

        P1 = strassenMatMult(A,np.subtract(F,H))
        P2 = strassenMatMult(np.add(A,B),H)
        P3 = strassenMatMult(np.add(C,D),E)
        P4 = strassenMatMult(D,np.subtract(G,E))
        P5 = strassenMatMult(np.add(A,D),np.add(E,H))
        P6 = strassenMatMult(np.subtract(B,D),np.add(G,H))
        P7 = strassenMatMult(np.subtract(A,C),np.add(E,F))

        # P5 + P4 - P2 + P6
        A = np.add(np.subtract(np.add(P5,P4),P2),P6)
        # P1 + P2
        B = np.add(P1,P2)
        # P3 + P4
        C = np.add(P3,P4)
        # P1 + P5 - P3 - P7
        D = np.subtract(np.subtract(np.add(P1,P5),P3),P7)

        #rejoins the smaller matricies
        matrix = np.array(np.concatenate([np.concatenate([A,B],axis=1), np.concatenate([C,D],axis=1)]))
        return matrix
    else:
        print("Something went wrong, sorry.")