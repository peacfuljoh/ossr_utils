
import os

import numpy as np

from src.ossr_utils.io_utils import save_pickle, load_pickle, save_json, load_json


def make_obj():
    obj = dict(
        a=np.arange(100).reshape(4, 25).tolist(),
        b='blah',
        c=5,
        d=True
    )
    return obj

def test_pickle():
    obj = make_obj()
    fpath = './dummy.pickle'
    save_pickle(fpath, obj)
    obj2 = load_pickle(fpath)
    os.remove(fpath)
    for key in obj.keys():
        assert obj[key] == obj2[key]

def test_json():
    obj = make_obj()
    fpath = './dummy.json'
    save_json(fpath, obj)
    obj2 = load_json(fpath)
    os.remove(fpath)
    for key in obj.keys():
        assert obj[key] == obj2[key]



if __name__ == "__main__":
    test_pickle()
    test_json()