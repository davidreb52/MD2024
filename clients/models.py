from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Clients(models.Model):
    code= models.fields.CharField(max_length=100, default='')
    CClient= models.fields.CharField(max_length=100, default='')
    Sommeil= models.fields.CharField(max_length=100, default='NONE')
    Civilite= models.fields.CharField(max_length=100, default='')
    Nom= models.fields.CharField(max_length=100, default='')
    Prenom= models.fields.CharField(max_length=100, default='')
    Contact= models.fields.CharField(max_length=100, default='')
    Rue_1= models.fields.CharField(max_length=100, default='')
    Rue_2= models.fields.CharField(max_length=100, default='')
    CP= models.fields.CharField(max_length=100, default='')
    Ville= models.fields.CharField(max_length=100, default='')
    Pays= models.fields.CharField(max_length=100, default='')
    Telephone= models.fields.CharField(max_length=100, default='')
    Telephone2= models.fields.CharField(max_length=100, default='')
    Fax= models.fields.CharField(max_length=100, default='')
    Portable= models.fields.CharField(max_length=100, default='')
    Adresse= models.fields.CharField(max_length=100, default='')
    Internet= models.fields.CharField(max_length=100, default='')
    EMail= models.fields.CharField(max_length=100, default='')
    Secteur= models.fields.CharField(max_length=100, default='')
    Commercial= models.fields.CharField(max_length=100, default='')
    Activite= models.fields.CharField(max_length=100, default='NONE')
    Categorie= models.fields.CharField(max_length=100, default='')
    Compte= models.fields.CharField(max_length=100, default='')
    Mode_de_Reglement= models.fields.CharField(max_length=100, default='')
    Risque= models.fields.CharField(max_length=100, default='')
    Remise= models.fields.CharField(max_length=100, default='')
    Plafond_en_Cours= models.fields.CharField(max_length=100, default='')
    Banque_Client= models.fields.CharField(max_length=100, default='')
    RIB= models.fields.CharField(max_length=100, default='')
    Memo= models.fields.CharField(max_length=100, default='')
    Adresse= models.fields.CharField(max_length=100, default='NONE')
    Date_de_creation= models.fields.CharField(max_length=100, default='')
    Date_de_MAJ= models.fields.CharField(max_length=100, default='')
    Champs_Sup_1= models.fields.CharField(max_length=100, default='')
    Champs_Sup_2= models.fields.CharField(max_length=100, default='')
    Champs_Sup_3= models.fields.CharField(max_length=100, default='')
    Champs_Sup_4= models.fields.CharField(max_length=100, default='')
    Champs_Sup_5= models.fields.CharField(max_length=100, default='')
    def __str__(self):
        """
        """
        return f"{self.code}"

class TypeMateriaux(models.Model):
    """
    """
    Code_Type= models.fields.CharField(max_length=255, default='', unique=True)
    Designation= models.fields.TextField(default='')
    Unite= models.fields.CharField(max_length=10, default='')
    Coef_FG= models.fields.FloatField()
    Coef_Benefice= models.fields.FloatField()

class Materiaux(models.Model):
    """
        Type: type d'enregistrement: matériaux, mémo, Engin, Sous-traitance, ...
        Code: Code de l'élément STR*255
        Designation: Désignation STR
        Complement: Complément de désigantion STR
        Unite: 
        Prix_tarif
        Remise
        PAUHF
        PAU
        FG
        PRU
        Benefice
    """
    Type= models.ForeignKey(TypeMateriaux, to_field= 'Code_Type', null=True, on_delete=models.SET_NULL)
    #Type= models.fields.IntegerField()#validators=[MinValueValidator(0), MaxValueValidator(999999)]
    Code= models.fields.CharField(max_length=255, default='')
    Designation= models.fields.TextField(default='')
    Complement= models.fields.TextField(default='')
    Unite= models.fields.CharField(max_length=10, default='')
    Prix_tarif= models.fields.FloatField()
    Remise= models.fields.FloatField()
    PAUHF= models.fields.FloatField()
    PAU= models.fields.FloatField()
    FG= models.fields.FloatField()
    PRU= models.fields.FloatField()
    Benefice= models.fields.FloatField()
    PVU= models.fields.FloatField()
    Coef_de_perte= models.fields.FloatField()
    Date_MAJ= models.fields.TextField(default='')
    Famille= models.fields.CharField(max_length=100, default='')
    Fournisseur= models.fields.CharField(max_length=100, default='')
    Code_barre= models.fields.CharField(max_length=20, default='')
    TypeMO= models.fields.IntegerField()
    CodeMO= models.fields.CharField(max_length=100, default='')
    QteMO= models.fields.FloatField()
    FGMO= models.fields.FloatField()
    BenefMO= models.fields.FloatField()
    PVUMO= models.fields.FloatField()
    Metre= models.fields.TextField(default='')

    
