
import csv

with open("input.txt") as file:
    lines = csv.reader(file, delimiter=" ")
    ok = 0
    not_ok = 0
    valid = 0

    for line in lines:
        low = int(line[0].split("-")[0])
        high = int(line[0].split("-")[1])
        letter = line[1].replace(":", "")
        pw = line[2]

        # Case 1
        if pw.count(letter) >= low and pw.count(letter) <= high:
            ok = ok + 1
        else:
            not_ok += 1

        # Case 2

        if bool(pw[low - 1] == letter) ^ bool(pw[high - 1] == letter):
            valid += 1

    print("ok: {}, not ok: {}".format(ok, not_ok))
    print("Valid pwds: {}".format(valid))

