# -*- coding: utf-8 -*-
import diff_match_patch as dmp_module
import constant


class Baymax(object):

    def match(self, text, keyword):
        return text.find(keyword)

    def comparison(self, oldText, newText):
        dmp = dmp_module.diff_match_patch()
        diffSections = dmp.diff_compute(oldText, newText, False, 1000)
        return diffSections

    def analyse(self, diffSections):
        if len(diffSections) == 1:
            if diffSections[0][0] == constant.MARK_EQUAL:
                return constant.DIFF_NOCHANGE
            elif diffSections[0][0] == constant.MARK_DELETE:
                return constant.DIFF_CUTOUT
            else:
                return constant.DIFF_NEW

        elif len(diffSections) == 2 \
                and diffSections[0][0] == constant.MARK_DELETE \
                and diffSections[0][0] == constant.MARK_INSERT:
            return constant.DIFF_LARGECHANGE

        else:
            return constant.DIFF_NORMALCHANGE

    def run(self):
        inputfile = open('input.txt', 'r')
        sourcefile = open('source.txt', 'r')

        oldText = sourcefile.read()
        newText = inputfile.read()

        for abnormal in constant.ABNORMAL_SYMBOLS:
            if self.match(newText, abnormal) is not constant.NOTFOUND:
                print constant.DIFF_ABNORMALCHANGE

        print self.comparison(oldText, newText)
        print self.analyse(self.comparison(oldText, newText))


if __name__ == '__main__':
    Baymax().run()
