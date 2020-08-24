import copy


class Item:
    def __init__(self, value, weight):
        self.value =value
        self.weight = weight


def dp_knapsack(itemList, capacity):
    assert len(itemList) > 0, "tough luck, the cave is empty"
    assert type(capacity) == int
    assert capacity > 0, "did you forget your knapsack"

    memo = [None] * (len(itemList) + 1)
    for j in range(len(memo)):
        memo[j] = [0] * (capacity + 1)

    memo_items = [None] * (len(itemList) + 1)
    for index in range(len(memo_items)):
        memo_items[index] = [[]] * (capacity + 1)

    i = 1
    for item in itemList:
        for j in range(1, (capacity + 1)):
            if item.weight > j:
                memo[i][j] = memo[i - 1][j]
                memo_items[i][j] = copy.deepcopy(memo_items[i - 1][j])
            else:
                memo[i][j] = max(memo[i - 1][j], item.value + memo[i - 1][j - item.weight])
                if memo[i][j] > memo[i-1][j]:
                    memo_items[i][j] = copy.deepcopy(memo_items[i - 1][j - item.weight])
                    memo_items[i][j].append(itemList.index(item))
                else:
                    memo_items[i][j] = copy.deepcopy(memo_items[i - 1][j])
        i += 1

    opt_value = memo[-1][-1]
    items = memo_items[-1][-1]

    return opt_value, items


def test_dp_knapsack():
    itemList = []
    item = Item(4000, 20)
    itemList.append(item)
    item = Item(3500, 10)
    itemList.append(item)
    item = Item(1800, 9)
    itemList.append(item)
    item = Item(400, 4)
    itemList.append(item)
    item = Item(1000, 2)
    itemList.append(item)
    item = Item(200, 1)
    itemList.append(item)

    assert (dp_knapsack(itemList, 20)) == (5500, [1, 2, 5]), "dp_knapsack failed"


test_dp_knapsack()
