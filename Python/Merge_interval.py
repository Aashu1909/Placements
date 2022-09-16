def are_overlapping(min_right,max_left)


def merge_interval(interval):
    interval.sort(key=lambda i:i[0])
    ans_interval=[]
    for i in range(len(interval)-1):
        for j in range(i+1,len(interval)):
            if 