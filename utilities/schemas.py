# -*- coding: utf-8 -*-

from atakl.utilities.utils import c_2space

AKL_VERSION = '2.0'
split_char = '@'

# Type ONE columns for processing
paraggelia = "Παραγγελία"
imerominia = "Ημερομηνία"
deltio = "Δελτίο_Αποστολής"
pelatis = "Επωνυμία_Πελάτη"
tomeas = "Γεωγραφικός_Τομέας"
paradosi = "Περιοχή_Παράδοσης"
paletes = "Παλέτες"
kivotia = "Κιβώτια"
kola = "Κόλα"
varelia = "Βαρέλια"
kena_varelia = "Κενά_Βαρέλια"
apostoli = "Τρόπος_Αποστολής"
paletes_dist_charge = "Χρέωση_Διανομής_Παλέτας"
kivotia_dist_charge = "Χρέωση_Διανομής_Κιβωτίου"
varelia_dist_charge = "Χρέωση_Διανομής_Βαρελιού"
kena_varelia_dist_charge = "Χρέωση_Διανομής_Κενού_Βαρελιού"
total_charge = "Συνολική_Χρέωση"
final_charge = "Τελική_Χρέωση"

# Type Two columns for processing
parastatiko = "Παραστατικό"
kodikos = "Κωδικός_Είδους"
perigrafi = "Περιγραφή"
tsantes = "Τσάντες"
temaxia = "Τεμάχια"
ompreles = "Διαφ_Ομπρέλες"
paletes_san = "Παλέτες_San_Miguel"
tsantes_dist_charge = "Χρέωση_Διανομής_Τσάντας"
ompreles_dist_charge = "Χρέωση_Διανομής_Διαφ_Ομπρέλας"

poli = "Πόλη"
sunolika_temaxia = "Συνολικά_Τεμάχια"
atofia_paleta = "Ατόφια_Παλέτα"
mixanes = "Μηχανές"
upoloipo_se_temaxia = "Υπόλοιπο_σε_Τεμάχια"
atofia_paleta_charge = "Χρέωση_Ατόφιας_Παλέτας"
kivotia_charge = "Χρέωση_Κιβωτίων"
mixanes_charge = "Χρέωση_Μηχανών"

kodikos_paraggelias = "Κωδικός_Παραγγελίας"
kodikos_arxikis_paraggelias = "Κωδικός_Αρχικής_Παραγγελίας"
imerominia_apostolis = "Ημερομηνία_Αποστολής"
paratiriseis = "Παρατηρήσεις"
kola_dist_charge = "Χρέωση_Διανομής_Κόλα"
strech = "Stretch_Filming"

paradosi_address = "Διεύθυνση_Παράδοσης"
kivotia_paixnidia = "Κιβώτια_Παιχνίδια"
kivotia_ogkou = "Κιβώτια_Μεγάλου_Όγκου"
ogkos = "Όγκος"
kivotia_lampades_dist_charge = "Χρέωση_Διανομής_Κιβωτίων_Λαμπάδες"
kivotia_paixnidia_dist_charge = "Χρέωση_Διανομής_Κιβωτίων_Παιχνίδια"
ogkos_dist_charge = "Χρέωση_Διανομής_Όγκου"
final_dist_charge = "Σύνολο_Χρέωσης_Διανομής"

imerominia_paradosis = "Ημερομηνία_Παράδοσης"
poli_paradosis = "Πόλη_Παράδοσης"
lampades = "Λαμπάδες"
sinolikos_ogkos = "Συνολικός_Όγκος_(m3)"
kivotio_charge = "Χρέωση_Κιβωτίου"

# ESSSE

order_code = "Order_Code"
distribution_date = "Distribution_Date"
delivery_note = "Delivery_Note"
customer_code = "Customer_Code"
customer_name = "Customer_Name"
delivery_area = "Delivery_Area"
city = "City"
delivery_method = "Delivery_Method"
product_code = "Product_Code"
product_description = "Product_Description"
total_pcs = "Total_pcs"
full_pallets = "Full_pallets"
cartons = "Cartons"
pieces = "Pieces"
pallets = "Pallets"
weight = "Weight_in_kg"
notes = "Notes"
delivery_cost = "Delivery_Cost"

