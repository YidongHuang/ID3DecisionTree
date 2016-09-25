import ARFF
import cmath as math
import numpy as np

class Tree:
    def __init__(self, fname):
        self._dtree = ARFF.ARFF(fname)
        self._classification_index = len(self._dtree.attributes) - 1
        self._pos_classification = self._dtree.attributes[self._classification_index].value[0]
        self._neg_classification = self._dtree.attributes[self._classification_index].value[1]
        self.clean_up()
        self.test()

    def test(self):
        self.fill_split_condition(self, node, self._dtree)

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
    def split_set(self, set, index, numeric):
        if self._dtree.attributes[index].nominal == True:
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
        else:
            result_sets = [[],[]]
            for element in set.data:
                if element[index] <= numeric:
                    result_sets[0].append(element)
                else:
                    result_sets[1].append(element)
            return result_sets


    def fill_split_condition(self, node, set):
        avail_attr_index = node.available_attr_index
        for index in avail_attr_index:
            if self._dtree.attributes[index].nominal == True:
                result_sets = self.split_sets(set, self._dtree.attributes[index], 0)
                entropy = []
                for result_set in result_sets:
                    entropy.append(self.cal_entropy(result_set))
                index_min = np.argmin(entropy)
                if entropy[index_min] < node.entropy:
                    node.name = self._dtree.attributes[index].name
                    node.entropy = entropy[index_min]
            else:
                mid_points = self._dtree.attributes[index].value
                for mid_point in mid_points:
                    result_sets = self.split_set(set, self._dtree.attributes[index], mid_point)
                    entropy = []
                    for result_set in result_sets:
                        entropy.append(self.cal_entropy(result_set))
                    index_min = np.argmin(entropy)
                    if entropy[index_min] < node.entropy:
                        node.name = self._dtree.attributes[index].name
                        node.entropy = entropy[index_min]
                        node.threshold = mid_point
        to_remove = 0
        for i in range(len(node.available_attr_index)):
            if self._dtree.attributes[node.available_attr_index[i]] == node.name:
                if self._dtree.attributes[node.available_attr_index[i]].nominal is True:
                    to_remove = node.available_attr_index[i]
                break
        node.available_attr_index.remove(to_remove)


    def clean_up(self):
        for attr in self._dtree.attributes:
            if attr.nominal is not True:
                attr.value_setter(list(set(attr.value)))
                attr.value.sort(key=float)
                mid_points = []
                for i in range(len(attr.value) - 1):
                    mid_points.append(attr.value[i] * 1.0/2 + attr.value[i + 1] * 1.0/2)
                attr.value_setter(mid_points)
