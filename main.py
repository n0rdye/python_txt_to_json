import json

with open("note.txt") as f:
    content = f.readlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
# for line in content:
#     print(line)

a=[]
i=0
List = {}
for line in content:
    line = line.replace("\n","")
    # print(line)
    # a[i]+=line
    a.append(line)
    i+=1
# print(a[1])

i=0

for data in a:
    spl = data.split("|")
    if len(spl)<3:
        pill = data.split("|")[-1]
        date = data.split("|")[-2]
        # print(date)
        pill_name = "pill_"+str(i)
        List[pill_name] = {}
        List[pill_name]["date"] = date
        List[pill_name]["pill"] = pill
        List[pill_name]["comment"] = "-"
        # List["s"] = "sd"
        i+=1
    else: # with comments
        pill = data.split("|")[-2]
        comm = data.split("|")[-1]
        date = data.split("|")[-3]
        # print(pill)
        pill_name = "pill_"+str(i)
        List[pill_name] = {}
        List[pill_name]["date"] = date
        List[pill_name]["pill"] = pill
        List[pill_name]["comment"] = comm
        # List["s"] = "sd"
        i+=1
    # print(data)

  
with open('convert.txt', 'w') as convert_file:
     convert_file.write(json.dumps(List))

# f = open("demofile3.txt", "w")
# f.write(List)
# f.close()
# print(List["pill_401"]["date"])
