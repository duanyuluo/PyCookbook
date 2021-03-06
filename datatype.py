#encoding=utf-8

from tools import *

i = new_intro("Data Type")

i.intro_chapter(
"""
built-in data type:

Text Type:      str
Numeric Types:  int, float, complex
Sequence Types: list, tuple, range
Mapping Type:   dict
Set Types:      set, frozenset
Boolean Type:   bool
Binary Types:   bytes, bytearray, memoryview
""")

i.section("Probe python built-in datatype.")
print("'Hello'", probe_var("Hello"))
print("20", probe_var(20))
print("20.0", probe_var(20.0))
print("2+1j", probe_var(2+1j))
print("[1,2,3]", probe_var([1,2,3]))
print("(1,2,3)", probe_var((1,2,3)))
print("range(10)", probe_var(range(10)))
print("{'name':'max', 'age':14}", probe_var({'name':'max', 'age':14}))
print("{'apple', 'orange', 'banana'}", probe_var({'apple', 'orange', 'banana'}))
print("True", probe_var(True))
print("b'Hello'", probe_var(b'Hello'))
print("bytearray(5)", probe_var(bytearray(5)))
print(probe_var(bytes(5)))

i.section("Use random.randrange() generate 10 random numbers.")
import random
array_rdm = [random.randrange(1, 10) for rdm in range(10)]
print("random.randrange 10 times are ", probe_var(array_rdm))