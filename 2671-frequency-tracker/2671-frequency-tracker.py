class FrequencyTracker:

    def __init__(self):
        from collections import defaultdict
        self.numFreq = defaultdict(int)   
        self.freqCount = defaultdict(int) 

    def add(self, number: int) -> None:
        oldFreq = self.numFreq[number]
        if oldFreq > 0:
            self.freqCount[oldFreq] -= 1
        
        newFreq = oldFreq + 1
        self.numFreq[number] = newFreq
        self.freqCount[newFreq] += 1

    def deleteOne(self, number: int) -> None:
        oldFreq = self.numFreq[number]
        if oldFreq == 0:
            return
        
        self.freqCount[oldFreq] -= 1
        newFreq = oldFreq - 1
        self.numFreq[number] = newFreq
        
        if newFreq > 0:
            self.freqCount[newFreq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqCount[frequency] > 0
