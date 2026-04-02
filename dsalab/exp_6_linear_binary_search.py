class Product:
    def __init__(self, n, p): self.name, self.price = n, p

def linear_search(d, t):
    for i, x in enumerate(d):
        if x.name == t: return i
    return -1

def binary_search(d, t):
    l, h = 0, len(d) - 1
    while l <= h:
        m = (l + h) // 2
        if d[m].name == t: return m
        if d[m].name < t: l = m + 1
        else: h = m - 1
    return -1

dataset = [Product(f'Product{i}', p) for i, p in enumerate([10.99, 24.99, 34.99, 14.99, 19.99], 1)]
target = 'Product3'

for name, search_func in [("Linear", linear_search), ("Binary", binary_search)]:
    if name == "Binary": dataset.sort(key=lambda x: x.name)
    res = search_func(dataset, target)
    print(f"{name} Search: {target} {'found at index ' + str(res) if res != -1 else 'not found'}")