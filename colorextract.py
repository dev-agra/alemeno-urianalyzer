import colorgram as cg

import turtle as t

import webcolors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

colors = cg.extract('strip_images/image3.jpg', 10**2*2)

rgb_colors = []

t.speed(100)

screen = t.Screen()

rgb_colors = []
for coloring in colors:
    r = coloring.rgb.r
    g = coloring.rgb.g
    b = coloring.rgb.b
    new_color = (r, g, b)
    requested_colour = new_color
    actual_name, closest_name = get_colour_name(requested_colour)
    rgb_colors.append(new_color)

print(rgb_colors)
# print("Actual colour name:", actual_name, ", closest colour name:", closest_name)