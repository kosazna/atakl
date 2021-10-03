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
palleta_ksilo = "Παλλέτα_(Ξύλο)"

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
kostos_metaforas = "Κόστος_Μεταφοράς"

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

perioxi = "Περιοχή"
kivotia_under_007 = "Κιβώτια_κάτω_από_0,07_κ.μ."
ogkos_over_007 = "Όγκος_σε_(m3)_πάνω_από_0,07 κ.μ."
ksila_paleton = "Ξύλα_παλετών"
stock_out_charge = "Χρέωση_Stock_Out"

paletes_charge = "Χρέωση_Παλετών"

kivotia_diafimistikou = "Κιβώτια_Διαφημιστικού_Υλικού"
kivotia_ximou = "Κιβώτια_Χυμοί"
kivotia_6fialon = "Κιβώτια_6φιαλών"
kivotia_12fialon = "Κιβώτια_12φιαλών"
diafimistiko_dist_charge = "Χρέωση_Διανομής_Διαφημιστικού_Υλικού"
ximoi_dist_charge = "Χρέωση_Διανομής_Χυμών"
fiales6_dist_charge = "Χρέωση_Διανομής_6φίαλων"
fiales12_dist_charge = "Χρέωση_Διανομής_12φίαλων"

# Cost file keys
paleta = "Παλέτα"
kivotio = "Κιβώτιο"
vareli = "Βαρέλι"
keno_vareli = "Κενό Βαρέλι"
elaxisti = "Ελάχιστη Χρέωση Παραγγελίας"
megisti = "Μέγιστη Χρέωση Παραγγελίας"
mixani = "Μηχανή"
tsanta = "Τσάντα"
omprela = "Διαφ Ομπρέλα"
kuviko = "Κυβικό"
minimum_charge = "Minimum Charge"
kuviko_metro = "Κυβικό μέτρο"
ogkos_small = "Όγκος <8 m3"
ogkos_medium = "Όγκος 8-16 m3"
ogkos_large = "Όγκος >16 m3"
kuviko_eidiki_xreosi = "Κυβικό μέτρο (ειδική χρέωση)"
diafimistiko = "Χρέωση Διαφημιστικού Υλικού"
ximoi = "Χρέωση Χυμών"
fiales6 = "Χρέωση Διανομής 6φίαλων"
fiales12 = "Χρέωση Διανομής 12φίαλων"
paleta_dist_charge = "Χρέωση Διανομής Παλέτας"

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
            palleta_ksilo]

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
               strech]

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
               kostos_metaforas,
               strech]

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

COSCO_INFOQUEST = [kodikos_paraggelias,
                   kodikos_arxikis_paraggelias,
                   imerominia,
                   parastatiko,
                   pelatis,
                   tomeas,
                   paradosi_address,
                   perioxi,
                   apostoli,
                   sunolika_temaxia,
                   sinolikos_ogkos,
                   kivotia_under_007,
                   ogkos_over_007,
                   ksila_paleton,
                   paratiriseis,
                   stock_out_charge,
                   ogkos_dist_charge,
                   final_dist_charge]

ALEXANDRION = [kodikos_paraggelias,
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
               ksila_paleton,
               kola,
               paratiriseis,
               kola_dist_charge,
               strech]

KITSANELIS = [kodikos_paraggelias,
              kodikos_arxikis_paraggelias,
              imerominia_paradosis,
              deltio,
              pelatis,
              tomeas,
              poli_paradosis,
              apostoli,
              kivotia_diafimistikou,
              kivotia_ximou,
              kivotia_6fialon,
              kivotia_12fialon,
              ksila_paleton,
              diafimistiko_dist_charge,
              ximoi_dist_charge,
              fiales6_dist_charge,
              fiales12_dist_charge,
              final_dist_charge]

