# encoding=utf8

"""
    Created by Yajun Huang at 2017/02/14
"""

import numpy as np
import sys
from StringIO import StringIO
from gym.envs.toy_text import discrete


class Action(object):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class GridWorld(discrete.DiscreteEnv):
    """
    Grid World environment from Sutton's Reinforcement Learning book chapter 4.
    You are an agent on an MxN grid and your goal is to reach the terminal
    state at the top left or the bottom right corner.
    For example, a 4x4 grid looks as follows:
    T  o  o  o
    o  x  o  o
    o  o  o  o
    o  o  o  T
    x is your position and T are the two terminal states.
    You can take actions in each direction (UP=0, RIGHT=1, DOWN=2, LEFT=3).
    Actions going off the edge leave you in your current state.
    You receive a reward of -1 at each step until you reach a terminal state.
    """

    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self, shape=(4, 4)):
        if not isinstance(shape, (list, tuple)) or not len(shape) == 2:
            raise ValueError('shape argument must be a list/tuple of length 2')

        self.shape = shape

        nA = 4
        nS = np.prod(shape)

        MAX_Y = shape[0]
        MAX_X = shape[1]

        P = {}
        # Initial grid and its iterator
        grid = np.arange(nS).reshape(shape)
        grid_it = np.nditer(grid, flags=['multi_index'])

        is_done = lambda s: s == 0 or s == nS-1

        # Initial state-action transition probabilities
        while not grid_it.finished:
            s = grid_it.iterindex
            y, x = grid_it.multi_index

            P[s] = {a: [] for a in range(nA)}

            reward = 0.0 if is_done(s) else -1.0

            up_next_state = s if y == 0 or is_done else s - MAX_X
            down_next_state = s if y == MAX_Y or is_done else s + MAX_X
            left_next_state = s if x == 0 or is_done else s - 1
            right_next_state = s if x == MAX_X or is_done else s + 1

            P[s][Action.UP] = [(1.0, up_next_state, reward, is_done)]
            P[s][Action.DOWN] = [(1.0, down_next_state, reward, is_done)]
            P[s][Action.LEFT] = [(1.0, left_next_state, reward, is_done)]
            P[s][Action.RIGHT] = [(1.0, right_next_state, reward, is_done)]

            grid_it.next()

        self.P = P

        # Initial state distribution is uniform
        isd = np.ones(nS) / nS
        # ...
        super(GridWorld, self).__init__(nS, nA, P, isd)

    def _render(self, mode='human', close=False):
        if close:
            return

        outfile = StringIO() if mode == 'ansi' else sys.stdout

        grid = np.arange(self.nS).reshape(self.shape)
        grid_it = np.nditer(grid, flags=['multi_index'])

        while not grid_it.finished:
            s = grid_it.iterindex
            y, x = grid_it.multi_index

            if self.s == s:
                output = ' x '
            elif s == 0 or s == self.nS - 1:
                output = ' T '
            else:
                output = ' o '

            if x == 0:
                output = output.lstrip()
            if x == self.shape[1] - 1:
                output = output.rstrip()

            outfile.write(output)

            if x == self.shape[1] - 1:
                outfile.write("\n")

            grid_it.iternext()
