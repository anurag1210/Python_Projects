'''
Strings.py program  to
convert a sentence into its UTF-8
version
'''

def get_user_sentence():
    user_sentence=input('Please input a sentence :')
    sentence_len=len(user_sentence)
    print(f'The length of your sentence is {sentence_len}')

    for char in user_sentence:
        print(f'{char} in {ord(char)}')


if __name__=='__main__':
     get_user_sentence()