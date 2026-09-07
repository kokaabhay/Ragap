from unstructured.partition.auto import partition
from unstructured.chunking.title import chunk_by_title



filepath="C://Users//AbhayKoka//ragap//src//Policy_Documents//sample.pdf"

def docextract(filepath):
    elements = partition(filename=filepath,languages=["eng"])
    #print(type(elements))
    
    #print([str(el) for el in elements])
    e=[str(el) for el in elements]
    # print(e)
    # #print("\n\n".join([str(el) for el in elements]))
    
    return elements

    #check titles
    # for e in elements:
    #     if e.category == "Title":
    #         print(e)


#use chunk by title strategy
def chunking(path=filepath):
    e=docextract(path)
    chunks=chunk_by_title(e)
    l=[]
    #print(type(chunks))
    for chunk in chunks:
        #print(chunk)
        l.append(chunk.text)
        #print("\n" + "-"*200)
    return l
        
    

#print(chunking(filepath))

