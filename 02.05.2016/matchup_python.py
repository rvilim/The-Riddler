import numpy as np

def matchup(strategy, competitors):
    winpoints = np.sum(strategy > competitors, axis=1)
    losspoints = np.sum(strategy < competitors, axis=1)

    win = winpoints > losspoints
    loss = winpoints < losspoints

    return win, loss