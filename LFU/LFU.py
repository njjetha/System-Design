from collections import OrderedDict, defaultdict
from datetime import datetime, timedelta
print(datetime.now().strftime("%Y-%m-%d"))


class LFUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.min_freq=0
        self.cache={} #key:(value,freq)
        self.freq_map=defaultdict(OrderedDict) # freq:{key:None}

    def _update(self,key,value):
        val,freq=self.cache[key]
        del self.freq_map[freq][key]
        self.cache[key]=(value,freq+1)
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if freq == self.min_freq:
                self.min_freq+=1
        self.freq_map[freq+1][key]=None

    def get(self,key):
        if key not in self.cache[key]:
            return
        self._update(key,self.cache[key][0])
        return self.cache[key][0]
    
    def put(self,key,value):
        if key in self.cache:
            self._update(key,value)
        else:
            if len(self.cache)>=self.capacity:
                evict_key,_=self.freq_map[self.min_freq].popitem(last=False)
                del self.cache[evict_key]
            self.cache[key]=(value,1)
            self.freq_map[1][key]=None
            self.min_freq=1

if __name__=='__main__':
    lfu_cache=LFUCache(2)
    lfu_cache.put(1,1)
    lfu_cache.put(2,2)
    print(lfu_cache.get(1))