def ajoutClientsCSV():
    """
        Ajout de données clients depuis un fichier CSV
    """
    import csv
    print("Ajout Client depuis un fichier CSV")
    # Table de conversion des nom de champs de la table Clients
    tableConvertField= {
        'CClient': 'CClient',
        'Sommeil': 'Sommeil',
        'Civilite': 'Civilite',
        'Nom': 'Nom',
        'Prenom': 'Prenom',
        'Contact': 'Contact',
        'Rue 1': 'Rue_1',
        'Rue 2': 'Rue_2',
        'CP': 'CP',
        'Ville': 'Ville',
        'Pays': 'Pays',
        'Telephone': 'Telephone',
        'Telephone2': 'Telephone2',
        'Fax': 'Fax',
        'Portable': 'Portable',
        'Adresse Internet': 'Adresse_Internet',
        'EMail': 'EMail',
        'Secteur': 'Secteur',
        'Commercial': 'Commercial',
        'Activite': 'Activite',
        'Categorie': 'Categorie',
        'Compte': 'Compte',
        'Mode de Reglement': 'Mode_de_Reglement',
        'Risque': 'Risque',
        'Remise': 'Remise',
        'Plafond en Cours': 'Plafond_en_Cours',
        'Banque Client': 'Banque_Client',
        'RIB': 'RIB',
        'Memo': 'Memo',
        'Adresse': 'Adresse',
        'Date de creation': 'Date_de_creation',
        'Date de MAJ': 'Date_de_MAJ',
        'Champs Sup 1': 'Champs_Sup_1',
        'Champs Sup 2': 'Champs_Sup_2',
        'Champs Sup 3': 'Champs_Sup_3',
        'Champs Sup 4': 'Champs_Sup_4',
        'Champs Sup 5': 'Champs_Sup_5'
    }
    nomFichier="C:\\Users\\rebel\\Dropbox\\REBELOI\\DevisFactures2024\\MD2000\\clients.csv"
    with open(nomFichier, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['CClient'], row['Nom'])
            client= Clients()
            for key, value in tableConvertField.items():
                client.__dict__[value]= row[key]
            client.save()
""" https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django/7514699-configurez-un-nouveau-projet-avec-lutilitaire-de-ligne-de-commande-de-django"""


def ajoutMateriaux():
    """
        Ajout de données materiaux depuis un fichier CSV
    """
    import csv

    # Table de conversion des nom de champs de la table Materiaux
    # Liste des champs da la table matériaux MD2000
    #listeChampMD2000= ["Type","Code","Designation","Complement","Libelle Commercial","Libelle Technique","Unite","Prix tarif","Remise","PAUHF","PAU","FG","PRU","Benefice","PVU","Coef de perte","Cadence","TVA","Date MAJ","Mot clef","Famille","IdFHier","Fournisseur","Date d'effet","Graphique","Graphique (chemin)","Code barre","Code regroupement","Code substitution","CarTech Code 1","CarTech Qte 1","CarTech Code 2","CarTech Qte 2","CarTech Code 3","CarTech Qte 3","PoseCheck","RemiseRadio","PVURadio","PVUPRadio","TypeMO","CodeMO","QteMO","FGMO","BenefMO","PVUMO","SupprimeCheck","SommeilCheck","PauFrnt","CentFrnt","FrntRadio","FrntCheck","Code comptable","Analytique1","Analytique2","Analytique3","AnalytiqueRadio","UCCarTech1","UCUnite1","UCVal1","UCCarTech2","UCUnite2","UCVal2","UCCarTech3","UCUnite3","UCVal3","UCCarTech4","UCUnite4","UCVal4","UCCarTech5","UCUnite5","UCVal5","Fournisseur1","CodeArticleFr1","Fournisseur2","CodeArticleFr2","Fournisseur3","CodeArticleFr3","Metre","CAOKey","CAOBin"]
    importcsv(nomFichier= "C:\\Users\\rebel\\Dropbox\\REBELOI\\DevisFactures2024\\MD2000\\materiaux.csv",
              listeChampMD2000= ["Type", "Code", "Designation", "Complement", "Unite", "Prix tarif", "Remise", "PAUHF", "PAU","FG","PRU",
                                 "Benefice","PVU","Coef de perte","Date MAJ", "Famille","Fournisseur","Code barre","TypeMO","CodeMO",
                                 "QteMO","FGMO","BenefMO","PVUMO","Metre"],
              table= Materiaux(),
              champCode= 'Code')
    
def ajoutTypeMateriaux():
    """
        Ajout de données TypeMateriaux depuis un fichier CSV
    """
    importcsv(nomFichier= "C:\\Users\\rebel\\Dropbox\\REBELOI\\DevisFactures2024\\MD2000\\type.csv",
              listeChampMD2000= ["Code Type","Designation","Unite","Coef FG","Coef Benefice"],
              table= TypeMateriaux(),
              champCode= 'Code Type')
    

def importcsv(nomFichier, listeChampMD2000, table, champCode=None):
    """
    """
    import csv
    import copy
    tableConvertField= {}
    # Conversion des champs MD2000 contenant des espaces par des tirets bas
    for lc in listeChampMD2000:
        lcMd2000= lc
        lc= lc.replace(" ","_")
        lc= lc.replace("'","")
        lc= lc.replace("(","")
        lc= lc.replace(")","")
        tableConvertField[lcMd2000]= lc
    i=0
    with open(nomFichier, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if champCode is not None:
                print(i, row[champCode])
            tableSqlite= copy.deepcopy(table)
            #print(type(materiaux.FrntCheck))
            for key, value in tableConvertField.items():
                tableSqlite.__dict__[value]= convertType(row[key], type(row[key]))
            i+=1
            print("    Sauvegarde de l'enregistrement...")
            tableSqlite.save()
            print("    OK")

def convertType(data, type):
    """
     Conversion de type
    """
    if isinstance(data, bytes):
        bytes(data)
    if isinstance(data, int):
        int(data)
    if isinstance(data, float):
        float(data)        
    if isinstance(data, str):
        str(data)
    if isinstance(data, bool):
        bool(data)
    return data
def importAllCVS():
    """ 
        iMPORTATION DE L4ENSEMBLE DES cvs
    """
    ajoutClientsCSV()
    ajoutTypeMateriaux()
    ajoutMateriaux()