__author__ = 'ohgushimasaya'

from numpy import *
from numpy.random import *
import numpy
import random
from Add_Count import add_count
import os.path

class Sampling:

    def __init__(self, xcorpus, ycorpus):
        self.iteration = 1000
        self.xcorpus = xcorpus
        self.ycorpus = ycorpus
        self.alpha = 0.01
        self.beta = 0.03

    def sampling(self, TOPICS, xcounts, ycounts, docId, different_word):

        for i in range(0, self.iteration):
            Sampling.sampler(self, i, TOPICS, xcounts, ycounts, docId, different_word)

    @staticmethod
    #def sampler(xcorpus, ycorpus, i, TOPICS, xcounts, ycounts, docId, different_word):
    def sampler(self, i, TOPICS, xcounts, ycounts, docId, different_word):
        ll = 0
        adder = add_count(xcounts, ycounts)
        probs = {}
        for i in range(0, len(self.xcorpus)):
            for j in range(0, len(self.xcorpus[i])):
                x = self.xcorpus[i][j]
                y = self.ycorpus[i][j]
                adder.add_counter(x, y, i, -1)
                for k in range(TOPICS):
                    if xcounts.has_key(k) and (x, k) in xcounts  and ycounts.has_key(docId) \
                    and (y, docId) in ycounts:
                        if xcounts[k] != 0 and ycounts[docId] != 0:
                           p_x_y = 1.0 * xcounts[(x, k)] + self.alpha / xcounts[k] + self.alpha * len(different_word)
                           p_y_Y = 1.0 * ycounts[(y, docId)] + self.beta / ycounts[docId] + self.beta * TOPICS
                           probs.update({k : p_x_y * p_y_Y})
            new_y = Sampling.sampleOne(probs)
            print new_y
            ll = ll + log(probs[new_y])
            adder.add_counter(x, new_y, i ,1)
            self.ycorpus[i][j] = new_y
        print ll

    @staticmethod
    def sampleOne(probs):
        z = 0
        for k, v in probs.items():
            z = z + v
        remaining = random.uniform(0, z)
        for k,v in probs.items():
            remaining = remaining - v
            if remaining <= 0:
                return k
