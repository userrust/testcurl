from config import code

def code_s(text):
    res = ""
    text_work = list(text.lower())

    for i in text_work:
        if i in code:
            res += code[i]

    print(res)


def decode(cod):
    array = [cod[i:i + 5] for i in range(0, len(cod), 5)]

    result = ""

    for q in array:
        for h in code:
            if q in code[h]:
                result += h
    print(result)
