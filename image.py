# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from PIL import Image, ImageFilter


class ImageRecognitionWordProcessing(object):
    @staticmethod
    def process_image():
        kitten = Image.open("files/Snipaste_2022-04-06_10-36-03.png")
        blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
        blurryKitten.save("files/Snipaste_2022-04-06_10-36-03_new.png")
        blurryKitten.show()

    @staticmethod
    def clean_file(file_path, new_file_path):
        image = Image.open(file_path)

        # 对图片进行阈值过滤，然后保存
        image = image.point(lambda x: 0 if x < 180 else 255)
        image.save(new_file_path)


if __name__ == '__main__':
    ImageRecognitionWordProcessing().clean_file(os.path.join(os.getcwd(), "files/test-text_has_symbol.max_340x194.jpg"),
                                                "text_2_clean.png")
