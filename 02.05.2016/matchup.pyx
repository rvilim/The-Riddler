#!python
#cython: boundscheck=False, wraparound=False, nonecheck=False, overflowcheck=False
import numpy as np
cimport numpy as np
cimport cython
# from cython.parallel import prange

@cython.boundscheck(False)
@cython.wraparound(False)
def matchup(np.ndarray[np.int_t, ndim=1, negative_indices=False] strategy,
            np.ndarray[np.int_t, ndim=2, negative_indices=False] competitors,
            np.ndarray[np.int_t, ndim=1, negative_indices=False] points):

    cdef np.int_t n_competitors = competitors.shape[0]
    cdef np.int_t n_castles = strategy.shape[0]

    cdef np.ndarray[np.int_t, ndim=1,negative_indices=False] winpoints = np.zeros(n_competitors, dtype=np.int)
    cdef np.ndarray[np.int_t, ndim=1,negative_indices=False] losspoints = np.zeros(n_competitors, dtype=np.int)

    cdef np.ndarray[np.int_t, ndim=1,negative_indices=False] win = np.zeros(n_competitors, dtype=np.int)
    cdef np.ndarray[np.int_t, ndim=1,negative_indices=False] loss = np.zeros(n_competitors, dtype=np.int)

    # Loop over all the competitors, compare them to the current strategy and find out who wins
    for i in range(n_competitors):
        for j in range(n_castles):

            if(strategy[j]>competitors[i,j]):
                winpoints[i]+=points[j]

            if(strategy[j]<competitors[i,j]):
                losspoints[i]+=points[j]

        if winpoints[i]>losspoints[i]:
            win[i]=1

        if winpoints[i]<losspoints[i]:
            loss[i]=1

    return win, loss