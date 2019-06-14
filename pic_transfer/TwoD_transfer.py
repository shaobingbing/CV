import cv2 as cv
import numpy as np
import random

class transfer():
    def  __init__(self, pic_file, save_dir):
        self.pic_file = pic_file
        self.save_dir = save_dir

    def crop(self):
        pass

    def resize(self):
        img = cv.imread(self.pic_file)
        # first method
        res = cv.resize(img, None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC)
        cv.imshow('img', res)
        cv.waitKey(0)
        cv.destoryALLWindows()

    def show_BGR(self):
        img = cv.imread(self.pic_file)
        B, G, R = cv.split(img)

        cv.imshow('B channel', B)
        cv.imshow('G channel', G)
        cv.imshow('R channel', R)
        cv.waitKey(0)
        cv.destoryALLWindows()


    def random_light_color(self):
        img = cv.imread(self.pic_file)
        B, G, R = cv.split(img)

        b_rand = random.randint(-50, 50)

        if b_rand == 0:
            pass
        if b_rand < 0:
            lim = 0 - b_rand
            B[B < lim] = 0
            B[B >= lim] = (b_rand + B[B >= lim]).astype(img.dtype)
        if b_rand > 0:
            lim = 255 - b_rand
            B[B > lim] = 255
            B[B <= lim] = (b_rand + B[B <= lim]).astype(img.dtype)


        g_rand = random.randint(-50, 50)
        if g_rand == 0:
            pass
        if g_rand < 0:
            lim = 0 - g_rand
            G[G < lim] = 0
            G[G >= lim] = (g_rand + G[G >= lim]).astype(img.dtype)
        if g_rand > 0:
            lim = 255 - g_rand
            G[G > lim] = 255
            G[G <= lim] = (g_rand + G[G <= lim]).astype(img.dtype)

        r_rand = random.randint(-50, 50)
        if r_rand == 0:
            pass
        if r_rand < 0:
            lim = 0 - r_rand
            R[R < lim] = 0
            R[R >= lim] = (r_rand + R[R >= lim]).astype(img.dtype)
        if r_rand > 0:
            lim = 255 - r_rand
            R[R > lim] = 255
            R[R <= lim] = (r_rand + R[R <= lim]).astype(img.dtype)

        img_merge = cv.merge((B,G,R))
        cv.imshow('random_light_color', img_merge)
        cv.waitKey(0)
        cv.destoryALLWindows()

    def crop(self):
        pass