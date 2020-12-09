# -*- coding: utf-8 -*-

from pathlib import Path


class Paths:
    def __init__(self):
        self.home = Path.home()
        self.akl_home = self.home.joinpath("Desktop\\AKL_Auto")

        self.default_costs = self.akl_home.joinpath(
            ".templates\\Region_Costs.xlsx")

        self.default_concepts = self.akl_home.joinpath(
            "DB_Data\\Concepts.xlsx")
        self.default_pt_spirits = self.akl_home.joinpath(
            "DB_Data\\PT Beverages - Spirits.xlsx")
        self.default_pt_lavazza = self.akl_home.joinpath(
            "DB_Data\\PT Beverages - Lavazza.xlsx")

        self.default_path_mapper = {
            "Concepts": self.default_concepts,
            "PT Beverages - Spirits": self.default_pt_spirits,
            "PT Beverages - Lavazza": self.default_pt_lavazza
        }

        self.default_export_concepts = self.akl_home.joinpath(
            "Concepts.xlsx")
        self.default_export_pt_spirits = self.akl_home.joinpath(
            "PT Beverages - Spirits.xlsx")
        self.default_export_pt_lavazza = self.akl_home.joinpath(
            "PT Beverages - Lavazza.xlsx")

        self.default_export_path_mapper = {
            "Concepts": self.default_export_concepts,
            "PT Beverages - Spirits": self.default_export_pt_spirits,
            "PT Beverages - Lavazza": self.default_export_pt_lavazza
        }

        self.user_costs = ""
        self.user_concepts = ""
        self.user_pt_spirits = ""
        self.user_pt_lavazza = ""

        self.user_path_mapper = {
            "Concepts": self.user_concepts,
            "PT Beverages - Spirits": self.user_pt_spirits,
            "PT Beverages - Lavazza": self.user_pt_lavazza
        }

    def get_path(self, process: str):
        return self.default_path_mapper[process]

    def get_user_path(self, process: str):
        return self.user_path_mapper[process]
