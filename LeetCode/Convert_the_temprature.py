class Solution: 
    def convertTemperature(self, celsius: float) -> List[float]:
        out=[]
        out.append(celsius+273.15)
        out.append(celsius*1.8+32)
        return out
