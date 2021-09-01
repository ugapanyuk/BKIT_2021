import os
from module_1 import *
from module_2 import *

# import * рекомендуется только во вспомогательном коде
# при отладке, написании тестов и т.д.

print('Hello from {}'.format(os.path.basename(__file__)))

a=2
b=3
print('{} + {} = {}'.format(a, b, sum1(a,b)))
