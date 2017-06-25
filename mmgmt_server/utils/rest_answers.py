from flask import jsonify
import json


def write_ok_result(payload=""):
    # payload = conv_dictlist_json(payload)
    result = {
        "result": "ok",
        "payload": payload
    }
    return jsonify(result)


def conv_dictlist_json(dictlist):
    if isinstance(dictlist, list):
        if isinstance(dictlist[0], object):
            json_vals = []
            for entry in dictlist:
                json_vals.append(entry.as_dict())
            return json_vals
    return dictlist

