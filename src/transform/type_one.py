import pandas as pd
from pathlib import Path
from ..validate.data import TypeOneValidator

sort_n_group = ['Ημερομηνία', 'Επωνυμία Πελάτη', 'Γεωγραφικός Τομέας',
                'Περιοχή Παράδοσης']


class TypeOneTransformer:
    def __init__(self, data_filepath: (str, Path), cost_filepath: (str, Path)):
        self.data_file = Path(data_filepath)
        self.cost_file = Path(cost_filepath)
        self.working_dir = self.data_file.parent
        self.output = self.working_dir.joinpath("Processed_Data.xlsx")

        self.data = pd.read_excel(self.data_file).sort_values(
            sort_n_group).dropna(subset=['Επωνυμία Πελάτη']).reset_index(
            drop=True)

        self.costs = pd.read_excel(self.cost_file).set_index(
            'Γεωγραφικός Τομέας', drop=True)

        self.original_columns = self.data.columns.tolist()
        self.data.columns = [col.replace(' ', '_') for col in
                             self.data.columns.str.strip()]
        self.preprocessed = False
        self.validator = TypeOneValidator(self.data)

    def _check_next_idx(self, index, column):
        try:
            return self.data[index, column] == self.data[index + 1, column]
        except KeyError:
            return False

    def _get_cost(self, region: str, material: str, quantity: int = None):
        if region == "ΕΞΑΓΩΓΗ":
            return 0
        else:
            try:
                if quantity is None:
                    return self.costs.loc[region, material]

                if material == "Παλέτα":
                    if region != 'ΑΤΤΙΚΗ':
                        return self.costs.loc[region, material] * quantity
                    else:
                        if quantity >= 21:
                            return 175
                        elif quantity >= 11:
                            return quantity * 11.5
                        elif quantity > 0:
                            return quantity * 15
                        else:
                            return 0
                else:
                    return self.costs.loc[region, material] * quantity
            except KeyError:
                return 0

    def _preprocess(self):
        self.data['Κενά_Βαρέλια'] = self.data['Κενά_Βαρέλια'].fillna(
            0).astype(
            int)
        self.data['Περιοχή_Παράδοσης'] = self.data[
            'Περιοχή_Παράδοσης'].fillna(
            "<NULL>")

        self.preprocessed = True

    def process(self):
        if not self.preprocessed:
            self._preprocess()

        self.validator.validate()

        self.data['Χρέωση_Διανομής_Παλέτας'] = self.data.apply(
            lambda x: self._get_cost(x['Γεωγραφικός_Τομέας'],
                                     'Παλέτα',
                                     x['Παλέτες']), axis=1)

        self.data['Χρέωση_Διανομής_Κιβωτίου'] = self.data.apply(
            lambda x: self._get_cost(x['Γεωγραφικός_Τομέας'],
                                     'Κιβώτιο',
                                     x['Κιβώτια']), axis=1)

        self.data['Χρέωση_Διανομής_Βαρελιού'] = self.data.apply(
            lambda x: self._get_cost(x['Γεωγραφικός_Τομέας'],
                                     'Βαρέλι',
                                     x['Βαρέλια']), axis=1)

        self.data['Χρέωση_Διανομής_Κενού_Βαρελιού'] = self.data.apply(
            lambda x: self._get_cost(x['Γεωγραφικός_Τομέας'],
                                     'Κενό Βαρέλι',
                                     x['Κενά_Βαρέλια']), axis=1)

        self.data['Συνολική_Χρέωση'] = sum(
            [self.data['Χρέωση_Διανομής_Παλέτας'],
             self.data['Χρέωση_Διανομής_Κιβωτίου'],
             self.data['Χρέωση_Διανομής_Βαρελιού'],
             self.data['Χρέωση_Διανομής_Κενού_Βαρελιού']])

        self.data['Τελική_Χρέωση'] = 0.0

        hold_idx = []
        hold = []

        for i in self.data.itertuples():
            same_name = self._check_next_idx(i.Index, "Επωνυμία_Πελάτη")

            same_date = self._check_next_idx(i.Index, "Ημερομηνία")

            same_region = self._check_next_idx(i.Index, "Γεωγραφικός_Τομέας")

            same_delivery = self._check_next_idx(i.Index, "Περιοχή_Παράδοσης")

            minimum = self._get_cost(i.Γεωγραφικός_Τομέας,
                                     'Ελάχιστη Χρέωση Παραγγελίας')

            if all([same_name, same_date, same_region, same_delivery]):
                hold_idx.append(i.Index)
                hold.append(i.Συνολική_Χρέωση)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)

                    if sum(hold) > minimum:
                        for idx, value in zip(hold_idx, hold):
                            self.data.loc[idx, 'Τελική_Χρέωση'] = value
                    else:
                        self.data.loc[i.Index, 'Τελική_Χρέωση'] = minimum

                    hold_idx = []
                    hold = []
                else:
                    if i.Συνολική_Χρέωση > minimum:
                        self.data.loc[
                            i.Index, 'Τελική_Χρέωση'] = i.Συνολική_Χρέωση
                    else:
                        self.data.loc[i.Index, 'Τελική_Χρέωση'] = minimum

        self.data['Περιοχή_Παράδοσης'] = self.data['Περιοχή_Παράδοσης'].replace(
            "<NULL>", "")

        self.data.loc[
            self.data["Τρόπος_Αποστολής"] == "Ιδιοφόρτωση", "Τελική_Χρέωση"] = 0

        self.original_columns.extend(
            ['Χρέωση Διανομής Παλέτας', 'Χρέωση Διανομής Κιβωτίου',
             'Χρέωση Διανομής Βαρελιού',
             'Χρέωση Διανομής Κενού Βαρελιού', 'Συνολική Χρέωση',
             'Τελική Χρέωση'])

        self.data.columns = self.original_columns

        print(f"    Data processing finished: [{self.data.shape[0]}] records\n")

    def export(self):
        self.data.to_excel(self.output, index=False)
        print(f"    Exported file: {self.output}\n\n\n\n")
