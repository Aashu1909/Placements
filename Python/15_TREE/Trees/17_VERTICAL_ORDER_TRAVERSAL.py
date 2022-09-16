from collections import deque,defaultdict
def vertical_order_traversal(root):
    ans_dict=defaultdict(list)
    queue=deque()
    start=end=0
    queue.append((root,0))
    while len(queue)>0:
        n=len(queue)
        curr_dict=defaultdict(list)
        for _ in range(n):
            node=queue.popleft()
            start=min(start,node[1])
            end=max(end,node[1])
            curr_dict[node[1]].append(node[0].val)
            if node[0].left!=None:
                queue.append((node[0].left,node[1]-1))
            if node[0].right!=None:
                queue.append((node[0].right,node[1]+1))
        for key ,value in curr_dict.items():
            ans_dict[key]+=value
    ans_list=[]
    for i in range(start,end+1):
        ans_list.extend(ans_dict[i])
    return ans_list