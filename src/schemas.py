from .utils import *

# Type ONE columns for processing
paraggelia = "Παραγγελία"
imerominia = "Ημερομηνία"
deltio = "Δελτίο Αποστολής"
pelatis = "Επωνυμία_Πελάτη"
tomeas = "Γεωγραφικός_Τομέας"
paradosi = "Περιοχή_Παράδοσης"
paletes = "Παλέτες"
kivotia = "Κιβώτια"
kola = "Κόλα"
varelia = "Βαρέλια"
kena_varelia = "Κενά_Βαρέλια"
apostoli = "Τρόπος_Αποστολής"
paletes_charge = "Χρέωση_Διανομής_Παλέτας"
kivotia_charge = "Χρέωση_Διανομής_Κιβωτίου"
varelia_charge = "Χρέωση_Διανομής_Βαρελιού"
kena_varelia_charge = "Χρέωση_Διανομής_Κενού_Βαρελιού"
total_charge = "Συνολική_Χρέωση"
final_charge = "Τελική_Χρέωση"

paleta = "Παλέτα"
kivotio = "Κιβώτιο"
vareli = "Βαρέλι"
keno_vareli = "Κενό Βαρέλι"
elaxisti = "Ελάχιστη Χρέωση Παραγγελίας"

atlog = "ATLOG"
idiofortosi = "Ιδιοφόρτωση"

DATA_SORT = list(map(undercore2space, [imerominia, pelatis, tomeas, paradosi]))

TYPE_ONE_COLUMNS = [paraggelia,
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
                    paletes_charge,
                    kivotia_charge,
                    varelia_charge,
                    kena_varelia_charge,
                    total_charge,
                    final_charge]