# Cost file keys
paleta = "Παλέτα"
kivotio = "Κιβώτιο"
vareli = "Βαρέλι"
keno_vareli = "Κενό Βαρέλι"
elaxisti = "Ελάχιστη Χρέωση Παραγγελίας"
mixani = "Μηχανή"
tsanta = "Τσάντα"
omprela = "Διαφ Ομπρέλα"
kuviko = "Κυβικό"
minimum_charge = "Minimum Charge"

atlog = "ATLOG"
idiofortosi = "Ιδιοφόρτωση"

DATA_DROP = list(map(c_2space, [imerominia, pelatis, tomeas]))

CONCEPTS = [paraggelia,
            imerominia,
            deltio,
            pelatis,
            tomeas,
            paradosi,
            paletes,
            kivotia,
            kola,
            varelia,
            kena_varelia,
            apostoli,
            paletes_dist_charge,
            kivotia_dist_charge,
            varelia_dist_charge,
            kena_varelia_dist_charge,
            total_charge,
            final_charge]

PTB_SPIRITS = [paraggelia,
               imerominia,
               parastatiko,
               pelatis,
               tomeas,
               paradosi,
               apostoli,
               kodikos,
               perigrafi,
               paletes,
               kivotia,
               tsantes,
               temaxia,
               varelia,
               ompreles,
               paletes_san,
               kola,
               paletes_dist_charge,
               kivotia_dist_charge,
               tsantes_dist_charge,
               varelia_dist_charge,
               ompreles_dist_charge,
               total_charge,
               final_charge]

PTB_LAVAZZA = [paraggelia,
               imerominia,
               parastatiko,
               pelatis,
               tomeas,
               poli,
               apostoli,
               kodikos,
               perigrafi,
               sunolika_temaxia,
               atofia_paleta,
               kivotia,
               upoloipo_se_temaxia,
               mixanes,
               atofia_paleta_charge,
               kivotia_charge,
               mixanes_charge,
               total_charge,
               final_charge]

CAVINO = [kodikos_paraggelias,
          kodikos_arxikis_paraggelias,
          imerominia_apostolis,
          parastatiko,
          pelatis,
          tomeas,
          paradosi,
          apostoli,
          paletes,
          kivotia,
          temaxia,
          kola,
          paratiriseis,
          kola_dist_charge,
          strech]

GIOCHI = [paraggelia,
          imerominia,
          parastatiko,
          pelatis,
          tomeas,
          paradosi,
          paradosi_address,
          apostoli,
          paletes,
          kivotia_paixnidia,
          kivotia_ogkou,
          temaxia,
          ogkos,
          paletes_dist_charge,
          kivotia_lampades_dist_charge,
          kivotia_paixnidia_dist_charge,
          ogkos_dist_charge,
          final_dist_charge]

GIOCHI_CRATE = [paraggelia,
                imerominia_paradosis,
                deltio,
                pelatis,
                tomeas,
                poli_paradosis,
                paradosi_address,
                apostoli,
                kivotia,
                lampades,
                temaxia,
                sinolikos_ogkos,
                kivotio_charge]

ESSSE = [order_code,
         distribution_date,
         delivery_note,
         customer_code,
         customer_name,
         delivery_area,
         city,
         delivery_method,
         product_code,
         product_description,
         total_pcs,
         full_pallets,
         cartons,
         pieces,
         pallets,
         weight,
         notes,
         delivery_cost]

