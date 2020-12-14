# -*- coding: utf-8 -*-

from atakl.validate import *
from atakl.utilities import *
from atakl.transform.type_one import TypeOneTransformer
from atakl.transform.type_two import TypeTwoTransformer
from atakl.transform.type_three import TypeThreeTransformer

transformer_mapper = {
    "Concepts": TypeOneTransformer,
    "PT Beverages - Spirits": TypeTwoTransformer,
    "PT Beverages - Lavazza": TypeThreeTransformer}


def load_tranformer(_action: str, mode, path_list=None):
    if mode == 'CMD':
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
