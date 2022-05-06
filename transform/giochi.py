# -*- coding: utf-8 -*-

from atakl.transform.template import *
from atakl.transform.giochi_crate import GiochiCrate


class Giochi(TypeTemplate):
    except_areas = ("ΡΑΦΗΝΑ", "ΜΕΓΑΡΑ", "ΛΑΥΡΙΟ", "ΣΟΥΝΙΟ", "ΑΝΑΒΥΣΣΟ")
    except_value = 30.0

    def __init__(self, data_filepath: Union[str, Path],
                 cost_filepath: Union[str, Path],
                 output_path: Union[str, Path] = None,
                 mode='GUI'):
        super().__init__(data_filepath, cost_filepath, mode)

        self.name = "Giochi"
        self.map_name = f"{self.name}"
        self.backup = f"{self.map_name}.xlsx"

        self.output = paths.akl_home.joinpath(
            f"{self.map_name}.xlsx") if output_path is None else output_path

        self.costs = pd.read_excel(self.cost_file,
                                   sheet_name=self.name).set_index(
            c_2space(tomeas), drop=True)

        self.data = self.set_data(data_filepath, self.map_name)
        self.validator = Validator(self.data, self.map_name, mode)
        self.giochi_crate = GiochiCrate(
            str(self.data_file) + "@Διανομή_Κιβωτίου",
            self.cost_file,
            output_path,
            mode)

    def get_cost(self,
                 client: str,
                 region: str,
                 material: str,
                 quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0.00
        else:
            try:
                if client == 'JUMBO Α.Ε.Ε' and region == 'ΣΤ.ΕΛΛΑΔΑ - ΕΥΒΟΙΑ':
                    return round2(self.costs.loc['ΑΤΤΙΚΗ', material] * quantity)
                return round2(self.costs.loc[region, material] * quantity)
            except KeyError as e:
                self.log(e, Display.ERROR)
                return 0.00

    def _preprocess(self):
        self.data[paletes] = self.data[paletes].fillna(0).astype(int)
        self.data[ogkos] = self.data[ogkos].fillna(0.0).astype(float)

        self.data[paradosi] = self.data[paradosi].fillna("<NULL>")

        self.preprocessed = True

    def validate(self):
        if self.validator is not None:
            self.validator.validate()
            self.giochi_crate.validator.validate()
        else:
            self.log("Validator is not set", Display.ERROR)

    def process_rows(self, insert_into='last'):
        self.data[final_charge] = 0.0

        hold_idx = []
        hold = []

        for i in self.data.itertuples():
            minimum = self.get_minimum(i.Γεωγραφικός_Τομέας,
                                       i.Περιοχή_Παράδοσης,
                                       self.except_areas,
                                       self.except_value)

            if self._check_idxs(i.Index, info_map[self.map_name]['check_idxs']):
                hold_idx.append(i.Index)
                hold.append(i.Συνολική_Χρέωση)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)

                    whole = round2(sum(hold))

                    if whole > minimum:
                        for idx, value in zip(hold_idx, hold):
                            self.data.loc[idx, final_charge] = value
                    else:
                        if insert_into == 'last':
                            self.data.loc[i.Index, final_charge] = minimum
                        else:
                            _position = hold.index(max(hold))
                            _df_index = hold_idx[_position]
                            self.data.loc[_df_index, final_charge] = minimum

                    hold_idx = []
                    hold = []
                else:
                    if i.Συνολική_Χρέωση > minimum:
                        self.data.loc[
                            i.Index, final_charge] = i.Συνολική_Χρέωση
                    else:
                        self.data.loc[i.Index, final_charge] = minimum

    def process_volume(self, insert_into='last', check_many=True):
        loc_attiki = self.data[tomeas] == 'ΑΤΤΙΚΗ'
        attiki = self.data.loc[loc_attiki].copy().reset_index()

        attiki[final_charge] = 0.0

        hold_idx = []
        hold_volume = []
        hold_charge = []

        minimum_volume = 0.45

        for i in attiki.itertuples():
            minimum_charge = self.get_minimum(i.Γεωγραφικός_Τομέας,
                                              i.Περιοχή_Παράδοσης,
                                              self.except_areas,
                                              self.except_value)

            if check_many:
                if check_idxs(attiki,
                              i.Index,
                              info_map[self.map_name]['check_idxs']):
                    hold_idx.append(i.index)
                    hold_volume.append(i.Όγκος)
                    hold_charge.append(i.Συνολική_Χρέωση)
                else:
                    if hold_charge:
                        hold_idx.append(i.index)
                        hold_volume.append(i.Όγκος)
                        hold_charge.append(i.Συνολική_Χρέωση)

                        whole_volume = round2(sum(hold_volume))

                        if whole_volume > minimum_volume:
                            for idx, value in zip(hold_idx, hold_charge):
                                self.data.loc[idx, final_charge] = value
                        else:
                            if insert_into == 'last':
                                self.data.loc[
                                    i.index, final_charge] = minimum_charge
                            else:
                                _position = hold_charge.index(max(hold_charge))
                                _df_index = hold_idx[_position]
                                self.data.loc[
                                    _df_index, final_charge] = minimum_charge

                        hold_idx = []
                        hold_charge = []
                        hold_volume = []
                    else:
                        if i.Όγκος > minimum_volume:
                            self.data.loc[
                                i.index, final_charge] = i.Συνολική_Χρέωση
                        else:
                            self.data.loc[
                                i.index, final_charge] = minimum_charge
            else:
                is_in_excepted_areas = any(
                    [_area in i.Περιοχή_Παράδοσης for _area in self.except_areas])

                if i.Όγκος > minimum_volume and not is_in_excepted_areas:
                    self.data.loc[
                        i.index, final_charge] = i.Συνολική_Χρέωση
                elif i.Συνολική_Χρέωση > minimum_charge:
                    self.data.loc[i.index, final_charge] = i.Συνολική_Χρέωση
                else:
                    self.data.loc[i.index, final_charge] = minimum_charge

    def process(self):
        self._preprocess()

        self.log("Processing...", Display.INFO)

        self.data[paletes_dist_charge] = self.data.apply(
            lambda x: self.get_cost(x[pelatis], x[tomeas], paleta,
                                    x[paletes]), axis=1)

        self.data[kivotia_lampades_dist_charge] = ''
        self.data[kivotia_paixnidia_dist_charge] = ''

        self.data[ogkos_dist_charge] = self.data.apply(
            lambda x: self.get_cost(x[pelatis], x[tomeas], kuviko,
                                    x[ogkos]), axis=1)

        self.data[total_charge] = sum([self.data[paletes_dist_charge],
                                       self.data[ogkos_dist_charge]])

        self.process_rows()
        self.process_volume(check_many=False)

        self.data[paradosi] = self.data[paradosi].replace("<NULL>", "")

        self.data.loc[
            self.data[apostoli] == idiofortosi, final_charge] = 0.00

        self.process_epinaulo()
        
        self.data[final_dist_charge] = self.data[final_charge]

        self.data = self.data[info_map[self.map_name]['akl_cols']]

        self.data.columns = info_map[self.map_name]['formal_cols']

        self.log(f"Data Process Complete: [{self.data.shape[0]}] records\n",
                 Display.INFO)

        self.giochi_crate.process()

        self.to_export = True

    def export(self, output=None):
        if self.to_export and self.giochi_crate.to_export:
            self.log("Saving data...", Display.INFO)

            mask1 = (self.data[c_2space(tomeas)] == 'ΑΤΤΙΚΗ') & (
                self.data[c_2space(apostoli)] == atlog)
            mask2 = self.data[c_2space(apostoli)] == idiofortosi
            mask3 = (self.data[c_2space(pelatis)] == 'JUMBO Α.Ε.Ε') & (
                self.data[c_2space(tomeas)] == 'ΣΤ.ΕΛΛΑΔΑ – ΕΥΒΟΙΑ') & (
                self.data[c_2space(apostoli)] == atlog)

            _kuviko = self.data.loc[~(mask1 | mask2 | mask3)].copy().drop(
                columns=[c_2space(paletes_dist_charge),
                         c_2space(kivotia_lampades_dist_charge),
                         c_2space(kivotia_paixnidia_dist_charge)])

            if self.sheet_name == 0 or self.sheet_name is None:
                sheet_name = 'Τιμολόγηση'
            else:
                sheet_name = f'Τιμολόγηση_{self.sheet_name}'

            crate_sheet = "Τιμολόγηση_Διανομή_Κιβωτίου"
            kuviko_sheet = "Τιμολόγηση_Διανομή_Κυβικού"

            if not self.output:
                with pd.ExcelWriter(self.data_file,
                                    engine='openpyxl',
                                    mode='a') as xlsx:
                    self.data.to_excel(xlsx, sheet_name=sheet_name, index=False)
                    _kuviko.to_excel(xlsx,
                                     sheet_name=kuviko_sheet,
                                     index=False)
                    self.giochi_crate.data.to_excel(xlsx,
                                                    sheet_name=crate_sheet,
                                                    index=False)

                self.log(f"Appended new sheets to original data",
                         Display.INFO)
            else:
                with pd.ExcelWriter(self.output) as xlsx:
                    self.data.to_excel(xlsx,
                                       sheet_name=sheet_name,
                                       index=False)
                    _kuviko.to_excel(xlsx,
                                     sheet_name=kuviko_sheet,
                                     index=False)
                    self.giochi_crate.data.to_excel(xlsx,
                                                    sheet_name=crate_sheet,
                                                    index=False)
                self.log(f"Exported file: {self.output}", Display.INFO)
        else:
            self.log("Can't export data. No processing was performed",
                     Display.INFO)
