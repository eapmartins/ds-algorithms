from src.base.block import Block

class Blockchain():

    def __init__(self):
        self.root = None

    def add(self, data):

        if self.root == None:
            self.root = Block(data, None)

        else:
            current = self.root

            while current.next:
                current = current.next

            previous_hash = current.hash
            current.next = Block(data, previous_hash)


blockchain = Blockchain()

blockchain.add("some information")
blockchain.add("another information")
blockchain.add("more information")

data = ["some information", "another information", "more information"]
i = 0
current = blockchain.root
previous_hash = None

while current.next:
    assert current.data == data[i]
    assert current.previous_hash == previous_hash
    previous_hash = current.hash
    current = current.next
    i += 1