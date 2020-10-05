import os
import sys
root_dir = os.path.realpath(__file__)
while not root_dir.endswith("CS101"):
  root_dir = os.path.dirname(root_dir)
# root_dir = os.path.join(root_dir, "cs101_libraries_py35")
sys.path.append(root_dir)

from cs101_libraries_py35.cs1media import *

def get_mean_rgb_from_square(input_image, i, j, n):
    size = n*n
    r_mean = 0
    g_mean = 0
    b_mean = 0
    for x in range(n):
        for y in range(n):
            r, g, b = input_image.get(i+x, j+y)
            r_mean += r
            g_mean += g
            b_mean += b
    r_mean //= size
    g_mean //= size
    b_mean //= size
    return (r_mean, g_mean, b_mean)


## Do not change the name and parameter of function
def reduce(input_image, factor):
    w, h = input_image.size() ## Do not modify this line
    output_image = create_picture(w // factor, h // factor) ## Do not modify this line
    
    ### Your code ###
    out_w = w // factor
    out_h = h // factor
    for i in range(out_w):
        for j in range(out_h):
            color = get_mean_rgb_from_square(input_image, i * factor, 
                                            j * factor, factor)

            output_image.set(i, j, color)
    
    ### End of your code ###
    
    return output_image ## Do not modify this line


if __name__ == '__main__':
    image = load_picture('../../images/sherlock.jpg')
    w, h = image.size()
    print("Original image's size: {} X {}".format(w, h))
    reduced_image = reduce(image, 4) # Example input
    w, h = reduced_image.size()
    print("Reduced image's size: {} X {}".format(w, h))
    reduced_image.show() # See your modification
