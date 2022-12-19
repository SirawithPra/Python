from collections import Counter

num_elements = int(input())
elements = []
counts = {}

for i in range(num_elements):
    element = input()
    elements.append(element)

counts = Counter(elements)
print(len(set(elements)))

for element, count in counts.items():
    print(count, end=' ')
print('yes')