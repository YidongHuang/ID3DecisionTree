import ARFF
import sys

def main(argv):
    input_fname = argv[0]
    output_fname = argv[1]
    criterion = argv[2]

    input_file = ARFF.ARFF(input_fname)

    print input_file.to_string()

if __name__ == "__main__":
    main(sys.argv[1:])