from pprint import pprint

dict_t = {'a':'1', 'b':17, 'info':'time',
'nine':'9', 'ride':'bike', 'r1': {'hostname': 'london_r1', 'location': '21'}, 
'r2': {'hostname': 'london_r2', 'location': '23'}}
print(dict_t, end='\n\n')
pprint(dict_t)
print()

interfaces = [['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'], 
['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'], 
['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]

print(interfaces, end='\n\n')
pprint(interfaces)