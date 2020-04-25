import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage.color import rgb2lab
import cv2
from PIL import Image
import collections
import pandas as pd
import os
from collections import OrderedDict


def load_lab_csv_list(lab_list_name):
    dic = OrderedDict()
    color = pd.read_csv(lab_list_name).drop("Unnamed: 0", axis=1)
    for i,v in color.iterrows():
        dic[v[0],v[1]]=np.array([v['L'],v['A'],v['B']])
    lab_list=list(dic.values())
    color_name=list(dic.keys())
    return lab_list, color_name

def get_2d_image(img, crop_ratio = 10, resize=150):
    img=cv2.resize(img, (resize, resize))
    rgb_1d = img.reshape(-1,3)
    return rgb_1d

def load_rgb_image(image_file):
    # cv2 load images as BGR
    image_bgr=np.asarray(Image.open(image_file))
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    return image_rgb

def get_lab_from_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


def extract_main_color(two_dim_img, num_clusters = 5, plot=None):
    def centroid_histogram(clt):
        numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins = numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()
        return hist
  
    def plot_colors(hist, centroids):
        bar = np.zeros((50, 300, 3), dtype = "uint8")
        startX = 0
        for (percent, color) in zip(hist, centroids):
            endX = startX + (percent * 300)
            cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                          color.astype("uint8").tolist(), -1)
            startX = endX
        return bar
    clt = KMeans(n_clusters = num_clusters)
    clt.fit(two_dim_img)
    hist = centroid_histogram(clt)
    main_colors = plot_colors(hist, clt.cluster_centers_)
    if plot:
        plt.figure()
        plt.imshow(main_colors)
        plt.show()
    return main_colors




def get_topN_color(color_name, lab_list, c1, c2, c3):
    def lab_distance_dic(n_color):
        dics = OrderedDict()
        for name,lab_value in zip(color_name, lab_list):
            dics[name]=np.linalg.norm(lab_value - n_color)
        return dics

    def return_topn_color(n_color):
        dic_n = lab_distance_dic(n_color)
        return [k for k, v in dic_n.items() if v == min(dic_n.values())]

    top1_color = return_topn_color(c1)
    top2_color = return_topn_color(c2)
    top3_color = return_topn_color(c3)
    return top1_color, top2_color, top3_color

