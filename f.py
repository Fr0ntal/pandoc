from panflute import *
from sys import stderr

headers = []


def duplicateHeaders(elem, doc):
    if type(elem) == Header:
        text = stringify(elem)
        if text in headers:
            print("Duplicate headers", file=stderr)
        else:
            headers.append(text)


def bold(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))



def upperStr(elem, doc):
    if type(elem) == Str:
        elem.text = elem.text.upper()


def upperHeader(elem, doc):
    if type(elem) == Header and elem.level > 2:
        return elem.walk(upperStr)


if __name__ == "__main__":
    run_filters([upperHeader, duplicateHeaders], prepare=bold)