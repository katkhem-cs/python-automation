with open("string-split.txt", "r") as file:
    for line in file:
        print(line.split()[0])
