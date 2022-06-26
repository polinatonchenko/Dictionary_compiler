def dictionary_compiler(some_text:str, print_dictionary=False, exception_words=[]):
    '''compiles dict (where the key is a word, the value is the number of repetitions) based on the some_text'''
    some_text = some_text.lower()
    changed_text = "".join(c for c in some_text if c.isalpha() or c==" ")
    print(changed_text)
    return


def replace_substrings(some_text:str, substrings_list:list=[], replace = ''):
    '''replace all substrings from substrings_list in some_text'''
    for some_substring in substrings_list:
        some_text = some_text.replace(some_substring, replace)
    return some_text

print('''In the deep, there are beasts so fell and terrible, that only they know what they are, for none who have met them have lived to tell of it... they are the Forgotten Beasts, born of the chaos from before the world's birth... they have waited, brooding in the dark places of the world... and now... by digging too deep... we have awakened them.''')
dictionary_compiler('''In the deep, there are beasts so fell and terrible, that only they know what they are, for none who have met them have lived to tell of it... they are the Forgotten Beasts, born of the chaos from before the world's birth... they have waited, brooding in the dark places of the world... and now... by digging too deep... we have awakened them.''')