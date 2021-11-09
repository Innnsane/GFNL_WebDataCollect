import os
import ujson
import datetime
from dicts import *


DATA = "./data"


def create_html(num):
    lists = []
    today = "".join(str(datetime.date.today()).split("-")) + ".json"
    if os.path.exists(os.path.join(DATA, today)):
        with open(os.path.join(DATA, today), "r", encoding='utf-8') as f:
            lists = ujson.load(f)
            f.close()

    html_list = []
    i = len(lists) - 1
    while i >= len(lists) - num and i >= 0:
        this_html_dict = {
            "1": f"No.{i}_周{lists[i]['inTurnType']}_{lists[i]['doNumber']}次_{len(lists[i]['algorithm'])}算法",
            "2": []
        }

        for j in lists[i]['algorithm']:
            this_html_dict["2"].append(f"{ALGORITHM[j['id']]['name']}-{j['position']}_{ATTRIBUTE[int(j['mainAttr'])]}")

        html_list.append(this_html_dict)
        i -= 1

    return ujson.dumps(html_list)


def format_algorithm_single(algorithm_list):
    algorithm_dict = {}
    for i in algorithm_list:
        keyname = f"{i['id']}-{i['position']}-{i['mainAttr']}"
        if keyname not in algorithm_dict.keys():
            algorithm_dict[keyname] = 1
        else:
            algorithm_dict[keyname] += 1

    return algorithm_dict

