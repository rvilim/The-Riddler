from itertools import combinations, product
import numpy as np
import matchup as matchup_cython
import matchup_python
from timeit import default_timer as timer
import sys
import rejects


def balls_in_boxes(n, m):
    """Generate combinations of n balls in m boxes. Stolen from somewhere on stakc overlflow
    """

    for c in combinations(range(n + m - 1), m - 1):
        yield tuple(b - a - 1 for a, b in zip((-1,) + c, c + (n + m - 1,)))

def score_strategies(strategies, points):
    wins = np.zeros((len(strategies),))

    for n in range(len(strategies)):
        # Calculate this strategy vs fll the strategies that haven't been tried
        resultwin, resultloss = matchup_cython.matchup(strategies[n,:], strategies[n+1:,:],points)

        # Increment the wins counter (note this is a half triangular matrix, so some weirdness here
        wins[n] += np.sum(resultwin)
        wins[n + 1:] += resultloss

    winssort=np.argsort(wins, axis=0)

    for strategy, winnum in zip(strategies[winssort[-500:],:], wins[winssort[-500:]]):
        print strategy, winnum

    return strategies[np.argmax(wins),:]




def filter(strategies, mustbeats, points):
    runningfilter=np.ones(shape=len(strategies), dtype=bool)

    for mustbeat in mustbeats:
        runningfilter = np.logical_and(runningfilter,
                        np.sum(points * (strategies > mustbeat), axis=1) > np.sum(points * (strategies<mustbeat),axis=1)
                        )

    return strategies[runningfilter]

def main():
    s = timer()

    ncastles = int(sys.argv[1])
    nsoldiers = int(sys.argv[2])
    userejects = False
    strategies = np.array(list(balls_in_boxes(nsoldiers, ncastles)),dtype=np.int)


    points=np.arange(ncastles,dtype=np.int)+1

    if((ncastles!=5 or nsoldiers!=50) and userejects):
        raise ValueError("Note: the rejects is tuned for 5, 50. Set userejects=False to run this")

    if userejects:
        strategies=filter(strategies,rejects.rejects(), points)

    score_strategies(strategies,points)
    e = timer()
    print(e - s)

if __name__ == "__main__":
    main()
