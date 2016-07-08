# import necessary libraries
import sys

# main entry point
def main(argv):
# if we do not have just one argument, show usage
    if len(argv) <> 1:
        print "usage: python wordreverse.py \"sentence\""
        sys.exit(2)
    try:
# call reverse sentence function
        reverseSentence(sys.argv[1])
    except Exception as error:
        print "An error has occurred while reversing the sentence: " + type(error)
        raise

# simple function using built in string methods to split on whitespace and rejoin in reverse
def reverseSentence(string):
    print " ".join(reversed(string.split()))

# if called from commandline call main function with arguments
if __name__=="__main__":
    main(sys.argv[1:])

