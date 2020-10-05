import os
import sys
root_dir = os.path.realpath(__file__)
while not root_dir.endswith("CS101"):
  root_dir = os.path.dirname(root_dir)
# root_dir = os.path.join(root_dir, "cs101_libraries_py35")
sys.path.append(root_dir)

from cs101_libraries_py35.cs1media import *


def get_blur_rgb(input_image, i, j, n):
    size = n*n
    mid = n//2
    r_mean = 0
    g_mean = 0
    b_mean = 0
    for x in range(i-mid, i+mid+1, 1):
        for y in range(j-mid, j+mid+1, 1):
            r, g, b = input_image.get(x, y)
            r_mean += r
            g_mean += g
            b_mean += b
    r_mean //= size
    g_mean //= size
    b_mean //= size
    return (r_mean, g_mean, b_mean)


## Do not change the name and parameter of function
def blur(input_image, blur_area_center, blur_area_size, n):
    ## ---------- Do not modify the code block below ----------
    w, h = input_image.size()
    output_image = create_picture(w, h)
    for i in range(w):
        for j in range(h):
            output_image.set(i, j, input_image.get(i, j))
    ## ---------------------------------------------------------
    
    ### Your code ###
    x, y = blur_area_center
    r_size = blur_area_size // 2
    for i in range(x-r_size, x+r_size + 1, 1):
        for j in range(y-r_size, y+r_size + 1, 1):
            blur_color = get_blur_rgb(input_image, i, j, n)
            output_image.set(i, j, blur_color)
    
    
    ### End of your code ###
    
    return output_image ## Do not modify this line


if __name__ == '__main__':
    image = load_picture('../../images/sherlock.jpg')
    blurred_image = blur(image, (200, 200), 151, 21) # Example input
    blurred_image.show() # See your modification
