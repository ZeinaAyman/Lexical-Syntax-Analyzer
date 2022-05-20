from pydoc import isdata
from tabulate import tabulate
import re



class Token:

    def tokenizer(self, tokens, input):
        for word in input:
            #tokenizer will look for datatype
            if word in ['int','double','string']:
                tokens.append(['DATATYPE', word])

            #tokenizer will look for identifier type
            elif re.match("^[A-Za-z_][A-Za-z0-9_]*$", word):
                tokens.append(['IDENTIFIER', word])

            #tokenizer will look for operators
            elif word in '*-/+%=':
                tokens.append(['OPERATOR', word])

            # tokenizer will look for integer items and cast them as a integer number
            elif re.match("^[1-9]\d*$", word):
                tokens.append(["INTEGER NUMBER", word])

            # tokenizer will look for double items and cast them as a double number
            elif re.match("^[0-9]+\\.?[0-9]*$", word):
                tokens.append(["DOUBLE NUMBER", word])

        

        return tokens


if __name__ == '__main__':

    tokens=[]
    input =' int x1 = 5.32 + 7'.split()
    tok = Token()
    print(tabulate(tok.tokenizer(tokens, input), tablefmt="grid"))