tup = [(19542209, "New York"), (4487871, "Alabama"), (234423, "Tehran"), (323023, "Kabul")]

# reverse list and sorted by last character of second item of tuple
sort_tup = sorted([(y, x) for x, y in tup], key=lambda x: x[0][-1])

print(sort_tup)

