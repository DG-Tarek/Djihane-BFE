import csv

PATH = "data/AQS2022.csv"
RESULT_PATH = "result/part_of_day.csv"
MORNING = [
    str(i) for i in range(8, 13)
]  # Morning time from 8:00 to 12:00 => [8, 9, 10, 11, 12]
AFTERNOON = [str(i) for i in range(12, 18)]  # Afternon time from 12 to 17:00
EVENING = [str(i) for i in range(18, 23)]  # Evning time from 17 to 22:00
NIGHT = [str(i) for i in range(22, 24)] + [
    str(i) for i in range(0, 9)
]  # Night time from 22:00 to 8:00


def get_part_of_day(time):
    time = time.split(":")[0]  # String into a list and the specified separator is ":" .
    # this means split(7:00) will return ["07","00"]

    if time[0] == "0":  # if time is "07" will remove "0", just keep the 7.
        time = time[1:]
    try:
        if time in MORNING:
            return "morning"
        if time in AFTERNOON:
            return "Afternoon"
        if time in EVENING:
            return "evening"
        if time in NIGHT:
            return "night"
    except:
        return ""


def read_data_from_csv(path):
    """Read data from csv file"""
    data = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(line)
    return data


DATA = read_data_from_csv(path=PATH)  # Reading data from csv file


def add_part_of_day(data):
    """Add part of day to the last column of table and return a new table (data)"""
    data_with_pod = []
    for line in data:
        if line[0]:
            pard_of_day = get_part_of_day(line[0])
            if pard_of_day:
                data_with_pod += [line + [pard_of_day]]
            else:
                data_with_pod += [line]

    return data_with_pod


data_with_part_of_day = add_part_of_day(data=DATA)  # Add part of dat to the table


def write_csv_file(data):
    """Write new data(Table) as a csv file."""
    with open(RESULT_PATH, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        for line in data:
            writer.writerow(line)


write_csv_file(data=data_with_part_of_day)  # Writing data as a csv file
