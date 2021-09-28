i]th, dirnames, filenames in os.walk(model_path):mport os

class ModelTree(object):
    """generate an item list for model tree display"""

    def __init__(self, model_path):
        self.model_path = model_path

    def generate(self):
        flist = []
        start = len(self.model_path)+1
        for dirpath, dirnames, filenames in os.walk(self.model_path):
            if len(dirnames) == 0:
                itype = "part"
            else:
                itype = "assembly"
            for f in filenames:
                if "data" in f or "pos" in f: continue
                path = os.path.abspath(os.path.join(dirpath, f))
                if path.endswith("scad"):
                    print(path, itype)
                    item = [path[start:], itype]
                    flist.append(item)
        return flist


if __name__ == '__main__':
    MODELDIR='/Users/rblack/_dev/math-magik-lpp/scad/math-magik-lpp'
    mt = ModelTree(MODELDIR)
    flist = mt.generate()
    for part in flist:
        print(part)
