class Solution(object):
    def intToRoman(self, num):
        s = str(num).zfill(4)
        t = ""
        # Thousands
        t = t + int(s[0]) * "M"
        # Hundreds
        if int(s[1]) == 9:
            t += "CM"
        elif int(s[1]) >= 5:
            t += "D"
            t += (int(s[1]) - 5) * "C"
        elif int(s[1]) == 4:
            t += "CD"
        else:
            t += int(s[1]) * "C"
        # Tens
        if int(s[2]) == 9:
            t += "XC"
        elif int(s[2]) >= 5:
            t += "L"
            t += (int(s[2]) - 5) * "X"
        elif int(s[2]) == 4:
            t += "XL"
        else:
            t += int(s[2]) * "X"
        # Ones
        if int(s[3]) == 9:
            t += "IX"
        elif int(s[3]) >= 5:
            t += "V"
            t += (int(s[3]) - 5) * "I"
        elif int(s[3]) == 4:
            t += "IV"
        else:
            t += int(s[3]) * "I"
        
        return(t)
        