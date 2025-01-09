condition = True
fname = input(f"Please enter a file name to count: ")

while(condition):
    try:
        f = open(fname, "r")
        condition = False
    except Exception:
        fname = input(f"The name caused an error, {Exception}, please try again: ")
print("The file opened succesfully")
f.close()
