import csv
import sys
import argparse

def parse_args(argv):
    policy_file = ''
    data_file = ''
    parser = argparse.ArgumentParser(description = "Description for my parser")
    parser.add_argument("-H", "--Help", help = "Example: Help argument", required = False, default = "")
    parser.add_argument("-s", "--save", help = "Example: Save argument", required = False, default = "")
    parser.add_argument("-p", "--print", help = "Example: Print argument", required = False, default = "")
    parser.add_argument("-o", "--output", help = "Example: Output argument", required = False, default = "")

    argument = parser.parse_args()
    status = False

    if argument.Help:
        print("You have used '-H' or '--Help' with argument: {0}".format(argument.Help))
        status = True
    if argument.save:
        print("You have used '-s' or '--save' with argument: {0}".format(argument.save))
        status = True
    if argument.print:
        print("You have used '-p' or '--print' with argument: {0}".format(argument.print))
        status = True
    if argument.output:
        print("You have used '-o' or '--output' with argument: {0}".format(argument.output))
        status = True
    if not status:
        print("Maybe you want to use -H or -s or -p or -p as arguments ?") 

def open_csv_file(filename):
    with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

def precinct_count(audited, precincts):
    n = 4794
    total = 1
    for x in range(0, 299):
        total *= (n - x) / (n - x + 6)
    print(total)

if __name__ == "__main__":
   parse_args(sys.argv[1:])
   open_csv_file(policy_filename)
   open_csv_file(data_filename)
   precinct_count(300, 4800)