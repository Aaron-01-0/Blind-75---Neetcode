class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #Time Complexity O(N long N) due to sorting

#Optimized Way
    def isAnagram(s, t):
        # 1. The Quick Reject: If they aren't the same length, it's impossible.
        if len(s) != len(t):
            return False
            
        count = {} # This is our dictionary (Hash Map) to hold the buckets
        
        # 2. Build the Frequency Map
        for i in range(len(s)):
            # dict.get(key, 0) means "give me the current count, or 0 if it doesn't exist yet"
            count[s[i]] = count.get(s[i], 0) + 1  # Add 1 for string s
            count[t[i]] = count.get(t[i], 0) - 1  # Subtract 1 for string t
            
        # 3. The Final Audit: Are all buckets exactly zero?
        for value in count.values():
            if value != 0:
                return False
                
        return True

#Pythonic Way
from collections import Counter

    def isAnagram(s, t):
        # Counter("listen") creates -> {'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1}
        return Counter(s) == Counter(t)


