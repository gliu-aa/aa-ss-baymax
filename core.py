# -*- coding: utf-8 -*-
import diff_match_patch as dmp_module

class Baymax(object):

    MARK_DELETE = -1
    MARK_INSERT = 1
    MARK_EQUAL = 0

    DIFF_NOCHANGE = ("G000000", "DIFF_NOCHANGE", "Text is unchanged")
    DIFF_CUTOUT = ("G000001", "DIFF_CUTOUT", "Text has been cut out!")
    DIFF_NEW = ("G000002", "DIFF_NEW", "Text has been newed!")
    DIFF_LARGECHANGE = ("G000003", "DIFF_LARGECHANGE", "Text has a large change!")
    DIFF_NORMALCHANGE = ("G000004", "DIFF_NORMALCHANGE", "Text has a normal change!")
    DIFF_ABNORMALCHANGE = ("G000005", "DIFF_ABNORMALCHANGE", "Text has a abnormal change!")

    SYMBOL_ABNORMAL = ['<div', '</div>', '<img']

    def match(self, text, keyword):
        return text.find(keyword)

    def comparison(self, oldText, newText):
        dmp = dmp_module.diff_match_patch()
        diffSections = dmp.diff_compute(oldText, newText, False, 1000)
        return diffSections

    def analyse(self, diffSections):
        if len(diffSections) == 1:
            if diffSections[0][0] == self.MARK_EQUAL:
                return self.DIFF_NOCHANGE
            elif diffSections[0][0] == self.MARK_DELETE:
                return self.DIFF_CUTOUT
            else:
                return self.DIFF_NEW

        elif len(diffSections) == 2 and diffSections[0][0] == self.MARK_DELETE and diffSections[0][0] == self.MARK_INSERT:
            return self.DIFF_LARGECHANGE
        else:
            return self.DIFF_NORMALCHANGE

    def run(self):
        inputfile = open('input.txt', 'r')
        sourcefile = open('source.txt', 'r')

        oldText = sourcefile.read()
        newText = inputfile.read()

        for abnormal in self.SYMBOL_ABNORMAL:
            if self.match(newText, abnormal) is not -1:
                print self.DIFF_ABNORMALCHANGE

        print self.comparison(oldText, newText)
        print self.analyse(self.comparison(oldText, newText))


if __name__ == '__main__':
    Baymax().run()
