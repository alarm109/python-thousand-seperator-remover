import sys
import os
import csv


class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_yellow(text: str):
    print(Color.YELLOW + text + Color.END)


def print_green(text: str):
    print(Color.GREEN + text + Color.END)


def print_red(text: str):
    print(Color.RED + Color.BOLD + text + Color.END)


if len(sys.argv) == 2:
    fileName = sys.argv[1]
    resultFileName = "result.csv"

    print(f'{Color.BOLD + "File name " + Color.END: <15} -> {fileName}')

    if not fileName.split(".")[-1] == "csv":
        print_red(f"File ({fileName}) extension is not csv")
        exit(1)

    if not os.path.isfile(fileName):
        print_red(f'File ({fileName}) does not exist')
        exit(1)

    print_green("🚀 File format is correct")
    print_green("Starting to read file...")

    result = []

    with open(fileName, "r") as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for i, line in enumerate(reader):
            newLine = line
            newLine[1] = newLine[1].replace(",", "").replace(".", ",")
            result.append(newLine)

    with open(resultFileName, mode='w') as f:
        employee_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in result:
            employee_writer.writerow(i)

    print_green(f"🚀 File saved as {resultFileName}")
else:
    print_red('Please provide a file name as an argument.')