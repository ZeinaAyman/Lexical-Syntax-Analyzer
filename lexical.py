from ast import Not
from pydoc import isdata
#from tabulate import tabulate
import re



class Token:

    def tokenizer(self, tokens, input):
        dt=False
        id=False
        op=False
        cast=False
        for word in input:
            #tokenizer will look for datatype
            if word in ['int','double','string']:
                dt=True
                tokens.append(['DATATYPE', word])

            #tokenizer will look for identifier type
            elif re.match("^[A-Za-z_][A-Za-z0-9_]*$", word):
                id=True
                tokens.append(['IDENTIFIER', word])

            #tokenizer will look for operators
            elif word in '*-/+%=':
                op=True
                tokens.append(['OPERATOR', word])

            # tokenizer will look for integer items and cast them as a integer number
            elif re.match("^[1-9]\d*$", word):
                cast=True
                tokens.append(["INTEGER NUMBER", word])

            # tokenizer will look for double items and cast them as a double number
            elif re.match("^[0-9]+\\.?[0-9]*$", word):
                cast=True
                tokens.append(["DOUBLE NUMBER", word])

        if not dt:
            print("datatype invalid")
        if not id: 
            print("identifier invalid")
        if not op:
            print("miss-used operator")
        if not cast:
            print("data type missmatch")

        return tokens


if __name__ == '__main__':

    tokens=[]
    input =' intz x1 = 7'.split()
    tok = Token()
    #print(tabulate(tok.tokenizer(tokens, input), tablefmt="grid"))
    print(tok.tokenizer(tokens, input))