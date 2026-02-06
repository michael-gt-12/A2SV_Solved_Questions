class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = []
        cpdomains_dict = {}
        for i in range(len(cpdomains)):
            rep,domain = cpdomains[i].split()
            rep = int(rep)
            domain = list(domain.split("."))
            for j in range(len(domain)-1,-1,-1):
                dom = ".".join(domain[j:])
                if dom in cpdomains_dict:
                    cpdomains_dict[dom] += rep
                else:
                    cpdomains_dict[dom] = rep
        for key,value in cpdomains_dict.items():
            value = str(value)
            result.append(" ".join([value,key]))
        return result
            


        