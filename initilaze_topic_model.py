#-*- coding:utf-8 -*-
__author__ = 'ohgushimasaya'

from numpy import *
from numpy.random import *
import numpy
from Add_Count import add_count
import os.path

class initilaze_topic_model:

    def __init__(self):
        self.xcorpus = numpy.array([])
        self.ycorpus = numpy.array([])
        self.xcounts = {}
        self.ycounts = {}
        self.topics_vector = numpy.array([])
        self.TOPICS = 7
        self.docid = 1

    def initilize(self):
        first_time = 1
        adder = add_count(self.xcounts, self.ycounts)
        self.docid = os.path.getsize("07-train.txt")
        #for line in open("wiki-en-documents.word", "r"):
        for line in open("07-train.txt", "r"):
            rline = line.rstrip("¥n")
            words = numpy.array(rline.split(" "))
            topics_vector = []
            for word in words:
                topic = randint(self.TOPICS) + 1
                topics_vector.append(topic)
                adder.add_counter(word, topic, self.docid,  1)
            array_topics_vector = numpy.array(topics_vector)
            if first_time == 1:
                self.xcorpus = numpy.hstack((self.xcorpus, words))
                self.ycorpus = numpy.hstack((self.ycorpus, array_topics_vector))
                first_time = first_time + 1
            else:
                self.xcorpus = numpy.vstack((self.xcorpus, words))
                self.ycorpus = numpy.vstack((self.ycorpus, array_topics_vector))
