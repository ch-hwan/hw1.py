# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GdnmeTXVCJhcB2f8JoDKD4zG3rc3CxTQ
"""

!mkdir circle_calculator
!cd circle_calculator
!git init

import math

def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    radius = get_radius("원의 반지름을 입력하세요: ")
    area = get_circle_area(radius)
    print(f"반지름 {radius}인 원의 넓이는 {area:.2f}입니다.")



