#!/bin/python3

# Mấy cái import này deo dùng k biết cho vào làm gì
import math
import os
import random
import re
import sys


if __name__ == '__main__': # kiểm tra code chạy live hay được import vào module khác
    n = int(input().strip()) # Đọc số nguyên sau khi nhập số đó vào và gán cho .strip() để loại bỏ khoảng trắng dư thừa sau khi nhập
    
    if n % 2 == 1: #Nếu n là số lẻ thì in ra Weird
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5: #Nếu n là số chẵn trong khoảng 2 đến 5 ( tính cả 2 và 5 ) thì in ra Not Weird
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20: ##Nếu n là số chẵn trong khoảng 6 đến 20 ( tính cả 6 và 20 ) thì in ra Weird
        print("Weird")
    elif n % 2 == 0 and n > 20: #Nếu n là số chẵn lớn hơn 20 thì in ra Not Weird
        print("Not Weird")    
                