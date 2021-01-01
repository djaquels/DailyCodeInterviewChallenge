class Node():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def maxSum(map):
    max = 0
    maxk = 0
    for k,v in map.items():
        if v > max:
            max = v
            maxk = k
    return maxk

def most_freq_subtree_sum(root,sums):
    if root.left == None and root.right == None:
        sum = root.val
        if sum in sums:
            sums[sum] += 1
        else:
            sums[sum] = 1
        print(sums,sum,root.val,'leaf')
        return sum
    if root.left == None:
        sum = root.val + most_freq_subtree_sum(root.right,sums)
        if sum in sums:
            sums[sum] += 1
        else:
            sums[sum] = 1
        print(sums,sum,root.val,'left')
        return sum
    if root.right == None:
        sum = root.val + most_freq_subtree_sum(root.left,sums)
        if sum in sums:
            sums[sum] += 1
        else:
            sums[sum] = 1
        print(sums,sum,root.val,'right')
        return sum
    sum = root.val + most_freq_subtree_sum(root.left,sums) + most_freq_subtree_sum(root.right,sums)
    if sum in sums:
        sums[sum] += 1
    else:
        sums[sum] = 1
    print(sums,sum,root.val)
    return sum


root = Node(3, Node(1,Node(2),Node(-3)), Node(-3,Node(4)))
map = {}
print(most_freq_subtree_sum(root,map))
maxs = maxSum(map)
print("Maximo: {}".format(maxs))