class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_map = {5:0,10:0,20:0}
        for i in range(len(bills)):
            bill = bills[i]
            bills_map[bill] += 1
            change = bill - 5
            if change == 0:
                continue
            elif change == 5:
                if bills_map[5] >= 1:
                    bills_map[5] -= 1
                    continue
                else:
                    return False
            else:
                if bills_map[5] >= 1 and bills_map[10] >= 1:
                    bills_map[5] -= 1
                    bills_map[10] -= 1
                elif bills_map[5] >= 3:
                    bills_map[5] -= 3
                else:
                    return False

        return True


        