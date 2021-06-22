from urllib.parse import urlparse
import sys
import re

def readFile(file, collaborator):
	lines = open(file).readlines()
	for l in lines:
		domain = urlparse(l).netloc
		l = l.replace("\n","")
		l = prepSpace(l)
		l = replace_fuzz(l, getParam(l), domain, collaborator)
		print(l)

def prepSpace(l):
	l = l.replace(" ","+")
	return l

def getParam(l):
	regex = re.compile("([\\w%]{0,})(?=\\=FUZZ)")
	matchArray = regex.findall(l)
	try:
		return matchArray[0]
	except:
		pass

def replace_fuzz(l,param,domain, collaborator):
	l = l.replace("=FUZZ",f"=https%3A%2F%2Fparameter-{param}.{domain}.{collaborator}")
	return l

def main():
	collaborator = sys.argv[1]
	file = sys.argv[2]

	readFile(file, collaborator)

if __name__ == '__main__':
	main()