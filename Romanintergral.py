class romanint(object):
    def romanToInt(self, s):
        romandic = {"M":1000,"D":500, "C":100, "L":50,"X":10,"V":5,"I":1,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        integerlis = []
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                nextletter = s[i] + s[i+1]
                print(f'{nextletter} is {i}')
            else:
                nextletter = 'empty'



            if nextletter in romandic:
                integerlis.append(romandic[nextletter])
                i += 2
            elif s[i] in romandic:
                integerlis.append(romandic[s[i]])
                i += 1
        print(integerlis)
        result = sum(integerlis)
        return result

romanint().romanToInt("III")