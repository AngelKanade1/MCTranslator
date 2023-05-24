import ast

with open('en_us.json', 'r', encoding='utf8') as fp:
    jsonStr = ""
    for line in fp.readlines():
        if "//" not in line:
            jsonStr += line

print(ast.literal_eval(jsonStr))
