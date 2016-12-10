class MongoUtils(object):
    mongo = None

    def __init__(self, mongo):
        self.mongo = mongo