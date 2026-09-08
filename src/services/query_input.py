class Empty_query_Error(BaseException):    
    pass

def input_query():
    query=input("Enter your query: ")
    if query:
        return query
    print("Query can't be empty")
    raise Empty_query_Error