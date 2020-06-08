#Python Program to Copy the Contents of One File into Another

with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
print("successful done")

output


new.txt:
hello,how r you
this is a python program


out.txt:
hello,how r you
this is a python program
