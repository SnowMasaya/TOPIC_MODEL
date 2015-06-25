__author__ = 'ohgushimasaya'
from numpy import *
from numpy.random import *
import numpy
import os.path

class Sampling_one:

    def __init__(self, probs):
        self.probs = probs

    def sampleOne(self):
        z = sum(self.probs)
        remaining = rand(z)
        for i in range(len(self.probs) - 1):
            remaining = remaining - self.probs[i]
            if remaining <= 0:
                return i
