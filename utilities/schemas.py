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

info_map = {
    "Concepts":
        {"init_ncols": 12,
         "formal_cols": list(map(c_2space, CONCEPTS)),
         "akl_cols": CONCEPTS,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi],
         "drop": list(map(c_2space, [imerominia, pelatis, tomeas]))},
    "PT Beverages - Spirits":
        {"init_ncols": 17,
         "formal_cols": list(map(c_2space, PTB_SPIRITS)),
         "akl_cols": PTB_SPIRITS,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi],
         "drop": list(map(c_2space, [imerominia, pelatis, tomeas]))},
    "PT Beverages - Lavazza":
        {"init_ncols": 14,
         "formal_cols": list(map(c_2space, PTB_LAVAZZA)),
         "akl_cols": PTB_LAVAZZA,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  poli],
         "drop": list(map(c_2space, [imerominia, pelatis, tomeas]))},
    "Cavino":
        {"init_ncols": 13,
         "formal_cols": list(map(c_2space, CAVINO)),
         "akl_cols": CAVINO,
         "sort": [imerominia_apostolis,
                  pelatis,
                  tomeas,
                  paradosi],
         "drop": list(map(c_2space, [imerominia_apostolis, pelatis, tomeas]))},
    "Giochi":
        {"init_ncols": 13,
         "formal_cols": list(map(c_2space, GIOCHI)),
         "akl_cols": GIOCHI,
         "sort": [imerominia,
                  pelatis,
                  tomeas,
                  paradosi,
                  paradosi_address],
         "drop": list(map(c_2space, [imerominia, pelatis, tomeas])),
         "check_idxs": [imerominia,
                        pelatis,
                        tomeas,
                        paradosi,
                        paradosi_address]}
}
