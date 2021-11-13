wkts_list = [6,5,4,3,1,3,2,1,0,5,3,3,2,2,1,3,4,3,3]

wkts_freq = {}

for item in wkts_list:
    if item in wkts_freq:
        wkts_freq[item] += 1
    else:
        wkts_freq[item] = 1

for item in wkts_freq:
    print("Wicket:", item, "Count:", wkts_freq[item])
