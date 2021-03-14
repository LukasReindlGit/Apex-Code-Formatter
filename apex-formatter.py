import fileinput
import re

current_indent = 0
next_indent = 0
indentsteps = 4

lastline=""


def regexSubstitution(line):

    result = line

    # add spaces around operators
    result = re.sub(r"([\*\/\+\-\=<>|][\+\-\=|]*)", r" \1 ", result)

    # add spaces after comma, not before
    result = re.sub(r"\s*,\s*", r", ", result)

    # add space after open querly brace
    result = re.sub(r"{\s*(\S)", r"{ \1", result)

    # add space before close querly brace
    result = re.sub(r"(\S)\s*}", r"\1 }", result)

    # formate List<ABC> Block
    result = re.sub(r"List\s*<\s*([a-z,0-9,A-Z]*)\s*>", r"List<\1>", result)

    # reduce multiple spaces
    result = (re.sub(r"\s\s*", " ", result))

    return result


for line in fileinput.input():
    # skip comments for now
    if '//' in line:
        print(" "*indentsteps*current_indent+line.rstrip().lstrip())
        continue

    # Perform all regex rules!
    result = regexSubstitution(line)

    # Indentation
    next_indent += (line.count('{')-line.count('}'))
    next_indent += (line.count('(')-line.count(')'))
    next_indent += (line.count('[')-line.count(']'))

    # Trim whitespaces
    result = result.rstrip().lstrip()

    # Skip multi-white-line
    if lastline == "" and result == "":
        continue;

    # Close indentation when closing braces TODO: replace this with regex!
    if result == ")" or result == "}" or result == "]":
        print(" " * indentsteps * (next_indent) + result)
    else:
        print(" " * indentsteps * (current_indent) + result)

    current_indent = next_indent
    lastline = result;

exit(0)
