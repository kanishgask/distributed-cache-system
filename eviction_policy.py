class LRUEviction:

    def evict(self, cache_order):

        if cache_order:
            return cache_order.pop(0)

        return None
