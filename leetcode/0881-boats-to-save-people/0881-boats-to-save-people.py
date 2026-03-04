class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        boat = 0
        popped = []
        for i in range(n):
            if people[i] == limit:
                boat += 1
                popped.append(i)
        for i in sorted(popped,reverse = True):
            people.pop(i)
        n = len(people)
        a = 0
        b = n-1
        while b >= a:
            if people[a] + people[b] <= limit:
                boat += 1
                a += 1
                b -= 1
            else:
                boat += 1
                b -= 1
        return boat


        



