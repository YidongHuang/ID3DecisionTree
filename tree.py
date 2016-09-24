import ARFF
import cmath as math

class Tree:
    def __init__(self, fname):
        self._dtree = ARFF.ARFF(fname)
        self._classification_index = len(self._dtree.attributes) - 1
        self._pos_classification = self._dtree.attributes[self._classification_index].value[0]
        self._neg_classification = self._dtree.attributes[self._classification_index].value[1]
        self.clean_up()
        self.test()

    def test(self):
        print self.split_set(self._dtree, 0)

    def cal_entropy(self, set):
        pos_res = 0
        for element in set.data:
            if element[self._classification_index] == self._pos_classification:
                pos_res = pos_res + 1
        if pos_res == 0 or pos_res == len(set.data):
            return 0
        prob = pos_res * 1.0 / len(set.data)
        return -(prob * math.log(prob, 2) + (1 - prob) * math.log(1 - prob, 2))

    '''return list of the sets based on the index of the attr to split'''
    def split_set(self, set, index):
        possible_vals = self._dtree.attributes[index].value

        '''initialize empty result_sets'''
        result_sets = [None] * (len(possible_vals))
        for i in range(len(result_sets)):
            result_sets[i] = []

        '''mapping attr values to buckets in result_sets'''
        dict = {}
        for i in range(len(possible_vals)):
            dict[possible_vals[i]] = i

        for element in set.data:
            result_sets[dict.get(element[index])].append(element)
        return result_sets

    def split(self, node, set):


    def clean_up(self):
        for attr in self._dtree.attributes:
            if attr.nominal is not True:
                attr.value_setter(list(set(attr.value)))
                attr.value.sort(key=float)