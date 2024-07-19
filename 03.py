import os
import sys
import collections

def main():
    file_path = ""
    level = ""
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else: print("Provide file path")
    if len(sys.argv) > 2:
        level = sys.argv[2]
    if file_path:
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        if level:
          display_logs_for_level(level, logs)



def load_logs(file_path: str):
    lines = list()
    try:
        with open(file_path) as file:
            lines = file.readlines()
    except:
        print("Error while read file")
        return lines
    return lines

def parse_log_line(line: str):
     try:
        words = line.split(" ")
        date = words[0]
        time = words[1]
        level = words[2]
        return {"time": time, "date": date,"level":level, "log":line}
     except:
         return {}


def filter_logs_by_level(logs: list, level: str):
   return filter(lambda line:level.lower() == parse_log_line(line)["level"].lower(),logs)

def count_logs_by_level(logs: list) -> dict:
    levels = map(lambda line:parse_log_line(line)["level"],logs)
    return collections.Counter(levels)

def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def display_logs_for_level(level:str, logs:list):
      print(f"Деталі логів для рівня '{level.upper()}':")
      for i in filter_logs_by_level(logs, level):
        print(i.strip())

if(__name__ == "__main__"):
    main()