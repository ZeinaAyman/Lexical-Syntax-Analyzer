from pydoc import isdata
import re



class Token:
    
    def isDatatype(self, tokens, input):
        for word in input:
            if word in ['int','double','string']:
                tokens.append(['DATATYPE', word])
        return tokens



if __name__ == '__main__':

    tokens=[]
    input =' int x = 5'.split()
    tok = Token()
    print(tok.isDatatype(tokens, input))