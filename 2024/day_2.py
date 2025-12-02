filename = "inputs/day_2_data.txt"

with open(filename) as f:
    mylist = f.read().splitlines()

reports = []
for line in mylist:
    line.split(" ")
    reports.append(list(map(int, line.split(" "))))

unsafe_count = 0
safe_list = []

for report in reports:
    print(report)
    curr = 0
    next = 1

    if 1 <= report[curr] - report[next] <= 3:
        while next < len(report):
            if 1 <= report[curr] - report[next] <= 3:
                curr += 1
                next += 1
            else:
                print("unsafe 1")
                unsafe_count += 1
                break

    elif 1 <= report[next] - report[curr] <= 3:
        while next < len(report):
            if 1 <= report[next] - report[curr] <= 3:
                curr += 1
                next += 1
            else:
                print("unsafe 2")
                unsafe_count += 1
                break

    else:
        print("unsafe 3")
        unsafe_count += 1

print(len(reports) - unsafe_count)
