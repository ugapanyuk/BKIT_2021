import os
import sys
import module_3

print('Hello from {}'.format(os.path.basename(__file__)))

a=2
b=3
print('{} + {} = {} \n'.format(a, b, module_3.sum1(a,b)))

print(sys.path)
