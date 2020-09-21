import math

sin = math.sin
pi  = math.pi

for i in range(41) :
    x = float(i) / 40.0 * 2 * pi
    character_count_per_line = 40 + int(sin(x) * 40) # Change this line to print out sine curve correctly.
    
    output_str = '#' * character_count_per_line
    print (output_str)
