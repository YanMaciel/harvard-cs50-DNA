# Academic Honesty
If you are taking Harvard's CS50 - Introduction to Computer Science course you **must follow the course's [Academic Honesty philosophy](https://cs50.harvard.edu/x/2021/honesty/)**.

It is not reasonable to access a solution to some assessement prior to (re-)submitting your own.

The essence of all work that you submit to the CS50 course **must be your own**. 

# DNA
## Background
Basically DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Every human cell has billions of these nucleotides arranged in sequence. Some portions of this sequence (i.e. genome) are the same, or at least very similar, across almost all humans, but other portions of the sequence have a higher genetic diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals.
In this exercise we needed to implement a command-line application using Python that first asks the user to type in some text, and then outputs the grade level for the text, according to the Coleman-Liau formula.

## Task for the application
The task was to write a program that took a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs.

# How it works
This is a command-line application fully developed in **Python**.

The task was open and read a CSV-database file and a txt file with sequences of DNA of a person using Python and implement an application that identifies the person based on their DNA.

# What I learned
In this exercise, I got to better understand how to use lists and dictionaries in Python, two powerful tools of the language. Also learned the basics on how to manage files in Python.

I had the chance to think thorugh the best way to formulate the function (count_STR) that counts STR from the .txt file and came up with a solution using basic operations after trying and error other 'complex' ways.

I again tried my best to keep my code clean and organized, and got a 100% grade in correctness, design and style.

# Usage
To use and test this program, you will need [CS 50 Library](https://cs50.readthedocs.io/libraries/cs50/python/) and [Python](https://www.python.org/downloads/). Copy this repository and through the command-line, enter the program's folder and run the following command:

    $ python dna.py

The program requires as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and as its second command-line argument the name of a text file containing the DNA sequence to identify. 

If the STR counts match exactly with any of the individuals in the CSV file, the program prints out the name of the matching individual.

If the STR counts do not match exactly with any of the individuals in the CSV file, the program prints "No match".

The program should behave per the examples below.

    $ python dna.py databases/large.csv sequences/5.txt
    Lavender
    
 or
 
    $ python dna.py databases/large.csv sequences/14.txt
    Severus
    
 and so on.
    
