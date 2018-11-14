import argparse

parser = argparse.ArgumentParser(description='command line parser.')

parser.add_argument('-e','--env', required=True, help='Environment')

parser.add_argument('--sol', required=False, help='Environment')

parser.add_argument('--flag', required=False, action='store_true',help='Environment')

args = parser.parse_args()

print('args : ', args)

print('Env : ', args.env)
print('Sol : ', args.sol)
print('flag : ', args.flag)

