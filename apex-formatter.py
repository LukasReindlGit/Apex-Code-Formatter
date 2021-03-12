import fileinput
import re

current_indent = 0
indentsteps = 4


def regexSubstitution(line):

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
    
    return result


for line in fileinput.input():
    # skip comments for now
    if '//'in line:
        print(" "*indentsteps*current_indent+line.rstrip().lstrip());
        continue;

    # Perform all regex rules!
    line = regexSubstitution(line);

    # count current indentation level
    current_indent += line.count('{')
    current_indent -= line.count('}')

    # prepare string without indentation or trailing spaces
    result = line.rstrip().lstrip()

    if len(result) == 0:
        print('')
        continue

    # does it end with an {? if so, push it to a new line!
    if len(result) > 1 and result[-1] == '{':
        print(" "*indentsteps*(current_indent-1)+result[:-1])
        result = '{'

    # is the line only { ?
    if len(result) == 1 and result[0] == '{':
        print(" "*indentsteps*(current_indent-1)+'{')
        continue

    print(" "*indentsteps*current_indent+result)
    current_indent += line.count('(')
    current_indent -= line.count(')')

    # TODO:
    # - rebuild to use regex rules per line
    # - put { always on new line (DONE)
    # - Correct indentation (DONE)
    # - space after ,
    # - space around operands
    # - space around () NOPE!
    # - no double space
    # - no empty line over } line
    # - increase indentation when line ends with (

    # IGNORE:
    # - All comments (easy hack: if contains // done)
    # - Inside strings (quick: if ' " ' in line)