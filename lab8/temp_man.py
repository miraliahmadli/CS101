def read_file(fname):
    temps = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            year = list(map(float, line.split()))
            temps.append(year)       
    
    return temps


def print_avg(temps):
    cur_yr = 1723
    for year in temps:
        winter = (year[0] + year[1]) / 2
        summer = (year[6] + year[7]) / 2
        print("Year %d, Winter average %f, Summer average %f", % (cur_yr, winter, summer))
        cur_yr += 1


def write_csv(out_file, temps):
    cur_yr = 1723
    with open(out_file, 'w+') as outfile:
        for year in temps:
            avg = sum(year) / 12
            line = str(cur_yr) + "," + str(avg) + "\n"
            outfile.write(line)


def main():
    fname = "tpmon.txt"
    temps = read_file(fname)
    print_avg(temps)
    out_file = "tpmon.csv"
    write_csv(out_file, temps)

main()