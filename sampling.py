__author__ = 'ohgushimasaya'

from numpy import *
from numpy.random import *
import numpy
import random
from Add_Count import add_count
import os.path

class Sampling:

    def __init__(self, xcourps, ycourps):
        self.iteration = 100000
        self.xcourps = xcourps
        self.ycourps = ycourps

    def sampling(self, TOPICS, xcounts, ycounts, docId):

        for i in range(0, self.iteration):
            Sampling.sampler(self.xcourps, self.ycourps, i, TOPICS, xcounts, ycounts, docId)

    @staticmethod
    def sampler(xcourps, ycourps, i, TOPICS, xcounts, ycounts, docId):
        ll = 0
        adder = add_count(xcounts, ycounts)
        probs = []
        for i in range(0, len(xcourps)):
            for j in range(0, len(xcourps[i])):
                x = xcourps[i][j]
                y = ycourps[i][j]
                adder.add_counter(x, y, i, -1)
                for k in range(TOPICS):
                    if xcounts.has_key(k) and (x, k) in xcounts  and ycounts.has_key(docId) \
                    and (y, docId) in ycounts:
                        if xcounts[k] != 0 and ycounts[docId] != 0:
                           p_x_y = 1.0 * xcounts[(x, k)] / xcounts[k]
                           p_y_Y = 1.0 * ycounts[(y, docId)] / ycounts[docId]
                           probs.append(p_x_y * p_y_Y)
            new_y = Sampling.sampleOne(probs)
            ll = ll + log(probs[new_y])
            adder.add_counter(x, new_y, i ,1)
            ycourps[i][j] = new_y
        print ll

    @staticmethod
    def sampleOne(probs):
        z = sum(probs)
        remaining = random.uniform(0, z)
        for i in range(len(probs)):
            remaining = remaining - probs[i]
            if remaining <= 0:
                return i
