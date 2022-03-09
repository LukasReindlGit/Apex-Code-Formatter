import fileinput
import re

current_indent = 0
next_indent = 0
indentsteps = 4

lastline = ""


def regexSubstitution(line):

    result = line


    # add spaces around operators
    result = re.sub(r"([\*\/\+\-\=\&!<>|][\+\-\=\&!<>|]*)", r" \1 ", result)

    # add spaces after comma, not before
    result = re.sub(r"\s*,\s*", r", ", result)

    # add space after open querly brace
    result = re.sub(r"{\s*(\S)", r"{ \1", result)

    # add space before close querly brace
    result = re.sub(r"(\S)\s*}", r"\1 }", result)

    # format List<ABC> varName = new List<ABC>()
    result = re.sub(
        r"List\s*<\s*([a-z,0-9,A-Z,_,\.]*)\s*>", r"List<\1>", result)
    result = re.sub(
        r"List\s*<\s*([a-z,0-9,A-Z,_,\.]*)\s*>\s*\(", r"List<\1>(", result)

    # format Set<ABC> varName = new Set<ABC>()
    result = re.sub(r"Set\s*<\s*([a-z,0-9,A-Z,_,\.]*)\s*>", r"Set<\1>", result)
    result = re.sub(
        r"Set\s*<\s*([a-z,0-9,A-Z,_,\.]*)\s*>\s*\(", r"Set<\1>(", result)

    # format Map<A,B> varName = new Map<A,B>()
    result = re.sub(
        r"Map\s*<\s*([a-z,0-9,A-Z,_,\.]*),\s*([a-z,0-9,A-Z,_,\.]*)\s*>", r"Map<\1,\2>", result)
    result = re.sub(
        r"Map\s*<\s*([a-z,0-9,A-Z,_,\.]*),\s*([a-z,0-9,A-Z,_,\.]*)\s*>\s*\(", r"Map<\1,\2>(", result)

    # format if Block
    result = re.sub(r"(\s)\s*if\s*\(", r"\1if (", result)

    # reduce multiple spaces
    result = (re.sub(r"\s\s*", " ", result))

    # remove space in ( ) and { }
    result = (re.sub(r"\( \)", "()", result))
    result = (re.sub(r"\{ }", "{}", result))

    # add space between (){}
    result = (re.sub(r"\)\{", ") {", result))

    # add Test
    result = re.sub(r"#TEST", r"@isTest\npublic static void test(){\n\t// Given\n\n\t// When\n\tTest.startTest();\n\tTest.stopTest();\n\n\t// Then\n}", result)

    return result

def restoreQuoteContent(original, changed):
    if '\'' not in line:
        return changed

    splitted_result = changed.split('\'')
    splitted_original = original.split('\'')
    tmp = ''
    for i in range(len(splitted_result)):
        # if index is even: we are not inside quotes -> use reformatted block
        if i % 2 == 0:
            tmp += splitted_result[i]
        else:
            tmp += splitted_original[i]
        # add ' between entries
        if i < len(splitted_result)-1:
            tmp += '\''
    return tmp

for line in fileinput.input():
    # skip comments for now
    if '//' in line:
        result = line.rstrip().lstrip()
        lastline = result
        print(" "*indentsteps*current_indent+result)
        continue
    if '/*' in line or '*/' in line:
        result = line.rstrip().lstrip()
        lastline = result
        print(" "*indentsteps*current_indent+result)
        continue

    # Perform all regex rules!
    result = regexSubstitution(line)

    # override content of quotes with original quote content
    result = restoreQuoteContent(line, result)

    # calculate Indentation (ignore string content and comments)
    indentationLine = line
    indentationLine = re.sub(r"'.*?'", r"", indentationLine)
    indentationLine = re.sub(r"//.*", r"", indentationLine)
    increment = 0
    increment += (indentationLine.count('{')-indentationLine.count('}'))
    increment += (indentationLine.count('(')-indentationLine.count(')'))
    increment += (indentationLine.count('[')-indentationLine.count(']'))

    if increment >= 0:
        next_indent += increment
    else:
        current_indent += increment
        next_indent = current_indent

    # Trim whitespaces
    result = result.rstrip().lstrip()

    # Skip multi-white-line
    if lastline == "" and result == "":
        continue

    # Close indentation when closing braces TODO: replace this with regex!
    toprint = ""
    if result == ")" or result == "}" or result == "]":
        toprint= " " * indentsteps * (next_indent) + result
    else:
        toprint= " " * indentsteps * (current_indent) + result
    
    # remove whitespace from empty lines
    if not result or not result.strip():
        toprint =""

    print(toprint)

    current_indent = next_indent
    lastline = result

exit(0)
