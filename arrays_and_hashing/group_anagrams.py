class Solution:
    def groupAnagrams(self, strs):
#         empty dict = {}
#         for each str in strs
#         sort the string 
#         if sorted not in dict
#               add to dictionary key and append that word to dictionary value

#         grouped_anagrams = {}
    
#         for s in strs:
#             sorted_s = "".join(sorted(s))
#             if sorted_s not in grouped_anagrams:
#                 grouped_anagrams[sorted_s] = [s]
#             else:
#                 grouped_anagrams[sorted_s].append(s)
            
#         return [val for val in grouped_anagrams.values()]
    
        grouped_anagrams = []
        sorted_anagrams = {} # {aet: 0, ant: 1, ...}
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in sorted_anagrams:
                sorted_anagrams[sorted_s] = len(grouped_anagrams)
                grouped_anagrams.append([s])
            else:
                grouped_anagrams[sorted_anagrams[sorted_s]].append(s)
                
        return grouped_anagrams