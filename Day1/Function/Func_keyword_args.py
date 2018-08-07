# Define a function which takes keywork arguments.

def func_keywrd_args(**kwargs):
    print(kwargs)
    print(kwargs['data_str'].split(kwargs['delim']))

func_keywrd_args(delim=' ', data_str='The quick brown fox jumps over the lazy dog')