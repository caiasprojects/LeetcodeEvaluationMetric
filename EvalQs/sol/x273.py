

from typing import List
class Solution:
    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def numberToWords(self, num):
        if not num:
            return "Zero"
        res = ""
        for thousand in self.thousands:
            if num % 1000:
                res = self.helper(num%1000) + thousand + " " + res
            num //= 1000
        return res.strip()

    def helper(self, num):
        if not num:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num//10] + " " + self.helper(num%10)
        else:
            return self.lessThan20[num//100] + " Hundred " + self.helper(num%100)

    def lengthOfLongestSubstring(self, s):
        # Use a dictionary to store the last seen index of each character
        last_seen = {}
        start = 0
        max_len = 0
        for end in range(len(s)):
            if s[end] in last_seen and last_seen[s[end]] >= start:
                start = max(last_seen[s[end]], start)
            last_seen[s[end]] = end + 1
            max_len = max(max_len, end - start + 1)
        return max_len