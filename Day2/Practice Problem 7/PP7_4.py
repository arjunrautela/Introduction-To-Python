# Write content to a file

file_handle = open('dummy.txt', 'w')

str_to_write = 'The quick brown fox jumps over the lazy dog'

file_handle.write(str_to_write)

file_handle.close()