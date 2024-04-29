import asyncio
from asyncio import Event
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from typing import List


def fun1(str):
    print("str:", str)
    return str * 2


def fun2(*str, **args):
    print("str:", str)
    print("args:", args)
    return str * 2


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as ex:
        result = ex.map(fun1, [1, 2, 3])
        for item in result:
            print(item)

    with ProcessPoolExecutor(max_workers=3) as ex:
        list = [ex.submit(fun2, *(1, 23), **{"id": 1})]
        list1 = as_completed(list)
        for item in list1:
            print(item.result())
