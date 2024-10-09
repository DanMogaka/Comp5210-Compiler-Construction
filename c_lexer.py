'''
    List of tokens supported by the lexer
'''
available_tokens = {
    "(": "LPAR", ")": "RPAR", "{": "LBRAC",
    "}": "RBRAC", ";": "SCOLON", "\n": "ESC_CHAR",
    "+": "ADD", "-": "SUB", "*": "MUL", "/": "DIV" 
}
reserved_keywords = {
    "return": "RETURN", "false": "FALSE", "true": "TRUE"
}

type_identifier = { "bool", "int", "float", "char"
}


'''
    Reads in a C source file and returns its contents as a string
    Input: filename
    Output: File content as str
'''
def load_cfile(filename):
    f = open(filename, 'r')
    content = []
    for line in f:
        content.append(line)
    f.close()
    
    return ''.join(content)


def tokenizer(filename):
    '''
    Basic program to parse through a program an array of different symbols and group.
    INPUT: Filename of the c file to be lexically analysed. 
    RETURNS: An array of tokenized characters.
    '''

    input_stream = load_cfile(filename)

    output_stream = [] 

    idx = 0
    while idx < len(input_stream):
        int_sequence = []
        ident_sequence = []
        if input_stream[idx].isnumeric():
            while idx < len(input_stream) and input_stream[idx].isnumeric():
                int_sequence.append(input_stream[idx])
                idx += 1

            output_stream.append(("INTEGER", "".join(int_sequence)))
        elif input_stream[idx].isalpha():
            while idx < len(input_stream) and input_stream[idx].isalpha():
                ident_sequence.append(input_stream[idx])
                idx += 1

            ''' evaluate identifier '''
            identifier = "".join(ident_sequence)
            if identifier in reserved_keywords:
                output_stream.append((reserved_keywords[identifier], identifier))
            elif identifier in type_identifier:
                output_stream.append(("TYPE", identifier))
            else:
                output_stream.append(("IDENT", identifier))

        elif input_stream[idx] in available_tokens:
            output_stream.append((available_tokens[input_stream[idx]], input_stream[idx]))
            idx += 1
        else:
            print("Error! Not supported token")
            idx += 1
        #todo: Fix the case for white spaces
        #todo: Add edge for supporting floating-constant and character-constant

    return output_stream