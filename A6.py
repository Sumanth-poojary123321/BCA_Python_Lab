fname = input("Enter file name: ")


with open(fname, "w") as f:
    print("Enter the contents into file :")
    while True:
        try:
            f.write(input())
            f.write("\n")
        except EOFError:
            break


cc = 0
wc = 0
lc = 0
with open(fname, "r") as f:
    for line in f:
        lc += 1
        wc += len(line.split())
        cc += len(line.strip("\n"))

print(f"\nLines = {lc} \nWords = {wc} \nCharacters = {cc}")