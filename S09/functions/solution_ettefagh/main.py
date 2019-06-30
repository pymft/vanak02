from ettefagh import data


def tag(t, t1=300, t2=700):
    if t < t1:
        return 'S'
    elif t > t2:
        return 'L'
    return 'M'


starts = data[:-1]
stops = data[1:]

intervals = [e - i for i, e in zip(starts, stops)]
tags = [tag(t) for t in intervals]
descriptive_str = ''.join(tags)

print(intervals)
print(tags)
print(descriptive_str)

pattern = "MLLLLM"
indx = descriptive_str.find(pattern, 116)
print(data[indx:indx + len(pattern)+ 1])

pattern = "LS{2, 5}L"