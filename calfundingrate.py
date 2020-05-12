from bfxmongo import useMongo

class calRate:
    def fundingRate():
        try:
            fundingRate = useMongo().mongofindone({},"frrrate")
            print(fundingRate)
            frrRate = fundingRate["frr"]
            days = 2 
            if fundingRate["frr"] > 0.00055: # 20%
                if dayhigh["dayhigh"] > 0.001: #40%
                    frrRate = (fundingRate["frr"] + fundingRate["dayhigh"])/2
                days = 30

            if fundingRate["ask"] < 0.00019: #7%
                frrRate = 0.00025
            elif fundingRate["ask"] > 0.0004: #15%
                frrRate = (fundingRate["frr"] + fundingRate["ask"])/2
        except:
            frrRate = 0.00027 #10%
            days = 2
        return frrRate, days
#calRate.fundingRate()
