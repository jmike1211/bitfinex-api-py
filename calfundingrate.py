from bfxmongo import useMongo

class calRate:
    def fundingRate():
        try:
            fundingRate = useMongo().mongofindone({},"frrrate")
            print(fundingRate)
            frrRate = fundingRate["frr"]
            days = 2 
            if fundingRate["frr"] > 0.00055: # 20%
                if fundingRate["dayhigh"] >= 0.001: #40%
                    frrRate = (fundingRate["frr"] + fundingRate["dayhigh"])/2
                elif fundingRate["frr"] >= fundingRate["dayhigh"]: #40%
                    frrRate = (fundingRate["lprice"] + fundingRate["dayhigh"])/2
                days = 14
            else:
                if fundingRate["lprice"] < 0.00019: #7%
                    frrRate = 0.00025
                elif fundingRate["lprice"] > 0.0004: #15%
                    frrRate = (fundingRate["frr"] + fundingRate["lprice"])/2
                elif fundingRate["frr"] >= fundingRate["dayhigh"]:
                    frrRate = (fundingRate["dayhigh"] + fundingRate["lprice"])/2
        except:
            frrRate = 0.00031123 #10%
            days = 2
        return frrRate, days
#a, b = calRate.fundingRate()
