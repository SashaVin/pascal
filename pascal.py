class PascalList:

    def __init__(self, lst):
        self.lst = lst

    def __setitem__(self, key, value):
        self.lst.insert(0, 0)
        return self.lst

    def __getitem__(self, item):
        if item > 0:
            return self.lst[item - 1]
        else:
            return 'KeyError'

    def __str__(self):
        return str(self.lst)


a = PascalList([1, 2, 3, 4])
print(a)
print(a[1])
