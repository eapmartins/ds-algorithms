import hashlib
from datetime import datetime

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = datetime.now()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.data)
      self.next = None

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()