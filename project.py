import requests
import re

top250_url = "http://akas.imdb.com/chart/top"


def get_top250():
    r = requests.get(top250_url)
    html = r.text.split("\n")
    result = []
    for line in html:
        line = line.rstrip("\n")
        m = re.search(r'data-titleid="tt(\d+?)">', line)
        if m:
            _id = m.group(1)
            result.append(_id)
    #
    return result


def main():
    print(get_top250())



def f():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()