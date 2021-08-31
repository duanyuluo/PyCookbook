#encoding=utf-8

from tools import *

i = new_intro("string")

str_sent = "life is short, use python."

i.section("string is a array of charactors. ")
i.intro("You can get any by [] operator.")
print(str_sent, probe_var([str_sent[idx] for idx in range(len(str_sent))]))

i.section("Scan string by for loop")
for c in str_sent:
    if c == '\n':
        print('EL')
    else:
        print(c, end=',')
print("<<")