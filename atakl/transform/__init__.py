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


def load_tranformer(_action: str):
    _data = validate_path("File with the database data:\n")
    _costs = validate_path("File with costs per region:\n")

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

    _tranformer = transformer_mapper[_action](data_filepath=data_path,
                                              cost_filepath=costs_path)

    return _tranformer
