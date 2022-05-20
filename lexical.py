from pydoc import isdata
import re


tokens=[]
input =' int x = 5'.split()



def isDatatype():
    for word in input:
        if word in ['int','double','string']:
            tokens.append(['DATATYPE', word])
    return tokens

if __name__ == '__main__':

    print(isDatatype())