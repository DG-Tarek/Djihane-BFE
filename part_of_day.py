import csv

PATH = "data/AQS2022.csv"
RESULT_PATH = "result/part_of_day.csv"
MORNING = [str(i) for i in range(8, 13)]
AFTERNOON = [str(i) for i in range(12, 18)]
EVENING = [str(i) for i in range(18, 23)]
NIGHT = [str(i) for i in range(22, 24)] + [str(i) for i in range(0, 9)]


def get_part_of_day(time):
    time = time.split(":")[0]

    if time[0] == "0":
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
    data = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(line)
    return data


DATA = read_data_from_csv(path=PATH)


def add_part_of_day(data):
    data_with_pod = []
    for line in data:
        if line[0]:
            pard_of_day = get_part_of_day(line[0])
            if pard_of_day:
                data_with_pod += [line + [pard_of_day]]
            else:
                data_with_pod += [line]

    return data_with_pod


data_with_part_of_day = add_part_of_day(data=DATA)


def write_csv_file(data):
    with open(RESULT_PATH, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        for line in data:
            writer.writerow(line)


write_csv_file(data=data_with_part_of_day)
