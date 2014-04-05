showStatement = False
printErrors = True
lineNumber = 0

# a function to print the name of the statement
def printStatement(statement):
    global showStatement
    if showStatement:
        print statement

def printError(statement, lineno):
    global printErrors
    if printErrors:
        print 'line %d:' %lineno, statement

def incrementLineNumber():
    global lineNumber
    lineNumber = lineNumber + 1
