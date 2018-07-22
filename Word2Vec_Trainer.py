import sys
import gensim
import keras

def GetDoc(docPath):
	doc = []

	f = open(docPath, "r")
	doc[0] = f.read()
	return doc


if __name__ == "__main__":

	# Check argument length
	if len(sys.argv) != 2:
		print("Invalid number of arguments. Please give the path for the document to build on.")
		break;

	# Get document
	doc = GetDoc(sys.argv[1])

	# Convert document to vector representation
