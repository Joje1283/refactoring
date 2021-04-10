from functools import reduce

class On:
    def __init__(self, collection):
        self.collection = collection
        self.pipeline = []

    def __iter__(self):
        for item in self.collection:
            for stage in self.pipeline:
                item = stage(item)
            yield item

    def inc(self, n):
        def _inc(i):
            return i + n
        self.pipeline.append(_inc)
        return self

    def mul(self, n):
        def _mul(i):
            return i * n
        self.pipeline.append(_mul)
        return self

    def map(self, func):
        self.pipeline = list(map(func, self.pipeline))
        return self
