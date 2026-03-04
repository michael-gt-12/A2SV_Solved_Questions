class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        a = 0
        teamSkl = []
        while a < (n/2):
            teamSkl.append(skill[a]+skill[n-1-a])
            a+=1
        a = 0
        result = 0
        if teamSkl.count(teamSkl[0]) == n/2:
            while a < (n/2):
                result += skill[a] * skill[n-1-a]
                a += 1
        else:
            result = -1
        return result

            


        