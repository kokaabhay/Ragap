from unstructured.partition.auto import partition
filepath="C://Users//AbhayKoka//ragap//src//Policy_Documents//sample.pdf"

def docextract(filepath):
    elements = partition(filename=filepath)
    print(type(elements))
    
    #print([str(el) for el in elements])
    e=[str(el) for el in elements]
    print(e)
    #print("\n\n".join([str(el) for el in elements]))
    
    return e

docextract(filepath)