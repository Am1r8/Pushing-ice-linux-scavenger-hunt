import os

path = r"/home/{USERNAME}/Desktop/scavenger-hunt/clues/"
os.chdir(path)
print(os.getcwd())
list = os.listdir()
print(list)
for folder in list:
    with open(folder+'/clue', 'r') as reader:
        for line in reader:
            if "Nothing to see" in line:
                continue
            else:
                print(folder)
