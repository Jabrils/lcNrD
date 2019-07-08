import argparse
import re 
import random as r

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.6', help="Show program's version number and exit.")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='** = required')
parser.add_argument(
    "-f", "--file", type=str,
    help='** this is the file you\'re targeting to get the lcNrD treatment')
parser.add_argument("-o", "--out", type=str,
    help='this is the file you want the lcNrD file to output as. Default = same name + _LcNrD')
parser.add_argument("-id", "--input_delimiter", type=str, default='\\n',
    help='this is the delimiter you want lcNrD to use for the input file')
parser.add_argument("-od", "--output_delimiter", type=str,
    help='this is the delimiter you want lcNrD to use for the output file. Default = input delimiter')

# store true or false so we can just be like 'if args.lowercase:'
# so use true or false values instead of comparing strings
parser.add_argument('-l', "--lowercase", action='store_true',
    help='add -l to set lowercase to true')
parser.add_argument('-d', "--duplicates", action='store_true',
    help='add -d to remove duplicate elements')
parser.add_argument('-s', "--shuffle", action='store_true',
    help='add -s to shuffle your list')
parser.add_argument('-rf', "--replace_file", action='store_true',
    help='add -rf to replace the original file after lcnrd operation')
parser.add_argument('-bl', "--blank_lines", action='store_true',
    help='add -bl to remove all blank lines')
parser.add_argument('-cmi', "--character_min", type=int, default=0,
    help='limits the minimal amount of chacters required')
parser.add_argument('-cma', "--character_max", type=int,
    help='limits the maximum amount of chacters required')
parser.add_argument('-kr', "--keyword_removal", type=str,
    help='add a -kr to remove lines with the removal keyword, use *.txt or whatever to point to a list of kr')
parser.add_argument('-kk', "--keyword_keep", type=str,
    help='add a -kk to keep only the lines with the keep keyword, use *.txt or whatever to point to a list of kk')
parser.add_argument('-kdb', "--keyword_delete_before", type=str,
    help='add a -kdb to delete all text before the delete before keyword')
parser.add_argument('-kda', "--keyword_delete_after", type=str,
    help='add a -kda to delete all text after the delete after keyword')
parser.add_argument('-kae', "--keyword_add_end", type=str,
    help='add a -kae to add some text to the end of every line')
args = parser.parse_args()

# check if input_delimiter is set to default & if so rectify escape character
# this escapse character is left in so that the default value displays correctly in -h
if(args.input_delimiter == "\\n"):
    args.input_delimiter = "\n"

# set output delimiter to input delimiter if output delimiter isn't set
if(args.output_delimiter == None):
    args.output_delimiter = args.input_delimiter

print('Grabbing file contents...')

# open the target file & grab its contents. Using `with` like this automatically
# closes the file for us when we leave the indentation.
with open(args.file, "r") as fp:
    text = fp.read()

# let's create an array of the lines
lines = text.split(args.input_delimiter)

# Remove blank lines
if args.blank_lines:
    print('Removing blank lines...')
    temp = ''
    for i in lines:
        if len(i) != 0:
            temp+='\n'+i
 
    # lines now = temp split, minus the first element which is an empty element
    lines = temp.split('\n')[1:]  

# 
if args.keyword_delete_before != None:
    print('removing text before delete keyword...')
    temp = ''

    # loop through all elements in the lines array
    for i in lines:
        # 
        new = i.split(args.keyword_delete_before)
        if len(new)>1:
            t = new[1:]
            ret = ''
            for a in t:
                ret+=a+args.keyword_delete_before
        else:
            ret = i
        temp+='\n'+ret
    
    # lines now = temp split, minus the first element which is an empty element
    lines = temp.split('\n')[1:]   

# 
if args.keyword_delete_after != None:
    print('removing text after delete keyword...')
    temp = ''

    # loop through all elements in the lines array
    for i in lines:
        # 
        new = i.split(args.keyword_delete_after)
        if len(new)>1:
            t = new[:1]
            ret = ''
            for a in t:
                ret+=a+args.keyword_delete_after
        else:
            ret = i
        temp+='\n'+ret
    
    # lines now = temp split, minus the first element which is an empty element
    lines = temp.split('\n')[1:]          

