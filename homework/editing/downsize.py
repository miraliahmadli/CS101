import os
import sys
root_dir = os.path.realpath(__file__)
while not root_dir.endswith("CS101"):
  root_dir = os.path.dirname(root_dir)
# root_dir = os.path.join(root_dir, "cs101_libraries_py35")
sys.path.append(root_dir)

from cs101_libraries_py35.cs1media import *

## Do not change the name and parameter of function
def reduce(input_image):
    w, h = input_image.size() ## Do not modify this line
    output_image = create_picture(w // 2, h // 2) ## Do not modify this line
    
    ### Your code ###
    for i in range(0, w-1, 2):
        for j in range(0, h-1, 2):
            r1, g1, b1 = input_image.get(i, j)
            r2, g2, b2 = input_image.get(i+1, j)
            r3, g3, b3 = input_image.get(i, j+1)
            r4, g4, b4 = input_image.get(i+1, j+1)

            r_mean = (r1 + r2 + r3 + r4) // 4
            b_mean = (b1 + b2 + b3 + b4) // 4
            g_mean = (g1 + g2 + g3 + g4) // 4
            color = (r_mean, g_mean, b_mean)

            output_image.set(i // 2, j // 2, color)

    ### End of your code ###
    
    return output_image ## Do not modify this line


if __name__ == '__main__':
    image = load_picture('../../images/sherlock.jpg')
    w, h = image.size()
    print("Original image's size: {} X {}".format(w, h))
    reduced_image = reduce(image) # Example input
    w, h = reduced_image.size()
    print("Reduced image's size: {} X {}".format(w, h))
    reduced_image.show() # See your modification
