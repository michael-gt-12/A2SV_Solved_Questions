class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        for i in range(len(responses)):
            responses[i] = list(set(responses[i]))

        response_freq = {}
        for i in range(len(responses)):
            for j in range(len(responses[i])):
                if responses[i][j] in response_freq:
                    response_freq[responses[i][j]] += 1
                else:
                    response_freq[responses[i][j]] = 1

        possible_responses = []

        highest_freq = max(response_freq.values())
        for key,value in response_freq.items():
            if value == highest_freq:
                possible_responses.append(key)
        
        return min(possible_responses)

        
