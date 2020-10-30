# -*- coding: utf-8 -*-

# author: Konstantinos Aznavouridis
# email: kaznavouridis@gmail.com
# github: kosazna

# This accounting automation was developed for ATTIKH KINISI LOGISTICS S.A.
# Always automate the boring stuff ;)

import pandas as pd
import sys
from pathlib import Path


def get_cost(cost_table, region, material, quantity=None):
    if region == "ΕΞΑΓΩΓΗ":
        return 0
    else:
        try:
            if quantity is None:
                return cost_table.loc[region, material]

            if material == "Παλέτα":
                if region != 'ΑΤΤΙΚΗ':
                    return cost_table.loc[region, material] * quantity
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
                return cost_table.loc[region, material] * quantity
        except KeyError:
            return 0


def main(data_file=None, cost_file=None):
    print("\nProcessing...\n")

    parent = Path(data_file).parent

    sort_n_group = ['Ημερομηνία', 'Επωνυμία Πελάτη', 'Γεωγραφικός Τομέας',
                    'Περιοχή Παράδοσης']

    data = pd.read_excel(data_file).sort_values(sort_n_group).dropna(
        subset=['Επωνυμία Πελάτη']).reset_index(drop=True)
    costs = pd.read_excel(cost_file).set_index('Γεωγραφικός Τομέας', drop=True)

    original_columns = data.columns.tolist()
    data.columns = [item.replace(' ', '_') for item in data.columns.str.strip()]

    data['Κενά_Βαρέλια'] = data['Κενά_Βαρέλια'].fillna(0).astype(int)
    data['Περιοχή_Παράδοσης'] = data['Περιοχή_Παράδοσης'].fillna("<NULL>")

    missing_region = data['Γεωγραφικός_Τομέας'].isna().sum()
    if bool(missing_region):
        print("[WARNING] - Column contains missing values.")
        print(f"    'Γεωγραφικός Τομέας' : {missing_region}\n")

    data['Χρέωση_Διανομής_Παλέτας'] = data.apply(
        lambda x: get_cost(costs, x['Γεωγραφικός_Τομέας'], 'Παλέτα',
                           x['Παλέτες']), axis=1)

    data['Χρέωση_Διανομής_Κιβωτίου'] = data.apply(
        lambda x: get_cost(costs, x['Γεωγραφικός_Τομέας'], 'Κιβώτιο',
                           x['Κιβώτια']), axis=1)

    data['Χρέωση_Διανομής_Βαρελιού'] = data.apply(
        lambda x: get_cost(costs, x['Γεωγραφικός_Τομέας'], 'Βαρέλι',
                           x['Βαρέλια']), axis=1)

    data['Χρέωση_Διανομής_Κενού_Βαρελιού'] = data.apply(
        lambda x: get_cost(costs, x['Γεωγραφικός_Τομέας'], 'Κενό Βαρέλι',
                           x['Κενά_Βαρέλια']), axis=1)

    data['Συνολική_Χρέωση'] = sum(
        [data['Χρέωση_Διανομής_Παλέτας'], data['Χρέωση_Διανομής_Κιβωτίου'],
         data['Χρέωση_Διανομής_Βαρελιού'],
         data['Χρέωση_Διανομής_Κενού_Βαρελιού']])

    data['Τελική_Χρέωση'] = 0.0

    hold_idx = []
    hold = []

    for i in data.itertuples():
        try:
            next_index = i.Index + 1
            con_name = i.Ημερομηνία == data.loc[next_index, 'Ημερομηνία']

            con_date = i.Επωνυμία_Πελάτη == data.loc[
                next_index, 'Επωνυμία_Πελάτη']

            con_region = i.Γεωγραφικός_Τομέας == data.loc[
                next_index, 'Γεωγραφικός_Τομέας']

            con_delivery = i.Περιοχή_Παράδοσης == data.loc[
                next_index, 'Περιοχή_Παράδοσης']

            minimum = get_cost(costs, i.Γεωγραφικός_Τομέας,
                               'Ελάχιστη Χρέωση Παραγγελίας')

            if all([con_name, con_date, con_region, con_delivery]):
                hold_idx.append(i.Index)
                hold.append(i.Συνολική_Χρέωση)
            else:
                if hold:
                    hold_idx.append(i.Index)
                    hold.append(i.Συνολική_Χρέωση)

                    if sum(hold) > minimum:
                        for idx, value in zip(hold_idx, hold):
                            data.loc[idx, 'Τελική_Χρέωση'] = value
                    else:
                        data.loc[i.Index, 'Τελική_Χρέωση'] = minimum

                    hold_idx = []
                    hold = []
                else:
                    if i.Συνολική_Χρέωση > minimum:
                        data.loc[i.Index, 'Τελική_Χρέωση'] = i.Συνολική_Χρέωση
                    else:
                        data.loc[i.Index, 'Τελική_Χρέωση'] = minimum

        except KeyError:
            data.loc[i.Index, 'Τελική_Χρέωση'] = sum(hold) + i.Συνολική_Χρέωση

    data['Περιοχή_Παράδοσης'] = data['Περιοχή_Παράδοσης'].replace("<NULL>", "")
    data.loc[data["Τρόπος_Αποστολής"] == "Ιδιοφόρτωση", "Τελική_Χρέωση"] = 0

    original_columns.extend(
        ['Χρέωση Διανομής Παλέτας', 'Χρέωση Διανομής Κιβωτίου',
         'Χρέωση Διανομής Βαρελιού',
         'Χρέωση Διανομής Κενού Βαρελιού', 'Συνολική Χρέωση',
         'Τελική Χρέωση'])

    data.columns = original_columns

    out_file = parent.joinpath("Processed_Data.xlsx")
    data.to_excel(out_file, index=False)

    print(f"Data processing finished\n   -> Exported file: {out_file}\n\n\n\n")


if __name__ == "__main__":
    print("ATTIKH KINISI LOGISTICS S.A.\n\n")

    process = input("(F)ast or (C)ustom processing?\n").upper()

    while process not in ['F', 'C']:
        print("\n[ERROR] - Enter a valid letter ('F' or 'C')\n")
        process = input("(F)ast or (C)ustom processing?\n").upper()

    if process == "F":
        try:
            working_dir = Path(sys.argv[1])
        except IndexError:
            working_dir = Path(__file__).parent.parent

        data_path = working_dir.joinpath("DB_Data.xlsx")
        costs_path = working_dir.joinpath(".templates\\Region_Costs.xlsx")

        main(data_file=data_path, cost_file=costs_path)
    elif process == "C":
        data_path = input("\nFile with the database data:\n").strip('"').strip(
            "'")
        costs_path = input('\nFile with costs per region:\n').strip('"').strip(
            "'")
        main(data_file=data_path, cost_file=costs_path)
