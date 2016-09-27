import ARFF
import sys
import tree as dtree

def main(argv):
    train_fname = argv[0]
    test_fname = argv[1]
    criterion = argv[2]

    tree = dtree.Tree(train_fname, test_fname, criterion)

if __name__ == "__main__":
    main(sys.argv[1:])