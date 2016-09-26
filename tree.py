import ARFF
import math as math
import numpy as np
import tree_node

class Tree:
    def __init__(self, fname, criterion):
        self._dtree = ARFF.ARFF(fname)
        self._classification_index = len(self._dtree.attributes) - 1
        self._pos_classification = self._dtree.attributes[self._classification_index].value[0]
        self._neg_classification = self._dtree.attributes[self._classification_index].value[1]
        self._criterion = int(criterion)
        self.clean_up()
        self.test()

    def test(self):
        node = tree_node.Tree_node()
        node.available_attr_index = range(len(self._dtree.attributes) - 1)
        self.fill_split_condition(node, self._dtree.data)
        node.print_tree("")

    def cal_entropy(self, set):
        pos_res = 0
        for element in set:
            if element[self._classification_index] == self._pos_classification:
                pos_res = pos_res + 1
        neg_res = len(set) - pos_res
        if pos_res == 0 or pos_res == len(set):
            return [0, pos_res, neg_res]
        prob = pos_res*1.0 /len(set)
        entropy = -(prob * math.log(prob, 2) + (1 - prob) * math.log(1 - prob, 2))
        return [entropy, pos_res, neg_res]

    '''return list of the sets based on the index of the attr to split'''
    def split_set(self, set, index, numeric):
        if self._dtree.attributes[index].nominal is True:
            possible_vals = self._dtree.attributes[index].value
            '''initialize empty result_sets'''
            result_sets = [None] * len(possible_vals)
            for i in range(len(result_sets)):
                result_sets[i] = []

            '''mapping attr values to buckets in result_sets'''
            dict = {}
            for i in range(len(possible_vals)):
                dict[possible_vals[i]] = i
            for element in set:
                result_sets[dict.get(element[index])].append(element)
            return result_sets
        else:
            result_sets = [[],[]]
            for element in set:
                if element[index] <= numeric:
                    result_sets[0].append(element)
                else:
                    result_sets[1].append(element)
            return result_sets

    def fill_split_condition(self, node, set):
        common_class = self.get_common_class(set)
        avail_attr_index = node.available_attr_index
        max_info_gain = 0
        divided_result_sets = []
        divided_entropy_list = []
        divided_dist_result = []
        divided_index = 0
        for index in avail_attr_index:
            if self._dtree.attributes[index].nominal is True:
                result_sets = self.split_set(set, index, 0)
                entropy_dist_list = self.get_entropy_list(result_sets)
                info_gain = self.get_info_gain(set, entropy_dist_list[0], result_sets, node)
                if max_info_gain < info_gain:
                    node.name = self._dtree.attributes[index].name
                    max_info_gain = info_gain
                    divided_entropy_list = entropy_dist_list[0]
                    divided_result_sets = result_sets
                    divided_dist_result = entropy_dist_list[1]
                    divided_index = index
            else:
                mid_points = self.get_midpoints(set, index)
                for mid_point in mid_points:
                    result_sets = self.split_set(set, index, mid_point)
                    entropy_dist_list = self.get_entropy_list(result_sets)
                    info_gain = self.get_info_gain(set, entropy_dist_list[0], result_sets, node)
                    if max_info_gain < info_gain or(max_info_gain == info_gain and index == divided_index and mid_point < node.threshold):
                        node.name = self._dtree.attributes[index].name
                        max_info_gain = info_gain
                        node.threshold = mid_point
                        divided_entropy_list = entropy_dist_list[0]
                        divided_result_sets = result_sets
                        divided_dist_result = entropy_dist_list[1]
                        divided_index = index

        '''Check if this node should be ended'''
        if max_info_gain == 0 or len(node.available_attr_index) == 0:
            node.result = common_class
            node.append_condition(": {}".format(common_class))
            return
        '''Remove entry from attr index for children'''
        children_avail_attr_index = node.available_attr_index[:]
        for i in range(len(children_avail_attr_index)):
            if self._dtree.attributes[node.available_attr_index[i]] == node.name:
                if self._dtree.attributes[node.available_attr_index[i]].nominal is True:
                    to_remove = children_avail_attr_index[i]
                    children_avail_attr_index.remove(to_remove)
                break

        '''Make children nodes'''
        node.children = self.make_children(divided_entropy_list, common_class, children_avail_attr_index, divided_index, divided_dist_result)
        grow_index = self.growing_index(divided_result_sets, node)
        for i in grow_index:
            self.fill_split_condition(node.children[i], divided_result_sets[i])
        return

    def get_midpoints(self, data_list, index):
        all_vals = []
        mid_points = []
        for element in data_list:
            all_vals.append(element[index])
        all_vals = list(set(all_vals))
        all_vals.sort(key=float)
        for i in range(len(all_vals) - 1):
            mid_points.append(all_vals[i] * 1.0 / 2 + all_vals[i + 1] * 1.0 / 2)
        return mid_points

    def get_entropy_list(self, result_sets):
        dist_list = []
        entropy_list = []
        for result_set in result_sets:
            entropy_dist_list = self.cal_entropy(result_set)
            entropy_list.append(entropy_dist_list[0])
            dist_list.append([entropy_dist_list[1], entropy_dist_list[2]])
        return [entropy_list, dist_list]

    def get_info_gain(self, set, entropy_list, result_sets, node):
        entropy = 0
        for i in range(len(result_sets)):
            entropy = entropy + len(result_sets[i]) * 1.0 / len(set) * entropy_list[i]
        return node.entropy - entropy

    def make_children(self, entropy_list, parent_common_class, avail_list, index, divided_dist_result):
        children = []
        child_avail_attr_index = avail_list[:]
        for i in range(len(entropy_list)):
            node = tree_node.Tree_node()
            node.entropy = entropy_list[i]
            node.parent_common_class = parent_common_class
            node.available_attr_index = child_avail_attr_index
            self.fill_condition(node, index, i, divided_dist_result)
            children.append(node)
        return children

    def get_common_class(self, set):
        pos_res = 0
        for element in set:
            if element[self._classification_index] == self._pos_classification:
                pos_res = pos_res + 1
        if pos_res * 2 >= len(set):
            return self._pos_classification
        return self._neg_classification

    def growing_index(self, divided_result_sets, node):
        more_split = []
        for i in range(len(divided_result_sets)):
            '''print node.name'''
            if node.children[i].entropy == 0 or len(divided_result_sets[i]) < self._criterion:
                node.children[i].name = self.get_common_class(divided_result_sets[i])
            else:
                more_split.append(i)
        return more_split

    def fill_condition(self, node, index, i, divided_dist_result):
        node.result = " = {} {}".format(self._dtree.attributes[index].name, divided_dist_result[i])


    def clean_up(self):
        for attr in self._dtree.attributes:
            if attr.nominal is not True:
                attr.value_setter(list(set(attr.value)))
                attr.value.sort(key=float)
                mid_points = []
                for i in range(len(attr.value) - 1):
                    mid_points.append(attr.value[i] * 1.0/2 + attr.value[i + 1] * 1.0/2)
                attr.value_setter(mid_points)



