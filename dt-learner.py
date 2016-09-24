import ARFF
import sys
import cmath as math

classification_index = 0
pos_classification = ""
neg_classification = ""
input_file = object()


def main(argv):
    input_fname = argv[0]
    output_fname = argv[1]
    criterion = argv[2]

    input_file = ARFF.ARFF(input_fname)
    classification_index = len(input_file.attributes) - 1
    pos_classification = input_file.attributes[classification_index].value[0]
    neg_classification = input_file.attributes[classification_index].value[1]

    '''print input_file'''

def cal_entropy(set):
    pos_res = 0
    neg_res = 0

    for element in set:
        if element[classification_index] is pos_classification:
            pos_res = pos_res + 1
    if pos_res is 0 or neg_res is 0:
        return 0
    prob = pos_res / len(set)
    return -(prob * math.log(prob, 2) + (1 - prob) * math.log(1 - prob, 2))


def grow_tree(set, node):

def split_set(set, attr_name):
    possible_vals = []
    for attr in input_file.attributes:
        if attr.name is attr_name:
            possible_vals = attr.value()
    branches = range(len(possible_vals))
    for element in set:




if __name__ == "__main__":
    main(sys.argv[1:])