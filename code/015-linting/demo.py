# Linting is the process of checking code for best practice formatting issues
# If a code fails a lint test / check, it is not rejected by default
# pylint - linting tool for python
# pip install pylint

# pylint <name of file>
# /* multiline comment in other languages

# */

""" Module docstring saying what this module does """

LONG_VAR = "abc"
def printtext(new_text):
    """ Telling you what this function does
    lots of things to say
    """
    print("hello world")
    return f"text added is {new_text}"
print(printtext('howdy'))
print(printtext(LONG_VAR))
