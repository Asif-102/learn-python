def mode(list):
    wkts_freq = {}
    for item in list:
        if item in wkts_freq:
            wkts_freq[item] += 1
        else:
            wkts_freq[item] = 1
        print("Wicket:", item, "Count:", wkts_freq[item])

wkts_list = [6,5,4,3,1,3,2,1,0,5,3,3,2,2,1,3,4,3,3]

mode(wkts_list)