from unittest import TestCase
from sampling_one import Sampling_one

class TestSampling_one(TestCase):
    def setUp(self):
        print "test"

    def test_add(self):
        sampler_one = Sampling_one([0.5, 0.2])
        print sampler_one.sampleOne()

if __name__ == "__main__":
    TestCase.main()
