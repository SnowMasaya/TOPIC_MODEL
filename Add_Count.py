__author__ = 'ohgushimasaya'

class add_count:

    def __init__(self, xcounts, ycoutns):
        self.xcounts = xcounts
        self.ycounts = ycoutns

    def add_counter(self, word, topic, docid, amount):
        #Word
        self.xcounts = add_count.check_dict(topic, self.xcounts, amount)
        self.xcounts = add_count.check_dict((word, topic), self.xcounts, amount)

        #TOPIC
        self.ycounts = add_count.check_dict(docid, self.ycounts, amount)
        self.ycounts = add_count.check_dict((topic, docid), self.ycounts, amount)

    @staticmethod
    def check_dict(key, w_t_count, amount):
        if w_t_count.has_key(key):
            w_t_count.update({key:w_t_count[key] + amount})
            return w_t_count
        else:
            w_t_count[key] = 1
            return w_t_count
