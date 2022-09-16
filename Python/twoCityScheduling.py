

def twoCitySchedCost(costs) -> int:
    a_cost=list()
    b_cost=list()
    row=len(costs)
    for i in range(row):
        for j in range(2):
            if j==0:
                a_cost.append(costs[i][j])
            else:
                b_cost.append(costs[i][j])
    print(a_cost)
    print(b_cost)
    # Each city must be visited by n person
    # a_visits<n//2 and b_visits<n//2
