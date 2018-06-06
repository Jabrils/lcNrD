import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.3', help="Show program's version number and exit.")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='** = required')
parser.add_argument(
    "-f", "--file", type=str,
    help='** this is the file you\'re targeting to get the lcNrD treatment')
parser.add_argument("-o", "--out", type=str,
    help='this is the file you want the lcNrD file to output as. Default = same name + _LcNrD')

# store true or false so we can just be like 'if args.lowercase:'
# so use true or false values instead of comparing strings
parser.add_argument('-l', "--lowercase", action='store_true',
    help='add -l to set lowercase to true')
parser.add_argument('-d', "--duplicates", action='store_true',
    help='add -d to remove duplicate elements')
parser.add_argument('-rk', "--removal_keyword", type=str,
    help='add -rk to remove lines with the removal keyword')
parser.add_argument('-kk', "--keep_keyword", type=str,
    help='add -kk to keep only the lines with the keep keyword')
args = parser.parse_args()

print('Grabbing file contents...')

# open the target file & grab its contents. Using `with` like this automatically
# closes the file for us when we leave the indentation.
with open(args.file, "r") as fp:
    text = fp.read()

# lets turn every line into an array 
lines = text.split("\n")

# this checks if there is a removal keyword & performs this operation if so
if args.removal_keyword != None:
    print('removing lines with removal keyword...')
    temp = ''

    # loop through all elements in the lines array
    for i in lines:
        # if not containing the removal keyword, then add it to temp
        if args.removal_keyword not in i:
            temp+='\n'+i
    
    # lines now = temp split, minus the first element which is an empty element
    lines = temp.split('\n')[1:]

# this checks if there is a removal keyword & performs this operation if so
if args.keep_keyword != None:
    print('removing lines without keep keyword...')
    temp = ''

    # loop through all elements in the lines array
    for i in lines:
        # if not containing the removal keyword, then add it to temp
        if args.keep_keyword in i:
            temp+='\n'+i
            print(i)
    
    # lines now = temp split, minus the first element which is an empty element
    lines = temp.split('\n')[1:]

# convert to lowercase while we have the initial string. so only one function
# call and no loops needed.
if args.lowercase:
    print('lowercasing contents...')
    lines = [x.lower() for x in lines]


# remove duplicates by making the list a `set` which automatically makes
# everything unique. Again no loops, just 1 function call.
if args.duplicates:
    print('removing duplicates...')
    lines = set(lines)

# set the name of the new converted file
if not args.out:
    # ok this is a little bit obscure but its reverse splitting an string into
    # a list once so 'dir/file.txt' -> ['dir/file', 'txt']. then the '*' before
    # it when passed to format tells format to read the list as mulptiple args.
    args.out = "{}._lcNrD.{}".format(*args.file.rsplit(".", 1))


# save the converted file
with open(args.out, "w") as fp:
    # strings are immutable in python so every time you add two strings together
    # its creating a brand new one. This gets quickly gets slow with lots of text
    # so we wanna do this as little as possible. Using join on the list means
    # we just make all the string concatenation opertations in one go.
    fp.write("\n".join(lines))

print('...& DONE!')