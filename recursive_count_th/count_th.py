'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    def count_ths(word, count):
        print(word)
        if len(word)<=1:
            # print('word in the if', word)
            return count
        elif word[-2] + word[-1]== 'th':
            # print('word in the else', word)
            count +=1
    
        # print('word before return', word)
        return count_ths(word[:-1], count)

    return count_ths(word, 0)
