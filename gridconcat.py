import cv2
import numpy as np

im1 = cv2.imread('/Users/srisagarkalisetty1/Downloads/MyPic.jpg')
im_v = cv2.hconcat([im1, im1])

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

im1_s = cv2.resize(im1, dsize=(0, 0), fx=0.5, fy=0.5)

im_tile = concat_tile([[im1_s, im1_s, im1_s, im1_s],
                       [im1_s, im1_s, im1_s, im1_s],
                       [im1_s, im1_s, im1_s, im1_s]])

def concat_tile_resize(im_list_2d, interpolation=cv2.INTER_CUBIC):
    im_list_v = [hconcat_resize_min(im_list_h, interpolation=cv2.INTER_CUBIC) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v, interpolation=cv2.INTER_CUBIC)

im_tile_resize = concat_tile_resize([[im1],
                                     [im1, im2, im1, im2, im1],
                                     [im1, im2, im1]])


cv2.imshow('sagar', im_v)
cv2.waitKey(0)
cv2.destroyAllWindows()