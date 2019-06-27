#!/usr/bin/env python3

import os
import sys

def parse_file(path):
    """
    分析给定文本文件，返回其空格、制表符、行的有关信息

    ：arg path：要分析的文本文件的路径

    ：return: 包含空格数、制表符数、行数的元组
    “”“
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
   #现在关闭打开的文件
    fd.close()

     
