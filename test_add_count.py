from unittest import TestCase
from Add_Count import add_count

__author__ = 'ohgushimasaya'


class TestInitilaze_topic_model(TestCase):

    def setUp(self):
        print "test"

    def test_add(self):
        adder = add_count()

if __name__ == "__main__":
    TestCase.main()
