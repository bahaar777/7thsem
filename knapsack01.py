class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def knapsack(items, capacity):
    # Number of items
    n = len(items)

    # Create a DP table with dimensions (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if i==0 or w==0:
                dp[i][w]= 0
            if items[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], items[i - 1].value + dp[i - 1][w - items[i - 1].weight])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# driver code
#items = [Item(60, 10), Item(100, 20), Item(120, 30)]

capacity = int(input("Enter the capacity of sack"))
n= int(input("Enter the no of items "))
items=[]
for i in range(n):
    v=int(input("Enter value of item "))
    w=int(input("Enter weight of item "))
    items.append(Item(v,w))



print("Maximum value in Knapsack =", knapsack(items, capacity))