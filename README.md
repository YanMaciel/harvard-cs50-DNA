# Academic Honesty
If you are taking Harvard's CS50 - Introduction to Computer Science course you **must follow the course's [Academic Honesty philosophy](https://cs50.harvard.edu/x/2021/honesty/)**.

It is not reasonable to access a solution to some assessement prior to (re-)submitting your own.

The essence of all work that you submit to the CS50 course **must be your own**. 

# DNA
In this exercise we needed to implement a command-line application using Python that first asks the user to type in some text, and then outputs the grade level for the text, according to the Coleman-Liau formula.

The Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

# How it works
This is a command-line application fully developed in **Python**.

The task was to implement Coleman-Liau index formula in Python coding and to implement efficient functions to count the number of letters, words, and sentences in the text.

In total I implemented four functions: 

1. To count how many letters;
2. To count how many words;
3. To count how many sentences;
4. And to apply the Coleman-Liau index formula.
  
# What I learned
In this exercise, I got a better grasp on how to define functions and struct a command-line program using Python. 

Despite being a simple application, this exercise was very useful for me to better understand and adapt to Python.

I again tried my best to keep my code clean and organized, and got a 100% grade in correctness, design and style.

# Usage
To use and test this program, you will need [CS 50 Library](https://cs50.readthedocs.io/libraries/cs50/python/) and [Python](https://www.python.org/downloads/). Copy this repository and through the command-line, enter the program's folder and run the following command:

    $ python readability.py

The application will request a text so it can grade it according to the Coleman-Liau index formula. The program should behave per the example below.

    $ python readability.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3
    
