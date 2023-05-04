
def mid(alpha):
        string_length = len(alpha)
        mod_value = string_length%2
        #print(mod_value)
        if mod_value==0:
            print('No Middle letter found')
        else:
            little_less_value = string_length//2
            middle_letter_value = little_less_value
            print('Middle letter found is:' + alpha[middle_letter_value])

alpha = input('Please input a name :')
#alpha = 'abc'
mid(alpha)