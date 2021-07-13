# Checks if a particular DNA is in a DNA-database.

import csv
import sys


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py database.csv sequence.txt")

    data = []
    # Reads database into memory from csvfile.
    database = sys.argv[1]
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile)
        for name in reader:
            data.append(name)

    person = []
    # Reads sequences into memory from txtfile.
    sequences = sys.argv[2]
    txtfile = open(sequences, "r")
    person = txtfile.read()

    counts = {}
    # Uses count_STR funcion to count all the STRs in the person's sequence.
    # Gets the keys from one of the data list (list of dictionaries) to search those keys (STRs) the person's sequence (txt file).
    # Saves STR counts in 'counts' dictionary.
    STRS = list(data[1].keys())     # Lists data.keys in a list so we can take the names and search as STR.
    for i in range(0, len(data[0])):
        STR = STRS[i]
        count = count_STR(person, STR)
        counts[STR] = count
    counts_values = list(counts.values())  # Lists dict.values in a list so we can iterate.

    for i in range(0, len(data)):
        matches = 0  # Sets counter back to 0 inside the loop, not out.
        data_values = list(data[i].values())  # Lists data.values in a list so we can iterate.
        for j in range(0, len(data[0])):
            if data_values[j] == counts_values[j]:
                matches += 1
        if matches == len(data[0])-1:  # If matches == lenght-1 bcuz we dont count 'name'.
            print(f"{data_values[0]}")  # If it matches all, prints the name and exit.
            sys.exit()

    print("No Match")


# For each STR, computes the longest run of consecutive repeats in the DNA sequence.
# Counts the maximum consecutive substring (STR) in a string with basic operations.
# Adds one more STR to the end of the current to check if it is still in the DNA sequence (person) and adds +1 to the counter.


def count_STR(person, STR):
    STR_count = 0
    curr_STR = STR
    while curr_STR in person:
        STR_count += 1
        curr_STR += STR

    return str(STR_count)


if __name__ == "__main__":
    main()