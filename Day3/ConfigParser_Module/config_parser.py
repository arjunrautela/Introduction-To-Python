import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config_sample.config')

'''
print config.sections()
print config.get('vgerndvud1479', 'hostname')
#print config.get('vgerndvud1477', 'hostname')
print config.options('vgerndvud1479')
'''
d = {}
fd={}
for section in config.sections():
    #read all the option and its value
    options = config.options(section)
    for option in options:
        #print config.get(section,option)
        d[option] = config.get(section,option)
    #print d
    fd[section] = d
    d = {}
print(fd)

'''
        options = config.options(section)
        print options
        for option in options:
            print config.get(section, option)


{'vgerndvud1479':{'hostname': 'vgerndvud1479', 'user':'linqus', 'ssh_port': '22'}, 'vgerndvud1659':{'hostname': 'vgerndvud1479', 'user': 'linqus'}}
'''