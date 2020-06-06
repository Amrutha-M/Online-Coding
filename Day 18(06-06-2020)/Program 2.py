#Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically

items=[n for n in input("enter the string separete by hyphen\n").split('-')]
items.sort()
print('-'.join(items))

output:
enter the string separete by hyphen
python-OS-OR-sscd-cnsc
cnsc-OR-OS-python-sscd