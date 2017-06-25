import enum
from flask.json import JSONEncoder
from mmgmt_server.models import MmgmtModel



class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, MmgmtModel):
                return obj.as_dict()
            if isinstance(obj, enum.Enum):
                return obj.name
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
