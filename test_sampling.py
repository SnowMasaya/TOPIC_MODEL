from unittest import TestCase
from Add_Count import add_count
from sampling import Sampling
from initilaze_topic_model import initilaze_topic_model

__author__ = 'ohgushimasaya'


class Testsampling(TestCase):

    def setUp(self):
        print "test"

    def test_sampling(self):
        init = initilaze_topic_model()
        init.initilize()
        sampleman = Sampling(init.xcorpus, init.ycorpus)
        sampleman.sampling(init.TOPICS, init.xcounts, init.ycounts, init.docid)
        print sampleman.xcourps
        print sampleman.ycourps

if __name__ == "__main__":
    TestCase.main()
