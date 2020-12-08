import re

with open('data.txt') as f:
    data = f.read().strip().split('\n')
# print(data)

res = 0
for i in data:
