import ARFF
import sys
import tree as dtree
import matplotlib.pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages

def main(argv):

    train_fname = argv[0]
    test_fname = argv[1]
    criterion = argv[2]

    tree = dtree.Tree(train_fname, criterion)
    tree.load_test_file(test_fname)
    tree.test_tree()

    '''
    heart_tree = dtree.Tree('train.arff', 4)
    heart_tree.load_test_file('test.arff')

    avg_data = []
    max_data = []
    min_data = []
    plot_data = []
    for i in range(10):
        plot_data.append(heart_tree.test_random_data(5))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))

    plot_data = []
    for i in range(10):
        plot_data.append(heart_tree.test_random_data(10))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))

    plot_data = []
    for i in range(10):
        plot_data.append(heart_tree.test_random_data(20))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))

    plot_data = []
    for i in range(10):
        plot_data.append(heart_tree.test_random_data(50))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))

    plot_data = []
    for i in range(10):
        plot_data.append(heart_tree.test_random_data(100))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))


    avg_line, = plot.plot([5, 10, 20, 50, 100],avg_data, label = 'average accuracy')
    max_line, = plot.plot([5, 10, 20, 50, 100],max_data, label = 'max accuracy')
    min_line, = plot.plot([5, 10, 20, 50, 100],min_data, label = 'min accuracy')
    plot.ylabel("Decision Tree Accuracy in %")
    plot.xlabel("Random Data Being Tested in %")
    plot.title("Percentage Accuracy for Heart Disease Data")
    plot.legend(handles=[avg_line, max_line, min_line], loc=4)
    plot.show()

    diabete_tree = dtree.Tree('diabete_train.arff', 4)
    diabete_tree.load_test_file('diabete_test.arff')

    avg_data = []
    max_data = []
    min_data = []
    plot_data = []
    for i in range(10):
        plot_data.append(diabete_tree.test_random_data(5))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))

    plot_data = []
    for i in range(10):
        plot_data.append(diabete_tree.test_random_data(10))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))

    plot_data = []
    for i in range(10):
        plot_data.append(diabete_tree.test_random_data(20))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))

    plot_data = []
    for i in range(10):
        plot_data.append(diabete_tree.test_random_data(50))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))

    plot_data = []
    for i in range(10):
        plot_data.append(diabete_tree.test_random_data(100))
    avg_data.append(sum(plot_data)/float(len(plot_data)))
    max_data.append(max(plot_data))
    min_data.append(min(plot_data))


    avg_line, = plot.plot([5, 10, 20, 50, 100],avg_data, label = 'average accuracy')
    max_line, = plot.plot([5, 10, 20, 50, 100],max_data, label = 'max accuracy')
    min_line, = plot.plot([5, 10, 20, 50, 100],min_data, label = 'min accuracy')
    plot.ylabel("Decision Tree Accuracy in %")
    plot.xlabel("Random Data Being Tested in %")
    plot.title("Percentage Accuracy for Diabetes Data")
    plot.legend(handles=[avg_line, max_line, min_line], loc=4)
    plot.show()

    m_size_data = []
    diabete_tree = dtree.Tree('diabete_train.arff', 2)
    diabete_tree.load_test_file('diabete_test.arff')
    m_size_data.append(diabete_tree.test_tree())

    diabete_tree = dtree.Tree('diabete_train.arff', 5)
    diabete_tree.load_test_file('diabete_test.arff')
    m_size_data.append(diabete_tree.test_tree())

    diabete_tree = dtree.Tree('diabete_train.arff', 10)
    diabete_tree.load_test_file('diabete_test.arff')
    m_size_data.append(diabete_tree.test_tree())

    diabete_tree = dtree.Tree('diabete_train.arff', 20)
    diabete_tree.load_test_file('diabete_test.arff')
    m_size_data.append(diabete_tree.test_tree())

    plot.plot([2, 5, 10, 20],m_size_data)
    plot.ylabel("Decision Tree Accuracy in %")
    plot.xlabel("m size")
    plot.title("Percentage Accuracy for Diabetes Data")
    plot.show()

    m_size_data = []
    diabete_tree = dtree.Tree('train.arff', 2)
    diabete_tree.load_test_file('test.arff')
    m_size_data.append(diabete_tree.test_tree())

    diabete_tree = dtree.Tree('train.arff', 5)
    diabete_tree.load_test_file('test.arff')
    m_size_data.append(diabete_tree.test_tree())

    diabete_tree = dtree.Tree('train.arff', 10)
    diabete_tree.load_test_file('test.arff')
    m_size_data.append(diabete_tree.test_tree())

    diabete_tree = dtree.Tree('train.arff', 20)
    diabete_tree.load_test_file('test.arff')
    m_size_data.append(diabete_tree.test_tree())

    plot.plot([2, 5, 10, 20],m_size_data)
    plot.ylabel("Decision Tree Accuracy in %")
    plot.xlabel("m size")
    plot.title("Percentage Accuracy for Heart Disease Data")
    plot.show()
    '''

if __name__ == "__main__":
    main(sys.argv[1:])