# -*- coding: utf-8 -*-

from difflib import Differ
import numpy as np


class Baymax(object):
	
    def comparison(self, str1, str2):
        variation = 0 # degree of variation
        return variation

    def appendBoldChanges(self, s1, s2):
        "Adds <b></b> tags to words that are changed"
        l1 = s1.split(' ')
        l2 = s2.split(' ')
        dif = list(Differ().compare(l1, l2))
        return " ".join(['<b>'+i[2:]+'</b>' if i[:1] == '+' else i[2:] for i in dif if not i[:1] in '-?'])

    def leDistance(self, input_x, input_y):
        xlen = len(input_x) + 1  # 此处需要多开辟一个元素存储最后一轮的计算结果
        ylen = len(input_y) + 1

        dp = np.zeros(shape=(xlen, ylen), dtype=int)
        for i in range(0, xlen):
            dp[i][0] = i
        for j in range(0, ylen):
            dp[0][j] = j

        for i in range(1, xlen):
            for j in range(1, ylen):
                if input_x[i - 1] == input_y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[xlen - 1][ylen - 1]


    def run(self):
        inputfile = open('input.txt', 'r')
        sourcefile = open('source.txt', 'r')

        str1 = inputfile.read()
        str2 = sourcefile.read()
        print self.appendBoldChanges(str1, str2)
        print self.leDistance(str1, str2)

if __name__ == '__main__':
    Baymax().run()