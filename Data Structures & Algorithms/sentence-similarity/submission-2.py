class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        true_so_far = 0
        
        if len(sentence1) != len(sentence2):
            return False
        
        similar_set = set(tuple(p) for p in similarPairs)
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or (sentence1[i], sentence2[i]) in similar_set or (sentence2[i], sentence1[i]) in similar_set:
                true_so_far += 1
        
        if true_so_far != len(sentence1):
            return False
        else:
            return True