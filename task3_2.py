def pluz(arg1, arg2):
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        except TypeError:
            return False
    types = [type(arg1), type(arg2)]
    term1 = is_number(arg1) and is_number(arg2)
    term2 = str in types
    term3 = int in types or float in types
    if term1 and term2 and term3:
        return float(arg1) + float(arg2)
    return arg1+arg2
