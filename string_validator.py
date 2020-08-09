# https://www.hackerrank.com/challenges/string-validators/problem
import re

s = input()
print(bool(re.search(r'[A-Za-z0-9]', s)))
print(bool(re.search('[A-Za-z]', s)))
print(bool(re.search(r'[0-9]', s)))
print(s != s.upper())
print(s != s.lower())


