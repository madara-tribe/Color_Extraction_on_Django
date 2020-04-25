from myapp.funcs import load_lab_csv_list, get_2d_image, load_rgb_image, get_lab_from_list, extract_main_color, get_topN_color
from skimage.color import rgb2lab
import numpy as np
CSV = "myapp/templates/LAB_color_list.csv"
#query_name = 'dirs/1.jpeg'


def main(query_name):
    lab_list, color_name = load_lab_csv_list(CSV)
    rgb_img = load_rgb_image(query_name)

    #print('color clustering in image')
    dim2rgb = get_2d_image(rgb_img)
    rgb_colors = extract_main_color(dim2rgb)

    #print('extract main color')
    lab_colors = rgb2lab(rgb_colors)
    c1, c2, c3, _, _ = get_lab_from_list(lab_colors[0].tolist())
    top1,top2,top3 = get_topN_color(color_name, lab_list, c1, c2, c3)
    #print('main_color1 {}, main_color2 {}, main_color3 {}'.format(top1,top2,top3))
    return top1, top2, top3


if __name__ == '__main__':
    main()
