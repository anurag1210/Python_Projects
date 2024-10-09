
def strings_enumerate():
    string_input = input('Input the String value : ')
    for char, idx in enumerate(string_input):
        print(char,idx)



if __name__=='__main__':
    strings_enumerate()