info_map = {
    "Concepts":
        {"init_ncols": 12,
         "formal_cols": list(map(c_2space, CONCEPTS)),
         "akl_cols": CONCEPTS,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi],
         "drop": list(map(c_2space, [imerominia,
                                     pelatis,
                                     tomeas])),
         "check_idxs": [imerominia,
                        pelatis,
                        tomeas,
                        paradosi,
                        apostoli],
         "validator": {"missing": [pelatis,
                                   tomeas,
                                   paradosi,
                                   apostoli],
                       "ensure_under": [(kivotia, 100)],
                       "ensure_zero": [kola]}},
    "PT Beverages - Spirits":
        {"init_ncols": 17,
         "formal_cols": list(map(c_2space, PTB_SPIRITS)),
         "akl_cols": PTB_SPIRITS,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi],
         "drop": list(map(c_2space, [imerominia,
                                     pelatis,
                                     tomeas])),
         "check_idxs": [imerominia,
                        pelatis,
                        tomeas,
                        paradosi,
                        apostoli],
         "validator": {"missing": [pelatis,
                                   tomeas,
                                   paradosi,
                                   apostoli],
                       "ensure_under": [(kivotia, 80)],
                       "ensure_zero": [temaxia,
                                       varelia,
                                       ompreles,
                                       paletes_san,
                                       kola]}},
    "PT Beverages - Lavazza":
        {"init_ncols": 14,
         "formal_cols": list(map(c_2space, PTB_LAVAZZA)),
         "akl_cols": PTB_LAVAZZA,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  poli],
         "drop": list(map(c_2space, [imerominia,
                                     pelatis,
                                     tomeas])),
         "check_idxs": [imerominia,
                        pelatis,
                        tomeas,
                        poli,
                        apostoli],
         "validator": {"missing": [pelatis,
                                   tomeas,
                                   poli,
                                   apostoli],
                       "ensure_under": [(kivotia, 80)],
                       "ensure_zero": [upoloipo_se_temaxia]}},
    "Cavino":
        {"init_ncols": 13,
         "formal_cols": list(map(c_2space, CAVINO)),
         "akl_cols": CAVINO,
         "sort": [imerominia_apostolis,
                  pelatis,
                  tomeas,
                  paradosi],
         "drop": list(map(c_2space, [imerominia_apostolis,
                                     pelatis,
                                     tomeas])),
         "check_idxs": [imerominia_apostolis,
                        pelatis,
                        tomeas,
                        paradosi,
                        apostoli],
         "validator": {"missing": [pelatis,
                                   tomeas,
                                   paradosi,
                                   apostoli],
                       "ensure_under": [(temaxia, 1)],
                       "ensure_zero": [kola]}},
    "Giochi":
        {"init_ncols": 13,
         "formal_cols": list(map(c_2space, GIOCHI)),
         "akl_cols": GIOCHI,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi,
                  paradosi_address],
         "drop": list(map(c_2space, [imerominia,
                                     pelatis,
                                     tomeas])),
         "check_idxs": [imerominia,
                        pelatis,
                        tomeas,
                        paradosi,
                        paradosi_address,
                        apostoli],
         "validator": {"missing": [imerominia,
                                   pelatis,
                                   tomeas,
                                   paradosi,
                                   apostoli],
                       "ensure_under": [],
                       "ensure_zero": [paletes, kivotia_ogkou, temaxia],
                       "no_duplicates": [imerominia,
                                         pelatis,
                                         tomeas,
                                         paradosi]}},
    "Giochi - Crate":
        {"init_ncols": 12,
         "formal_cols": list(map(c_2space, GIOCHI_CRATE)),
         "akl_cols": GIOCHI_CRATE,
         "sort": [imerominia_paradosis,
                  pelatis,
                  tomeas,
                  poli_paradosis,
                  paradosi_address],
         "drop": list(map(c_2space, [imerominia_paradosis,
                                     pelatis,
                                     tomeas])),
         "check_idxs": [imerominia_paradosis,
                        pelatis,
                        tomeas,
                        poli_paradosis,
                        paradosi_address,
                        apostoli],
         "validator": {"missing": [imerominia,
                                   pelatis,
                                   tomeas,
                                   paradosi,
                                   apostoli],
                       "ensure_under": [],
                       "ensure_zero": [lampades, temaxia],
                       "no_duplicates": [imerominia,
                                         pelatis,
                                         tomeas,
                                         paradosi]}},
    "Essse":
        {"init_ncols": 17,
         "formal_cols": list(map(c_2space, ESSSE)),
         "akl_cols": ESSSE,
         "sort": [distribution_date,
                  customer_code,
                  customer_name,
                  delivery_area,
                  city,
                  order_code],
         "drop": list(map(c_2space, [distribution_date,
                                     customer_name,
                                     delivery_area])),
         "check_idxs": [distribution_date,
                        customer_code,
                        customer_name,
                        delivery_area,
                        city,
                        delivery_method],
         "validator": {"missing": [customer_name,
                                   delivery_area,
                                   distribution_date],
                       "ensure_under": [(temaxia, 1)],
                       "ensure_zero": [pieces]}}
}
