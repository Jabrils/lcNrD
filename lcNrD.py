import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", "--file", type=str,
    help='this is the file you\'re targeting to get the lcNrD treatment')
parser.add_argument("-o", "--out", type=str,
    help='this is the file you want the lcNrD file to output as')

# store true or false so we can just be like 'if args.lowercase:'
# so use true or false values instead of comparing strings
parser.add_argument('-l', "--lowercase", action='store_true',
    help='add -l to set lowercase to true')
parser.add_argument('-d', "--duplicates", action='store_true',
    help='add -d to remove duplicate elements')
args = parser.parse_args()

print('Grabbing file contents...')
# open the target file & grab its contents. Using `with` like this automatically
# closes the file for us when we leave the indentation.
with open(args.file, "r") as fp:
    text = fp.read()

# convert to lowercase while we have the initial string. so only one function
# call and no loops needed.
if args.lowercase:
    print('lowercasing contents...')
    text = text.lower()

# need to store 
lines = text.split("\n")

# remove duplicates by making the list a `set` which automatically makes
# everything unique. Again no loops, just 1 function call.
if args.unique:
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