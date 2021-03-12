import fileinput
import re

for line in fileinput.input():

    result = line;

    # add spaces around operators
    result = re.sub(r"([\*\/\+\-\=<>|][\+\-\=|]*)", r" \1 ", result);

    # add spaces after comma, not before
    result = re.sub(r"\s*,\s*", r", ", result);

    # add space after open querly brace
    result = re.sub(r"{\s*(\S)", r"{ \1", result)

    # add space before close querly brace
    result = re.sub(r"(\S)\s*}", r"\1 }", result)

    # formate List<ABC> Block
    result = re.sub(r"List\s*<\s*([a-z,0-9,A-Z]*)\s*>", r"List<\1>", result);

    # reduce multiple spaces
    result = (re.sub(r"\s\s*", " ", result))

    print(result)
