def extract_line(line):
    st = 0
    lst = []
    line = line.replace('"', "")
    for i in range(len(line)):
        if line[i] == ",":
            if line[i+1] == " ":
                continue
            else:
                lst.append(line[st : i])
                st = i+1
    lst.append(line[st:])
    return lst


def read_file(fname):
    names = []
    coors = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            code, name, lat, lon = extract_line(line)
            lat, lon = float(lat), float(lon)
            names.append((code, name))
            coors.append((code, lat, lon))
    
    return names, coors

def print_south(names, coors):
    for (code, name), (_, lat, lon) in zip(names, coors):
        if 0 > lat:
            print(name)

def print_name(code, names):
    for cd, name in names:
        if cd == code:
            print(name)
            return
    print("Sorry this code don't exist in our DB")

def main():
    fname = "average-latitude-longitude-countries.csv"
    names, coors = read_file(fname)
    print_south(names, coors)

    code = input("Enter country code: ")
    print_name(code, names)

main()