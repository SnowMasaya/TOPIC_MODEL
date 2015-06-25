from unittest import TestCase
from initilaze_topic_model import initilaze_topic_model

__author__ = 'ohgushimasaya'


class TestInitilaze_topic_model(TestCase):

    def setUp(self):
        print "test"

    def test_add(self):
        init = initilaze_topic_model()
        print init.initilize()
        print init.xcounts
        print init.ycounts
        print init.xcorpus
        print init.ycorpus

if __name__ == "__main__":
    TestCase.main()