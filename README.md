# lcNrD v1.7

lowercase AND remove Duplicates - A Very Simple Program;

I find myself having to clean up data quite often & lose python scripts that I write for data cleaning. So I've decided to start this lcNrD project that is a but more of a permanent solution & I will add to its usefulness as I see fit.

## Current Functionality:
* Set input delimiter
* Set output delimiter
* Lowercase the text of a file
* Remove duplicates of a file
* Copy all operations onto a new file
* Remove lines containing a removal keyword
* Removes all lines except ones that contain a keep keyword
* Remove everything except ones that matches Regular Expression
* keep only lines with a min & max amount of characters

## Program Arguments: (* = required)

```
  -v, --version         Show program's version number and exit.
  -h, --help            ** = required
  -f FILE, --file FILE  ** this is the file you're targeting to get the lcNrD
                        treatment (default: None)
  -o OUT, --out OUT     this is the file you want the lcNrD file to output as.
                        Default = same name + _LcNrD (default: None)
  -id INPUT_DELIMITER, --input_delimiter INPUT_DELIMITER
                        this is the delimiter you want lcNrD to use for the
                        input file (default: \n)
  -od OUTPUT_DELIMITER, --output_delimiter OUTPUT_DELIMITER
                        this is the delimiter you want lcNrD to use for the
                        output file. Default = input delimiter (default: None)
  -d, --duplicates      add -d to remove duplicate elements (default: False)
  -s, --shuffle         add -s to shuffle your list (default: False)
  -rf, --replace_file   add -rf to replace the original file after lcnrd
                        operation (default: False)
  -bl, --blank_lines    add -bl to remove all blank lines (default: False)
  -cmi CHARACTER_MIN, --character_min CHARACTER_MIN
                        limits the minimal amount of chacters required
                        (default: 0)
  -cma CHARACTER_MAX, --character_max CHARACTER_MAX
                        limits the maximum amount of chacters required
                        (default: None)
  -kr KEYWORD_REMOVAL, --keyword_removal KEYWORD_REMOVAL
                        add a -kr to remove lines with the removal keyword,
                        use *.txt or whatever to point to a list of kr
                        (default: None)
  -kk KEYWORD_KEEP, --keyword_keep KEYWORD_KEEP
                        add a -kk to keep only the lines with the keep
                        keyword, use *.txt or whatever to point to a list of
                        kk (default: None)
  -kdb KEYWORD_DELETE_BEFORE, --keyword_delete_before KEYWORD_DELETE_BEFORE
                        add a -kdb to delete all text before the delete before
                        keyword (default: None)
  -kda KEYWORD_DELETE_AFTER, --keyword_delete_after KEYWORD_DELETE_AFTER
                        add a -kda to delete all text after the delete after
                        keyword (default: None)
  -kae KEYWORD_ADD_END, --keyword_add_end KEYWORD_ADD_END
                        add a -kae to add some text to the end of every line
                        (default: None)
```
## Using the .exe
The standalone exe works just like the python script, but has all dependencies packaged with it. Follow these steps to use it if on Windows:
1. Enter the 'dist' folder, or any folder containing lcnrd.exe
2. Open your terminal of choice
3. type `.\lcnrd -h` to see all availible options

If you'd like to be able to access lcnrd from anywhere on your computer, add the 'dist' folder into your environment variables, you can do that by:
1. Going to Start on Windows (or press the windows key)
2. Search for "Edit the system Environment Variables" (just start typing if that start menu is up to search)
3. Click that option
4. Click Environment Variables button at the bottom
5. In System Variables panel, look for "Path"
6. Add the full directory to 'dist' to this list of environment variables
7. You should now from anywhere on your computer be able to type simply `lcnrd -h` from a terminal & it should work!

## Roadmap:
