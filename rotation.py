# -*- coding: utf-8 -*-
"""
    rotation
    ~~~~~~~~

    Rotation by line. This module is basically used for shape / image rotation
    according to a line defined by two reference points.

    :copyright: (c) 2015 by Ming (i AT ufoym DOT com).
    :license: BSD, see LICENSE for more details.
"""

import math


class Rotation(object):
    """Line-based rotation"""
    def __init__(self):
        pass

    def get_degree(self, x1, y1, x2, y2):
        vx, vy = (x2 - x1, y2 - y1) if x2 > x1 else (x1 - x2, y1 - y2)
        deg = 90 + math.atan2(vx, vy) * 180 / math.pi
        return deg

if __name__ == '__main__':
    import cv2

    r = Rotation()

    curr_line = [None, None]
    curr_img = cv2.imread('test.png')
    cv2.namedWindow('rotation test')
    cv2.namedWindow('rotation result')

    def rotate(image, angle, method=cv2.INTER_LINEAR):
        h, w = image.shape[:2]
        center = w/2, h/2
        rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(image, rot_mat, (w, h), flags=method)

    def on_mouse(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            curr_line[0] = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            if curr_line[0] is not None and curr_line[1] is not None:
                angle = r.get_degree(curr_line[0][0], curr_line[0][1],
                                     curr_line[1][0], curr_line[1][1]) - 180
                cv2.imshow('rotation result', rotate(curr_img, angle))
        curr_line[1] = (x, y)

    cv2.setMouseCallback('rotation test', on_mouse, 0)
    while True:
        vis_img = curr_img.copy()
        if curr_line[0] is not None and curr_line[1] is not None:
            cv2.line(vis_img, curr_line[0], curr_line[1], 255)
        cv2.imshow('rotation test', vis_img)
        if cv2.waitKey(5) == 27:
            cv2.destroyAllWindows()
            break
