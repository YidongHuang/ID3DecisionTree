import ARFF
import sys
import tree as dtree

def main(argv):
    input_fname = argv[0]
    output_fname = argv[1]
    criterion = argv[2]

    tree = dtree.Tree(input_fname)


if __name__ == "__main__":
    main(sys.argv[1:])