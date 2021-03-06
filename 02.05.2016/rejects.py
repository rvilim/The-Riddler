import numpy as np

def rejects():
    # This function returns the "rejects", e.g. solutions that must be beat in all valid solutions
    return np.array([[10,10,10,10,10],
              [0, 6, 7 , 12, 25],
              [0, 3, 16, 10, 21],
              [1, 1, 6, 19, 23],
              [0, 1, 6, 17, 26],
              [0, 1, 21, 5, 23],
              [1, 0, 11, 17, 21],
              [0, 1, 4, 20, 25],
              [1, 1, 8, 15, 25],
              [0, 3, 8, 17, 22],
              [1, 0, 7, 20, 22],
              [1, 1, 7, 19, 22],
              [2, 0, 16, 8, 24],
              [1, 2, 9, 17, 21],
              [0, 0, 18, 5, 27],
              [2, 0, 11, 16, 21],
              [0, 3, 8, 16, 23],
              [1, 3, 10, 15, 21],
              [0, 0, 24, 2, 24],
              [1, 0, 5, 19, 25],
              [0, 0, 1, 24, 25],
              [1, 0, 15, 8, 26],
              [0, 2, 6, 18, 24],
              [3, 0, 13, 12, 22],
              [1, 2, 13, 10, 24],
              [0, 2, 9, 18, 21],
              [3, 0, 12, 13, 22],
              [2, 2, 10, 14, 22],
              [0, 2, 8, 15, 25],
              [2, 1, 10, 16, 21],
              [0, 1, 10, 18, 21],
              [0, 0, 21, 7, 22],
              [0, 1, 16, 7, 26],
              [2, 1, 15, 9, 23],
              [2, 1, 16, 9, 22],
              [0, 1, 20, 7, 22],
              [2, 2, 14, 11, 21],
              [0, 2, 6, 19, 23],
              [2, 0, 8, 16, 24],
              [1, 0, 8, 15, 26],
              [1, 0, 20, 5, 24],
              [0, 3, 15, 9, 23],
              [0, 3, 16, 9, 22],
              [1, 0, 16, 12, 21],
              [1, 3, 14, 11, 21],
              [1, 3, 10, 14, 22],
              [0, 2, 7, 19, 22],
              [1, 1, 14, 9, 25],
              [1, 2, 10, 13, 24],
              [0, 0, 5, 18, 27],
              [0, 2, 14, 9, 25],
              [1, 1, 17, 10, 21],
              [0, 0, 2, 22, 26],
              [0, 2, 17, 10, 21],
              [1, 2, 8, 17, 22],
              [1, 0, 12, 16, 21],
              [2, 0, 15, 12, 21],
              [0, 1, 19, 5, 25],
              [0, 1, 17, 11, 21],
              [0, 2, 17, 7, 24],
              [2, 2, 13, 11, 22],
              [0, 1, 4, 21, 24],
              [0, 0, 23, 4, 23],
              [1, 1, 17, 7, 24],
              [1, 2, 12, 11, 24],
              [2, 0, 17, 8, 23],
              [1, 2, 16, 10, 21],
              [2, 2, 11, 14, 21],
              [2, 0, 12, 15, 21],
              [2, 0, 17, 9, 22],
              [1, 2, 8, 16, 23],
              [1, 3, 13, 11, 22],
              [1, 2, 11, 12, 24],
              [2, 1, 9, 15, 23],
              [1, 0, 14, 9, 26],
              [1, 1, 9, 14, 25],
              [1, 0, 15, 13, 21],
              [0, 0, 7, 21, 22],
              [2, 2, 11, 13, 22],
              [0, 3, 10, 16, 21],
              [2, 1, 9, 16, 22],
              [0, 2, 18, 7, 23],
              [1, 0, 13, 15, 21],
              [0, 0, 2, 24, 24],
              [2, 1, 15, 11, 21],
              [1, 0, 20, 6, 23],
              [1, 1, 18, 7, 23],
              [0, 0, 17, 6, 27],
              [0, 1, 7, 16, 26],
              [1, 3, 11, 14, 21],
              [1, 0, 5, 20, 24],
              [2, 0, 14, 13, 21],
              [2, 2, 13, 12, 21],
              [0, 2, 18, 8, 22],
              [1, 1, 18, 8, 22],
              [1, 0, 9, 14, 26],
              [2, 2, 12, 12, 22],
              [0, 0, 23, 2, 25],
              [1, 0, 14, 14, 21],
              [2, 0, 13, 14, 21],
              [0, 2, 9, 14, 25],
              [1, 0, 19, 8, 22],
              [2, 0, 8, 17, 23],
              [1, 3, 11, 13, 22],
              [2, 0, 9, 17, 22],
              [1, 1, 10, 17, 21],
              [0, 1, 11, 17, 21],
              [2, 2, 12, 13, 21],
              [1, 0, 18, 6, 25],
              [0, 3, 15, 11, 21],
              [1, 3, 13, 12, 21],
              [1, 3, 12, 12, 22],
              [1, 1, 13, 10, 25],
              [0, 1, 5, 21, 23],
              [2, 0, 15, 9, 24],
              [0, 2, 13, 10, 25],
              [0, 0, 21, 3, 26],
              [0, 1, 15, 8, 26],
              [2, 1, 11, 15, 21],
              [0, 0, 6, 17, 27],
              [1, 0, 13, 10, 26],
              [1, 2, 16, 9, 22],
              [1, 3, 12, 13, 21],
              [0, 3, 9, 15, 23],
              [0, 1, 20, 5, 24],
              [0, 1, 16, 12, 21],
              [1, 2, 15, 9, 23],
              [0, 0, 4, 23, 23],
              [1, 1, 10, 13, 25],
              [0, 1, 7, 20, 22],
              [1, 1, 7, 17, 24],
              [1, 0, 10, 13, 26],
              [2, 1, 14, 10, 23],
              [0, 0, 20, 8, 22],
              [0, 2, 10, 17, 21],
              [2, 0, 9, 15, 24],
              [1, 2, 10, 16, 21],
              [1, 0, 6, 20, 23],
              [1, 0, 8, 19, 22],
              [0, 3, 9, 16, 22],
              [0, 2, 10, 13, 25],
              [1, 1, 12, 11, 25],
              [0, 3, 14, 10, 23],
              [1, 0, 12, 11, 26],
              [1, 0, 6, 18, 25],
              [1, 0, 11, 12, 26],
              [1, 1, 11, 12, 25],
              [0, 1, 5, 19, 25],
              [0, 2, 12, 11, 25],
              [1, 1, 16, 11, 21],
              [2, 1, 14, 12, 21],
              [0, 1, 12, 16, 21],
              [0, 0, 16, 7, 27],
              [2, 1, 15, 10, 22],
              [0, 2, 16, 11, 21],
              [0, 2, 11, 12, 25],
              [2, 1, 10, 14, 23],
              [0, 2, 7, 17, 24],
              [0, 1, 8, 15, 26],
              [0, 0, 2, 23, 25],
              [1, 1, 7, 18, 23],
              [0, 3, 11, 15, 21],
              [0, 0, 23, 3, 24],
              [1, 1, 8, 18, 22],
              [0, 3, 15, 10, 22],
              [0, 1, 15, 13, 21],
              [0, 1, 20, 6, 23],
              [2, 1, 12, 14, 21],
              [0, 0, 3, 21, 26],
              [0, 0, 8, 20, 22],
              [1, 2, 15, 11, 21],
              [0, 1, 19, 8, 22],
              [0, 3, 14, 12, 21],
              [2, 0, 16, 10, 22],
              [2, 1, 13, 13, 21],
              [0, 0, 7, 16, 27],
              [0, 1, 13, 15, 21],
              [0, 1, 14, 9, 26],
              [0, 1, 14, 14, 21],
              [2, 0, 14, 10, 24],
              [2, 0, 16, 9, 23],
              [1, 1, 11, 16, 21],
              [1, 2, 9, 15, 23],
              [2, 1, 10, 15, 22],
              [1, 0, 19, 6, 24],
              [2, 1, 13, 11, 23],
              [0, 2, 16, 8, 24],
              [1, 1, 16, 8, 24],
              [1, 2, 9, 16, 22],
              [0, 0, 22, 5, 23],
              [0, 1, 18, 6, 25],
              [0, 3, 10, 14, 23],
              [0, 2, 7, 18, 23],
              [2, 0, 10, 14, 24],
              [0, 2, 8, 18, 22],
              [2, 0, 10, 16, 22],
              [2, 1, 11, 13, 23],
              [0, 0, 15, 8, 27],
              [0, 3, 12, 14, 21],
              [0, 3, 13, 11, 23],
              [2, 0, 9, 16, 23],
              [0, 3, 13, 13, 21],
              [0, 1, 9, 14, 26],
              [0, 2, 11, 16, 21],
              [1, 0, 18, 9, 22],
              [0, 0, 19, 9, 22],
              [2, 1, 12, 12, 23],
              [1, 2, 11, 15, 21],
              [1, 1, 15, 12, 21],
              [1, 0, 17, 7, 25],
              [0, 1, 5, 20, 24],
              [0, 1, 13, 10, 26],
              [1, 2, 14, 10, 23],
              [0, 0, 8, 15, 27],
              [0, 0, 20, 4, 26],
              [0, 2, 15, 12, 21],
              [0, 0, 3, 23, 24],
              [2, 0, 13, 11, 24],
              [0, 0, 22, 3, 25],
              [1, 0, 19, 7, 23],
              [1, 0, 6, 19, 24],
              [2, 1, 14, 11, 22],
              [1, 1, 17, 9, 22],
              [0, 3, 10, 15, 22],
              [0, 2, 17, 9, 22],
              [0, 3, 11, 13, 23],
              [2, 0, 11, 13, 24],
              [0, 2, 17, 8, 23],
              [1, 1, 17, 8, 23],
              [1, 1, 12, 15, 21],
              [0, 3, 12, 12, 23],
              [1, 2, 15, 10, 22],
              [1, 2, 14, 12, 21],
              [0, 1, 10, 13, 26],
              [0, 0, 14, 9, 27],
              [1, 1, 8, 16, 24],
              [1, 0, 9, 18, 22],
              [2, 0, 12, 12, 24],
              [0, 1, 12, 11, 26],
              [0, 0, 9, 19, 22],
              [1, 0, 7, 17, 25],
              [0, 3, 14, 11, 22],
              [0, 0, 5, 22, 23],
              [0, 1, 8, 19, 22],
              [2, 1, 11, 14, 22],
              [0, 1, 11, 12, 26],
              [1, 1, 14, 13, 21],
              [2, 0, 15, 11, 22],
              [0, 0, 9, 14, 27],
              [0, 1, 6, 20, 23],
              [0, 2, 12, 15, 21],
              [1, 2, 12, 14, 21],
              [1, 1, 13, 14, 21],
              [1, 2, 10, 14, 23],
              [0, 2, 14, 13, 21],
              [0, 1, 6, 18, 25],
              [0, 2, 8, 16, 24],
              [1, 2, 13, 13, 21],
              [2, 0, 11, 15, 22],
              [0, 1, 19, 6, 24],
              [0, 0, 13, 10, 27],
              [1, 0, 7, 19, 23],
              [2, 0, 15, 10, 23],
              [0, 0, 4, 20, 26],
              [2, 1, 13, 12, 22],
              [0, 2, 13, 14, 21],
              [0, 0, 10, 13, 27],
              [2, 1, 12, 13, 22],
              [0, 0, 18, 10, 22],
              [0, 0, 12, 11, 27],
              [1, 2, 13, 11, 23],
              [1, 1, 9, 17, 22],
              [0, 0, 3, 22, 25],
              [0, 0, 11, 12, 27],
              [0, 1, 18, 9, 22],
              [2, 0, 10, 15, 23],
              [1, 2, 10, 15, 22],
              [0, 3, 11, 14, 22],
              [1, 1, 15, 9, 24],
              [0, 2, 15, 9, 24],
              [0, 0, 22, 4, 24],
              [1, 1, 8, 17, 23],
              [0, 3, 13, 12, 22],
              [2, 0, 14, 12, 22],
              [1, 0, 17, 10, 22],
              [1, 2, 11, 13, 23],
              [0, 1, 17, 7, 25],
              [0, 1, 19, 7, 23],
              [0, 0, 21, 6, 23],
              [1, 0, 16, 8, 25],
              [2, 0, 12, 14, 22],
              [0, 0, 10, 18, 22],
              [1, 2, 12, 12, 23],
              [0, 3, 12, 13, 22],
              [1, 0, 18, 7, 24],
              [0, 2, 9, 17, 22],
              [2, 0, 13, 13, 22],
              [1, 2, 14, 11, 22],
              [0, 0, 19, 5, 26],
              [0, 2, 8, 17, 23],
              [1, 0, 10, 17, 22],
              [1, 1, 9, 15, 24],
              [2, 0, 14, 11, 23],
              [1, 0, 8, 16, 25],
              [0, 0, 17, 11, 22],
              [1, 1, 16, 10, 22],
              [2, 0, 11, 14, 23],
              [0, 2, 16, 10, 22],
              [1, 0, 18, 8, 23],
              [0, 0, 21, 4, 25],
              [1, 0, 7, 18, 24],
              [0, 1, 9, 18, 22],
              [1, 2, 11, 14, 22],
              [0, 0, 4, 22, 24],
              [0, 2, 9, 15, 24],
              [0, 1, 6, 19, 24],
              [1, 1, 16, 9, 23],
              [0, 2, 16, 9, 23],
              [0, 0, 11, 17, 22],
              [0, 0, 6, 21, 23],
              [2, 0, 13, 12, 23],
              [0, 0, 5, 19, 26],
              [2, 0, 12, 13, 23],
              [1, 1, 14, 10, 24],
              [1, 2, 13, 12, 22],
              [0, 1, 7, 17, 25],
              [0, 2, 14, 10, 24],
              [1, 0, 16, 11, 22],
              [0, 0, 16, 12, 22],
              [1, 2, 12, 13, 22],
              [1, 0, 15, 9, 25],
              [1, 1, 10, 16, 22],
              [0, 1, 17, 10, 22],
              [1, 0, 8, 18, 23],
              [0, 1, 7, 19, 23],
              [1, 0, 11, 16, 22],
              [0, 0, 12, 16, 22],
              [1, 1, 10, 14, 24],
              [0, 1, 18, 7, 24],
              [1, 0, 9, 15, 25],
              [0, 1, 16, 8, 25],
              [1, 1, 9, 16, 23],
              [0, 0, 4, 21, 25],
              [0, 0, 15, 13, 22],
              [0, 2, 10, 16, 22],
              [0, 0, 18, 6, 26],
              [0, 0, 13, 15, 22],
              [0, 0, 20, 7, 23],
              [0, 2, 10, 14, 24],
              [0, 0, 14, 14, 22],
              [0, 0, 21, 5, 24],
              [1, 1, 13, 11, 24],
              [1, 0, 17, 8, 24],
              [1, 0, 15, 12, 22],
              [1, 1, 15, 11, 22],
              [0, 2, 13, 11, 24],
              [0, 2, 9, 16, 23],
              [0, 2, 15, 11, 22],
              [1, 1, 11, 13, 24],
              [0, 1, 18, 8, 23],
              [1, 0, 12, 15, 22],
              [0, 1, 10, 17, 22],
              [1, 0, 14, 10, 25],
              [1, 1, 12, 12, 24],
              [0, 2, 11, 13, 24],
              [0, 0, 6, 18, 26],
              [1, 0, 14, 13, 22],
              [0, 2, 12, 12, 24],
              [1, 1, 15, 10, 23],
              [1, 0, 10, 14, 25],
              [1, 1, 11, 15, 22],
              [1, 0, 17, 9, 23],
              [1, 0, 13, 14, 22],
              [1, 0, 8, 17, 24],
              [0, 2, 15, 10, 23],
              [0, 1, 8, 16, 25],
              [0, 0, 7, 20, 23],
              [0, 1, 16, 11, 22],
              [0, 0, 20, 5, 25],
              [0, 0, 5, 21, 24],
              [1, 0, 13, 11, 25],
              [0, 2, 11, 15, 22],
              [0, 1, 7, 18, 24],
              [1, 1, 14, 12, 22],
              [1, 0, 11, 13, 25],
              [0, 1, 15, 9, 25],
              [1, 0, 9, 17, 23],
              [1, 1, 10, 15, 23],
              [1, 0, 12, 12, 25],
              [0, 2, 14, 12, 22],
              [0, 0, 17, 7, 26],
              [1, 1, 12, 14, 22],
              [0, 1, 11, 16, 22],
              [1, 1, 13, 13, 22],
              [0, 1, 8, 18, 23],
              [0, 0, 19, 8, 23],
              [0, 2, 10, 15, 23],
              [0, 2, 12, 14, 22],
              [0, 0, 5, 20, 25],
              [1, 0, 16, 9, 24],
              [0, 1, 15, 12, 22],
              [0, 2, 13, 13, 22],
              [0, 1, 17, 8, 24],
              [1, 1, 14, 11, 23],
              [0, 0, 7, 17, 26],
              [0, 1, 9, 15, 25],
              [0, 2, 14, 11, 23],
              [0, 0, 20, 6, 24],
              [0, 1, 12, 15, 22],
              [1, 0, 16, 10, 23],
              [1, 0, 9, 16, 24],
              [1, 1, 11, 14, 23],
              [0, 1, 14, 10, 25],
              [0, 1, 17, 9, 23],
              [0, 1, 14, 13, 22],
              [0, 0, 8, 19, 23],
              [0, 1, 13, 14, 22],
              [0, 0, 16, 8, 26],
              [1, 1, 13, 12, 23],
              [0, 2, 11, 14, 23],
              [1, 0, 10, 16, 23],
              [1, 1, 12, 13, 23],
              [0, 0, 19, 6, 25],
              [0, 2, 13, 12, 23],
              [0, 1, 10, 14, 25],
              [0, 2, 12, 13, 23],
              [0, 1, 8, 17, 24],
              [0, 0, 6, 20, 24],
              [0, 0, 8, 16, 26],
              [0, 1, 13, 11, 25],
              [1, 0, 15, 10, 24],
              [0, 0, 18, 9, 23],
              [0, 1, 11, 13, 25],
              [0, 1, 12, 12, 25],
              [1, 0, 15, 11, 23],
              [0, 1, 9, 17, 23],
              [1, 0, 10, 15, 24],
              [0, 0, 15, 9, 26],
              [0, 0, 6, 19, 25],
              [0, 1, 16, 9, 24],
              [1, 0, 11, 15, 23],
              [0, 0, 9, 18, 23],
              [0, 0, 9, 15, 26],
              [0, 0, 19, 7, 24],
              [0, 1, 16, 10, 23],
              [1, 0, 14, 11, 24],
              [1, 0, 14, 12, 23],
              [0, 0, 14, 10, 26],
              [1, 0, 11, 14, 24],
              [1, 0, 12, 14, 23],
              [0, 0, 17, 10, 23],
              [1, 0, 13, 13, 23],
              [0, 0, 18, 7, 25],
              [0, 0, 10, 14, 26],
              [1, 0, 13, 12, 24],
              [0, 1, 9, 16, 24],
              [1, 0, 12, 13, 24],
              [0, 0, 13, 11, 26],
              [0, 0, 7, 19, 24],
              [0, 0, 11, 13, 26],
              [0, 1, 10, 16, 23],
              [0, 0, 12, 12, 26],
              [0, 0, 10, 17, 23],
              [0, 1, 15, 10, 24],
              [0, 0, 7, 18, 25],
              [0, 1, 15, 11, 23],
              [0, 0, 16, 11, 23],
              [0, 0, 18, 8, 24],
              [0, 1, 10, 15, 24],
              [0, 0, 11, 16, 23],
              [0, 1, 11, 15, 23],
              [0, 0, 17, 8, 25],
              [0, 1, 14, 11, 24],
              [0, 0, 15, 12, 23],
              [0, 1, 14, 12, 23],
              [0, 0, 12, 15, 23],
              [0, 0, 8, 18, 24],
              [0, 1, 12, 14, 23],
              [0, 0, 14, 13, 23],
              [0, 1, 13, 13, 23],
              [0, 1, 11, 14, 24],
              [0, 0, 13, 14, 23],
              [0, 0, 8, 17, 25],
              [0, 1, 13, 12, 24],
              [0, 1, 12, 13, 24],
              [0, 0, 17, 9, 24],
              [0, 0, 16, 9, 25],
              [0, 0, 9, 17, 24],
              [0, 0, 9, 16, 25],
              [0, 0, 15, 10, 25],
              [0, 0, 16, 10, 24],
              [0, 0, 10, 15, 25],
              [0, 0, 10, 16, 24],
              [0, 0, 14, 11, 25],
              [0, 0, 11, 14, 25],
              [0, 0, 15, 11, 24],
              [0, 0, 13, 12, 25],
              [0, 0, 12, 13, 25],
              [0, 0, 11, 15, 24],
              [0, 0, 14, 12, 24],
              [0, 0, 12, 14, 24],
              [0, 0, 13, 13, 24]])