###学号：201811113033###
import re

f = open("log_files/201811113033.log",encoding='utf8')
text = f.read()

f.close()

num = re.split(r'[\s,]',text)

# print(num)

count = {'学号：201811113033':0}

for n in num:
        if n in count:
                count["学号：201811113033"] += 1

print(count["学号：201811113033"])