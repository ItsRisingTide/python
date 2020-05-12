from functools import wraps
cashe = {}
def lru_cashe(limit):
    def cash_decorator(func):
        #cashe = {}
        @wraps(func)
        def new_func(x):
            if x not in cashe:
                if len(cashe) == limit:
                    print("popitem from cashe")
                    print(cashe)
                    cashe.popitem()
                    print("new cashe")
                    print(cashe)
                cashe[x] = func(x)
            return cashe[x]
        return new_func
    return cash_decorator

@lru_cashe(limit = 3)
def sqr(x):
    print("calculating sqr")
    return x * x

#и
