# Define a function which takes keywork arguments.

def func_keywrd_args(**kwargs):
    print(kwargs)

func_keywrd_args(delim=':', data_str='The quick brown fox jumps over the lazy dog')