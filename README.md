# lcNrD

lowercase AND remove Duplicates - A Very Simple Program;

I find myself having to clean up data quite often & lose python scripts that I write for data cleaning. So I've decided to start this lcNrD project that is a but more of a permanent solution & I will add to its usefulness as I see fit.

## Disclaimer:
As it stands, this program works best with text listed using the '\n' delimiter. I plan to soon add more delimiter options

## Current Functionality:
* Lowercase the text of a file
* Remove duplicates of a file
* Copy all operations onto a new file
* Remove lines containing a keyword

## Program Arguments: (* = required)

```
  -h, --help            show this help message and exit
* -f FILE, --file FILE  this is the file you're targeting to get the lcNrD
                        treatment (default: None)
  -o OUT, --out OUT     this is the file you want the lcNrD file to output as.
                        Default = same name + _LcNrD (default: None)
  -l, --lowercase       add -l to set lowercase to true (default: False)
  -d, --duplicates      add -d to remove duplicate elements (default: False)
  -rk REMOVAL_KEYWORD, --removal_keyword REMOVAL_KEYWORD
                        add -rk to remove lines with the removal keyword
                        (default: None)
```

## Roadmap:
* Add input delimiter
* Add output delimiter
* Add function that removes all lines except ones that contain a keyword