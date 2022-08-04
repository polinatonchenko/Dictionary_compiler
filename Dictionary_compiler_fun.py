import os
import json

def dictionary_compiler(some_text:str=None, txt_file:str=None):
    '''compiles dict (where the key is a word, the value is the number of repetitions) based on the some_text'''
    try: os.mkdir("texts")
    except: FileExistsError
    if some_text == None:
        if txt_file != None:
            with open(f"texts/{txt_file}", 'r') as file:
                some_text = file.read().replace('\n', ' ')
        else:
            list_of_names = list_txt_files("texts")
            if len(list_of_names) == 0:
                print("No text")
                return 
            for n in list_of_names:
                dictionary_compiler(txt_file=n)
            return
    if not is_accessible("dict.json"):
        with open("dict.json", "w") as wf:
            json.dump({}, wf)
    with open("dict.json", "r") as rf:
        fin_dict = json.load(rf)
    some_text = some_text.lower()
    changed_text = "".join(c for c in some_text if c.isalpha() or c==" ") # removes all symbols except letters from the text
    text_list = changed_text.split()
    step_dict = dict.fromkeys(text_list, 0)
    for w in text_list:
        step_dict[w] += 1 
    fin_dict = dict_combiner(fin_dict, step_dict)
    with open("dict.json", "w") as wf:
        json.dump(fin_dict, wf)
    return

def list_txt_files(mydir = None):
    '''creates a list of all file names in a directory with a .txt extension'''
    list_of_names = []
    for file in os.listdir(mydir):
        if file.endswith(".txt"):
            list_of_names.append(file)
    return list_of_names

def is_accessible(path, mode='r'):
    '''Checking if a file or folder is from `path` available to work in the format provided by `mode`'''
    try:
        f = open(path, mode)
        f.close()
    except FileNotFoundError:
        return False
    return True

def dict_combiner(dict1 , dict2):
    '''creates a dictionary with keys from dict1 and dict2 and sum their values'''
    for k in dict1:
        if k in dict2:
            dict1[k] += dict2[k]
            dict2.pop(k)
    dict1.update(dict2)
    return dict1

def replace_substrings(some_text:str, substrings_list:list=[], replace = ''):
    '''replace all substrings from substrings_list in some_text'''
    for some_substring in substrings_list:
        some_text = some_text.replace(some_substring, replace)
    return some_text

dictionary_compiler()