info_map = {
    "Concepts":
        {"init_ncols": 12,
         "date_col": imerominia,
         "formal_cols": list(map(c_2space, CONCEPTS)),
         "akl_cols": CONCEPTS,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi],
         "drop": [imerominia,
                  pelatis,
                  tomeas],
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
         "date_col": imerominia,
         "formal_cols": list(map(c_2space, PTB_SPIRITS)),
         "akl_cols": PTB_SPIRITS,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi],
         "drop": [imerominia,
                  pelatis,
                  tomeas],
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
         "date_col": imerominia,
         "formal_cols": list(map(c_2space, PTB_LAVAZZA)),
         "akl_cols": PTB_LAVAZZA,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  poli],
         "drop": [imerominia,
                  pelatis,
                  tomeas],
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
         "date_col": imerominia_apostolis,
         "formal_cols": list(map(c_2space, CAVINO)),
         "akl_cols": CAVINO,
         "sort": [imerominia_apostolis,
                  pelatis,
                  tomeas,
                  paradosi],
         "drop": [imerominia_apostolis,
                  pelatis,
                  tomeas],
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
         "date_col": imerominia,
         "formal_cols": list(map(c_2space, GIOCHI)),
         "akl_cols": GIOCHI,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi,
                  paradosi_address],
         "drop": [imerominia,
                  pelatis,
                  tomeas],
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
                       "ensure_zero": [paletes,
                                       kivotia_ogkou,
                                       temaxia],
                       "no_duplicates": [imerominia,
                                         pelatis,
                                         tomeas,
                                         paradosi]}},
    "Giochi - Crate":
        {"init_ncols": 12,
         "date_col": imerominia_paradosis,
         "formal_cols": list(map(c_2space, GIOCHI_CRATE)),
         "akl_cols": GIOCHI_CRATE,
         "sort": [imerominia_paradosis,
                  pelatis,
                  tomeas,
                  poli_paradosis,
                  paradosi_address],
         "drop": [imerominia_paradosis,
                  pelatis,
                  tomeas],
         "check_idxs": [imerominia_paradosis,
                        pelatis,
                        tomeas,
                        poli_paradosis,
                        paradosi_address,
                        apostoli],
         "validator": {"missing": [imerominia_paradosis,
                                   pelatis,
                                   tomeas,
                                   poli_paradosis,
                                   apostoli],
                       "ensure_under": [],
                       "ensure_zero": [lampades, temaxia],
                       "no_duplicates": [imerominia_paradosis,
                                         pelatis,
                                         tomeas,
                                         poli_paradosis]}},
    "Essse":
        {"init_ncols": 17,
         "date_col": distribution_date,
         "formal_cols": list(map(c_2space, ESSSE)),
         "akl_cols": ESSSE,
         "sort": [distribution_date,
                  customer_code,
                  customer_name,
                  delivery_area,
                  city,
                  order_code],
         "drop": [distribution_date,
                  customer_name,
                  delivery_area],
         "check_idxs": [distribution_date,
                        customer_code,
                        customer_name,
                        delivery_area,
                        city,
                        delivery_method],
         "validator": {"missing": [customer_name,
                                   delivery_area,
                                   distribution_date],
                       "ensure_under": [],
                       "ensure_zero": [pieces]}},
    "Cosco - Infoquest":
        {"init_ncols": 15,
         "date_col": imerominia,
         "formal_cols": list(map(c_2space, COSCO_INFOQUEST)),
         "akl_cols": COSCO_INFOQUEST,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi_address],
         "drop": [pelatis,
                  tomeas,
                  paradosi_address,
                  perioxi],
         "check_idxs": [imerominia,
                        pelatis,
                        tomeas,
                        paradosi_address,
                        perioxi,
                        apostoli],
         "validator": {"missing": [tomeas,
                                   perioxi]}},
    "Alexandrion":
        {"init_ncols": 14,
         "date_col": imerominia_apostolis,
         "formal_cols": list(map(c_2space, ALEXANDRION)),
         "akl_cols": ALEXANDRION,
         "sort": [imerominia_apostolis,
                  pelatis,
                  tomeas,
                  paradosi,
                  apostoli],
         "drop": [pelatis,
                  tomeas,
                  paradosi],
         "check_idxs": [imerominia_apostolis,
                        pelatis,
                        tomeas,
                        paradosi,
                        apostoli],
         "validator": {"missing": [tomeas,
                                   pelatis]}},
    "Kitsanelis":
        {"init_ncols": 13,
         "date_col": imerominia_paradosis,
         "formal_cols": list(map(c_2space, KITSANELIS)),
         "akl_cols": KITSANELIS,
         "sort": [imerominia_paradosis,
                  pelatis,
                  tomeas,
                  poli_paradosis,
                  apostoli],
         "drop": [pelatis,
                  tomeas,
                  poli_paradosis],
         "check_idxs": [imerominia_paradosis,
                        pelatis,
                        tomeas,
                        poli_paradosis,
                        apostoli],
         "validator": {"missing": [tomeas,
                                   paradosi]}}
}
