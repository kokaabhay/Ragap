from unstructured.partition.auto import partition

elements = partition(filename="C://Users//AbhayKoka//ragap//src//Policy_Documents//sample.pdf")
print("\n\n".join([str(el) for el in elements]))