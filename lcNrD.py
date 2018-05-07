import matplotlib.pyplot as plt
import os
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--target', type=str, help='this is the file you\'re targeting to get the lcNrD treatment')
    parser.add_argument('--outputName', type=str, help='this is the file you want the lcNrD file to output as')
    parser.add_argument('--lowercase', type=str, default='T', help='T = lowercase all, F = keep original')
    parser.add_argument('--removeDups', type=str, default='T', help='T = lowercase all, F = keep original')
    args = parser.parse_args()
    
    execute(args)

def execute(args):
    print('Grabbing file contents...')

    # open the target file & grab its contents
    targetFile = open(args.target, 'r')
    allLines = targetFile.read().split('\n')
    targetFile.close()

    # we need a new array that holds all lines, but lowercased
    allLinesNew = [None]*len(allLines)

    # We need a new variable to store our final output
    allLinesFin = ''
 
    # Check if we want to lowercase file or not
    if args.lowercase.lower() == 't':
        print('lowercasing contents...')

        # Loop through & lowercase
        for i in range(len(allLines)):
            allLinesNew[i] = allLines[i].lower()
    else:
        allLinesNew = allLines

    if args.removeDups.lower() == 't':
        print('removing duplicates...')

        # Loop through & remove duplicates
        for i in range(len(allLines)):
            if allLinesNew[i]+'\n' not in allLinesFin:
                allLinesFin += allLinesNew[i]+'\n'
    else:
        # Loop through & remove duplicates
        for i in range(len(allLines)):
            allLinesFin += allLinesNew[i]+'\n'
    
    # segment the file directory, we just need the actual file name
    last =  targetFile.name.split('/')

    # set the name of the new converted file
    if args.outputName is None:
        nFile = last[len(last)-1].split('.')[0] + '_lcNrD.' + last[len(last)-1].split('.')[1]
    else:
        nFile = args.outputName
    
    print('saving lcNrD convert...')

    # save the converted file
    save = open(nFile,'w+')
    save.write(allLinesFin)
    save.close()

    print('...& DONE!')

main()