# Remove lines that are UNDER min character requirements
if args.character_min > 0:
    print('Removing lines under min character requirements...')
    temp = ''
    for i in lines:
        if len(i) > args.character_min-1:
            temp+='\n'+i

    # lines now = temp split, minus the first element which is an empty element
    lines = temp.split('\n')[1:]        

# Remove lines that are OVER max character requirements
if args.character_max != None:
    print('Removing lines over max character requirements...')
    temp = ''
    for i in lines:
        if len(i) < args.character_max+1:
            temp+='\n'+i

    # lines now = temp split, minus the first element which is an empty element
    lines = temp.split('\n')[1:]        

# this checks if there is a removal keyword & performs this operation if so
if args.keyword_removal != None:
    print('removing lines with removal keyword...')

    temp = ''

    # 
    if ("*." in args.keyword_removal):
        print("file used!")
        print('Reading filter keywords...')

        # open the keyword keep file & save a reference to its contents
        with open(args.keyword_removal.replace('*',''), "r") as fp:
            filt = fp.read().split('\n')

        keeper = []

        print('filter keywords from file...')
        # now we break up the lines, break up the filter keywords, then compare each word
        for i in lines:
            for j in (i.split()):
                for k in filt:
                    if j != k and i not in keeper:
                        keeper.append(i)
                        temp += '\n'+i
        
        # lines now = temp split, minus the first element which is an empty element
        lines = temp.split('\n')[1:]
    else:

        # loop through all elements in the lines array
        for i in lines:
            # if not containing the removal keyword, then add it to temp
            if args.keyword_removal not in i:
                temp+='\n'+i
        
        # lines now = temp split, minus the first element which is an empty element
        lines = temp.split('\n')[1:]

# this checks if there is a removal keyword & performs this operation if so
if args.keyword_keep != None:
    print('removing lines without keep keyword...')

    temp = ''

    # 
    if ("*." in args.keyword_keep):
        print("file used!")
        print('Reading filter keywords...')

        # open the keyword keep file & save a reference to its contents
        with open(args.keyword_keep.replace('*',''), "r") as fp:
            filt = fp.read().split('\n')

        keeper = []

        print('filter keywords from file...')
        # now we break up the lines, break up the filter keywords, then compare each word
        for i in lines:
            for j in (i.split()):
                for k in filt:
                    if j == k and i not in keeper:
                        keeper.append(i)
                        temp += '\n'+i
        
        # lines now = temp split, minus the first element which is an empty element
        lines = temp.split('\n')[1:]
    else:
        print("keyword used!")

        # loop through all elements in the lines array
        for i in lines:
            # if not containing the removal keyword, then add it to temp
            if args.keyword_keep in i:
                temp+='\n'+i
        
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

# 
if args.keyword_add_end != None:
    print('adding keyword to end...')
    temp = ''
    
    for i in lines:
        temp+='\n'+i+args.keyword_add_end

    # lines now = temp split, minus the first element which is an empty element
    lines = temp.split('\n')[1:]

# set the name of the new converted file
if not args.out:
    if args.replace_file:
        print('replacing orginal file...')
        args.out = args.file
    else:
    # ok this is a little bit obscure but its reverse splitting an string into
    # a list once so 'dir/file.txt' -> ['dir/file', 'txt']. then the '*' before
    # it when passed to format tells format to read the list as mulptiple args.
        args.out = "{}_lcNrD.{}".format(*args.file.rsplit(".", 1))

# shuffle the list of content if -s is added
if args.shuffle:
    print('shuffling content...')
    r.shuffle(lines)

# save the converted file
with open(args.out, "w") as fp:
    # strings are immutable in python so every time you add two strings together
    # its creating a brand new one. This gets quickly gets slow with lots of text
    # so we wanna do this as little as possible. Using join on the list means
    # we just make all the string concatenation opertations in one go.
    fp.write(args.output_delimiter.join(lines))

print('...& DONE!')
