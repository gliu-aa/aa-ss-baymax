from difflib import Differ

class Baymax(object):
	
    def _comparison(self, str1, str2):
        variation = 0 # degree of variation
        return variation

    def appendBoldChanges(self, s1, s2):
        "Adds <b></b> tags to words that are changed"
        l1 = s1.split(' ')
        l2 = s2.split(' ')
        dif = list(Differ().compare(l1, l2))
        return " ".join(['<b>'+i[2:]+'</b>' if i[:1] == '+' else i[2:] for i in dif if not i[:1] in '-?'])

    def run(self):
        str1 = "asdf ghhj"
        str2 = "asdf tyui"
        variation = self._comparison(str1, str2)
        print self.appendBoldChanges(str1, str2)
        print variation

if __name__ == '__main__':
    Baymax().run()