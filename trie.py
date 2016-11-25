"""A simple TRIE tree """

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.eof = False

    def __repr__(self):
        return "<Node value:{} EOF:{} children:{}>".format(
            self.value,
            self.eof,
            len(self.children),
        )


class Trie(object):

    def __init__(self, dictionary):
        self.root = {}
        self.dictionary = dictionary
        self._create()

    def _create(self):
        root = self.root
        for word in self.dictionary:
            current = root
            value = ""
            for char in word:
                value += char
                if not current.get(value):
                    node = Node(value)
                    current.update({value: node})
                else:
                    node = current.get(value)
                current = node.children
            node.eof = True

    def all(self):
        return self._all(self.root)

    def _all(self, current):
        words = []
        for word, node in current.iteritems():
            if node.eof:
                words.append(word)
            words += self._all(node.children)
        return words

    def lookup(self, lookup_value):
        return self._lookup(self.root, lookup_value)

    def _lookup(self, current, lookup_value):
        value = ""
        for char in lookup_value:
            value += char
            if value in current:
                current = current.get(value).children
            else:
                return False
        return True

dictionary = [
    'foo',
    'foobar',
    'foobaz',
    'bar',
    'baz',
    'barz',
]

trie = Trie(dictionary)

print "TRIE tree dictionary: {}".format(trie.all())
print "Looking up some example words ->"
for key in ('foo', 'bar', 'book', 'class'):
    print "{}: {}".format(key, "found" if trie.lookup(key) else "notfound")
