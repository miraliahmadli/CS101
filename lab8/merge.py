from time import sleep

def merge(input_filenames, output_filename):
    with open(output_filename, 'w+') as outfile:
        for fname in input_filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

merge(['kaist1.txt', 'kaist2.txt', 'kaist3.txt'], 'output.txt')

sleep(0.5) # Wait 0.5 seconds before creating a download link.
# elice_utils.send_file('output.txt')