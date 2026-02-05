from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        chars_dict = Counter(chars)
        for i in range(len(words)):
            word_dict = Counter(words[i])
            count = 0
            for key in word_dict:
                if key not in chars_dict.keys():
                    break
                else:
                    if word_dict[key] > chars_dict[key]:
                        break
                    else:
                        count += word_dict[key]
            if count == len(words[i]):
                result += count 
        return result

                



        