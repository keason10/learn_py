import abc
import collections.abc
from datetime import datetime,timedelta
from pathlib import Path

gv = 111
def show_desc(par: str, sec: str):
    def show_desc_de(fc):
        def show_desc_para_fc(*p, **p1):
            print(f"par= {par} sec= {sec} :{fc.__name__}")
            fc(*p, **p1)

        return show_desc_para_fc

    return show_desc_de


@show_desc(**{"par": "par1", "sec": "sec1"})
def show_par(*p, **p1):
    print(f"p {p!r},p2 {p1}")

def show_nolocal():
    '''nonlocal 改变闭包里边的值'''
    id =1
    id1 = 11
    def show_nolocal_inner():
        id =10
        nonlocal  id1
        id1 =22
        print(f"show_nolocal_inner id = {id}, id1 ={id1}")
    show_nolocal_inner()
    print(f"show_nolocal id = {id}, id1 ={id1}")


class Test:
    pass

a_test = Test()

if __name__ == '__main__':
    show_nolocal()

    name ="jams"
    show_par(*(1, 2, 3), **{"id": 123})
    show_par(*(1, 2, 3), **locals())
    show_par(*(1, 2, 3), **globals())


    # 这里使用/直接拼接途径
    pa = Path("./")
    with (pa/"path_test.txt").open("w+") as f1:
        f1.write("hello path /")


