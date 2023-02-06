class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letter_count = {
            "b":0,
            "a":0,
            "l":0,
            "o":0,
            "n":0
        }
        count = 0
        for x in text:
            if x in letter_count:
                letter_count[x] += 1

        for x in letter_count:
            if letter_count[x] <= 0:
                return 0
            if x == "l" or x == "o":
                if letter_count[x] <= 1:
                    return 0
        print(letter_count)
        while letter_count["b"] > 0:
            for x in letter_count:
                if x == "l" or x == "o":
                    letter_count[x] -= 2
                else:
                    letter_count[x] -= 1
            count +=1
            for x in letter_count:
                if letter_count[x] <= 0:
                    return count
                if x == "l" or x == "o":
                    if letter_count[x] <= 1:
                        return count
        return count
        


