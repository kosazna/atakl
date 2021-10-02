# -*- coding: utf-8 -*-

from atakl.validate import *
from atakl.utilities import *
from atakl.transform.concepts import Concepts
from atakl.transform.ptb_spirits import PTBSpirits
from atakl.transform.ptb_lavazza import PTBLavazza
from atakl.transform.cavino import Cavino
from atakl.transform.giochi import Giochi
from atakl.transform.giochi_crate import GiochiCrate
from atakl.transform.essse import Essse
from atakl.transform.cosco_infoquest import CoscoInfoquest
from atakl.transform.alexandrion import Alexandrion
from atakl.transform.kitsanelis import Kitsanelis

transformer_mapper = {
    "Concepts": Concepts,
    "PT Beverages - Spirits": PTBSpirits,
    "PT Beverages - Lavazza": PTBLavazza,
    "Cavino": Cavino,
    "Giochi": Giochi,
    "Giochi - Crate": GiochiCrate,
    "Essse": Essse,
    "Cosco - Infoquest": CoscoInfoquest,
    "Alexandrion": Alexandrion,
    "Kitsanelis": Kitsanelis}


def load_tranformer(_action: str, mode, path_list=None):
    if mode == 'CLI':
        _data = validate_path("File with the database data:\n")
        _costs = validate_path("File with costs per region:\n")
        _out = None

        if _data is None:
            data_path = paths.default_path_mapper[_action]
        else:
            paths.user_path_mapper[_action] = _data
            data_path = _data

        if _costs is None:
            costs_path = paths.default_costs
        else:
            paths.user_costs = _costs
            costs_path = _costs
    else:
        costs_path = path_list[0]
        data_path = path_list[1]
        _out = path_list[2]

    _tranformer = transformer_mapper[_action](data_filepath=data_path,
                                              cost_filepath=costs_path,
                                              output_path=_out,
                                              mode=mode)

    return _tranformer
