import os

# 示例
file_path =  "our_method.txt"
file_new_path = "our_method1.txt"


def solvepre(line):
    line = line.replace("∧", "&&")
    line = line.replace("→", "->")
    line = line.replace("->", "->")
    line = line.replace("&&", "&")
    line = line.replace("¬", "!")
    line = line.replace("∨", "||")
    line = line.replace(" || ", " | ")
    line = line.replace(" implies ", " -> ")
    return line

textlist = []
with open(file_path, "r", encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n')
        line = solvepre(line)
        textlist.append(line)
    print("-----------------1---------------")
    file.close()



with open(file_new_path, 'w') as f:
     for i in textlist:
            f.write(i + '\n')
     f.close()
     print("-----------------2--------------")
