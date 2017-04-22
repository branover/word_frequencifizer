# word_frequencifizer


## Description ##

This script uses the Yandex Mystem 3.0 morphological analyzer to read in a text file of Russian and output a frequency list after converting all words to their base.  Words are output in descending order of frequency, and can be output to a file (in CSV format) for easy import to Anki, or other flashcard programs.

## Installation ##

All you need to do for this to work is install one dependency:

`pip install pymystem3`

## Usage ## 
```
Usage: python main.py [options]

Options:

  -h, --help            									show this help message and exit
  
  -i FILENAME, --input=FILENAME           Read in from file
                        
  -o OUTFILE, --output=OUTFILE            Output to results to file
                        
  -d DIRECTORY, --directory=DIRECTORY     Read in from every file in directory
                        
  -q , --quantity                         Add the quantity to the word
                        
  -m MINIMUM, --minimum=MINIMUM           Minimum number of occurences before showing a word
                        
  -l LENGTH, --length=LENGTH              Maximum number of results to show (sorted by frequency)
                        
  -e EXCLUDE, --exclude=EXCLUDE           Load file with list of words to exclude from results (will also be converted to root word before comparison)```
