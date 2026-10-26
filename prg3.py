def mapper(line):
    return tuple(line.strip().split(','))

def reducer(date,conditions):
    return date , max(set(conditions),key=conditions.count)

def main(input_file):
    with open(input_file,'r') as f:
        data = {}
        for line in f:
            date,conditions = mapper(line)
            data.setdefault(date, []).append(conditions)
        for date,condition in data.items():
            print(f"Weather on {date} : {reducer(date,condition)[1]}")

if __name__ == "__main__":
    main('weather.txt')

