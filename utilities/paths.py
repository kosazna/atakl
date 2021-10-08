# -*- coding: utf-8 -*-

from pathlib import Path


class Paths:
    def __init__(self):
        self.home = Path.home()

        self.akl_home = Path.cwd()
        self.logger = self.akl_home.joinpath("AKL_Log.txt")

        self.default_costs = self.akl_home.joinpath(
            ".templates\\Region_Costs.xlsx")

        self.default_concepts = self.akl_home.joinpath(
            "DB_Data\\Concepts.xlsx")
        self.default_pt_spirits = self.akl_home.joinpath(
            "DB_Data\\PT Beverages - Spirits.xlsx")
        self.default_pt_lavazza = self.akl_home.joinpath(
            "DB_Data\\PT Beverages - Lavazza.xlsx")
        self.default_cavino = self.akl_home.joinpath(
            "DB_Data\\Cavino.xlsx")
        self.default_giochi = self.akl_home.joinpath(
            "DB_Data\\Giochi.xlsx")
        self.default_giochi_crate = self.akl_home.joinpath(
            "DB_Data\\Giochi.xlsx")
        self.default_essse = self.akl_home.joinpath(
            "DB_Data\\Essse.xlsx")
        self.default_cosco_infoquest = self.akl_home.joinpath(
            "DB_Data\\Cosco - Infoquest.xlsx")
        self.default_alexandrion = self.akl_home.joinpath(
            "DB_Data\\Alexandrion.xlsx")
        self.default_kitsanelis = self.akl_home.joinpath(
            "DB_Data\\Kitsanelis.xlsx")
        self.default_siganos = self.akl_home.joinpath(
            "DB_Data\\Siganos.xlsx")

        self.default_path_mapper = {
            "Concepts": self.default_concepts,
            "PT Beverages - Spirits": self.default_pt_spirits,
            "PT Beverages - Lavazza": self.default_pt_lavazza,
            "Cavino": self.default_cavino,
            "Giochi": self.default_giochi,
            "Giochi - Crate": self.default_giochi_crate,
            "Essse": self.default_essse,
            "Cosco - Infoquest": self.default_cosco_infoquest,
            "Alexandrion": self.default_alexandrion,
            "Kitsanelis": self.default_kitsanelis,
            "Siganos": self.default_siganos}

        self.default_export_concepts = self.akl_home.joinpath(
            "Concepts.xlsx")
        self.default_export_pt_spirits = self.akl_home.joinpath(
            "PT Beverages - Spirits.xlsx")
        self.default_export_pt_lavazza = self.akl_home.joinpath(
            "PT Beverages - Lavazza.xlsx")
        self.default_export_cavino = self.akl_home.joinpath(
            "Cavino.xlsx")
        self.default_export_giochi = self.akl_home.joinpath(
            "Giochi.xlsx")
        self.default_export_giochi_crate = self.akl_home.joinpath(
            "Giochi.xlsx")
        self.default_export_essse = self.akl_home.joinpath(
            "Essse.xlsx")
        self.default_export_cosco_infoquest = self.akl_home.joinpath(
            "Cosco - Infoquest.xlsx")
        self.default_export_alexandrion = self.akl_home.joinpath(
            "DB_Data\\Alexandrion.xlsx")
        self.default_export_kitsanelis = self.akl_home.joinpath(
            "DB_Data\\Kitsanelis.xlsx")
        self.default_export_siganos = self.akl_home.joinpath(
            "DB_Data\\Siganos.xlsx")

        self.default_export_path_mapper = {
            "Concepts": self.default_export_concepts,
            "PT Beverages - Spirits": self.default_export_pt_spirits,
            "PT Beverages - Lavazza": self.default_export_pt_lavazza,
            "Cavino": self.default_export_cavino,
            "Giochi": self.default_export_giochi,
            "Giochi - Crate": self.default_export_giochi_crate,
            "Essse": self.default_export_essse,
            "Cosco - Infoquest": self.default_export_cosco_infoquest,
            "Alexandrion": self.default_export_alexandrion,
            "Kitsanelis": self.default_export_kitsanelis,
            "Siganos": self.default_export_siganos}

        self.user_costs = ""
        self.user_concepts = ""
        self.user_pt_spirits = ""
        self.user_pt_lavazza = ""
        self.user_cavino = ""
        self.user_giochi = ""
        self.user_giochi_crate = ""
        self.user_essse = ""
        self.user_cosco_infoquest = ""
        self.user_alexandrion = ""
        self.user_kitsanelis = ""
        self.user_siganos = ""

        self.user_path_mapper = {
            "Concepts": self.user_concepts,
            "PT Beverages - Spirits": self.user_pt_spirits,
            "PT Beverages - Lavazza": self.user_pt_lavazza,
            "Cavino": self.user_cavino,
            "Giochi": self.user_giochi,
            "Giochi - Crate": self.user_giochi_crate,
            "Essse": self.user_essse,
            "Cosco - Infoquest": self.user_cosco_infoquest,
            "Alexandrion": self.user_alexandrion,
            "Kitsanelis": self.user_kitsanelis,
            "Siganos": self.user_siganos}

    def get_path(self, process: str):
        return self.default_path_mapper[process]

    def get_user_path(self, process: str):
        return self.user_path_mapper[process]
