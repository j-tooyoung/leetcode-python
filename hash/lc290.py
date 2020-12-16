
#
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            # if ch not in ch2word:
            #     ch2word[ch] = word
            # elif ch2word[ch] != word:
            #     return False
            # if word not in word2ch:
            #     word2ch[word] = ch
            # elif word2ch[word] != ch:
            #     return False
            if (ch in ch2word and ch2word[ch] != word) or (word in word2ch and word2ch[word] != ch):
                return False
            ch2word[ch] = word
            word2ch[word] = ch
        return True
