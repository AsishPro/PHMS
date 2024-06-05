import pandas as pd


path1 = 'Symptom-severity.csv'
path2 = 'med.xlsx'
path3='disease_category.xlsx'
path4='category_doctors_hospitals.xlsx'
path5='medicines_indetail.xlsx'
path6='medicines_description2.xlsx'

df1=pd.read_csv(path1)
l=[i for i in range(1,len(df1)+1)]
df1['weight']=l

m={}    


for i,j in enumerate(df1['Symptom']):
    if j not in m:
        m[j]=i+1
    else:
        continue
m['none']=0
# print(m)
    

sl=list(m)
# print(m)

disease={
 'Fungal infection': 0,
 'Allergy': 1,
 'GERD': 2,
 'Chronic cholestasis': 3,
 'Drug Reaction': 4,
 'Peptic ulcer disease': 5,
 'AIDS': 6,
 'Diabetes': 7,
 'Gastroenteritis': 8,
 'Bronchial Asthma': 9,
 'Hypertension': 10,
 'Migraine': 11,
 'Cervical spondylosis': 12,
 'Paralysis (brain hemorrhage)': 13,
 'Jaundice': 14,
 'Malaria': 15,
 'Chickenpox': 16,
 'Dengue': 17,
 'Typhoid': 18,
 'hepatitis A': 19,
 'Hepatitis B': 20,
 'Hepatitis C': 21,
 'Hepatitis D': 22,
 'Hepatitis E': 23,
 'Alcoholic hepatitis': 24,
 'Tuberculosis': 25,
 'Common Cold': 26,
 'Pneumonia': 27,
 'Dimorphic hemmorhoids(piles)': 28,
 'Heart attack': 29,
 'Varicose veins': 30,
 'Hypothyroidism': 31,
 'Hyperthyroidism': 32,
 'Hypoglycemia': 33,
 'Osteoarthristis': 34,
 'Arthritis': 35,
 '(vertigo) Paroymsal  Positional Vertigo': 36,
 'Acne': 37,
 'Urinary tract infection': 38,
 'Psoriasis': 39,
 'Impetigo': 40,
 'no disease':41}

dl=list(disease.keys())
# print(dl)

disease=list(disease)

medicines=pd.read_excel(path2)

categories=pd.read_excel(path3)
# print(categories[categories['Disease']=='AIDS']['Category1'].values[0])

doctor=pd.read_excel(path4)

med_detailed=pd.read_excel(path5)

medicines_desc=pd.read_excel(path6)