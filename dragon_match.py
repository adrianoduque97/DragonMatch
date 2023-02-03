import difflib
import smtplib
from email.mime.text import MIMEText
import pandas as pd
import numpy as np


listT = []

total = []
totala = []
preferencias = []
matches = []
anti = []

def similarity(arr1,arr2):
    sm = difflib.SequenceMatcher(None, arr1, arr2)
    #print(sm.get_matching_blocks())
    return (sm.ratio())


def emailAnswers(nombres):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("HOla")
    server.starttls()
    server.login("adrianoduque97", "Asda2397+")


    msg = MIMEText("Tus matches son"+str(matches[0]))
    msg['From']='adrianoduque97@gmail.com'
    msg['Subject']="test"

    server.sendmail("adrianoduque97@gmail.com", nombres, msg.as_string())

def generateResults():
    print("generating results...")
    pref = pd.read_csv("prefrencias.csv", delimiter=',')
    pr = pref.values.tolist()

    for i in range(len(arr)):
        listT = []
        for j in range(len(arr)):
            if j in pr[i]:
                listT.append(similarity(arr[i], arr[j]))
            else:
                listT.append(0)
        total.append(listT)
    #print(total)
    df = pd.DataFrame(total, columns=labels, index=labels)
    print(df)

    df=df.multiply(1.4)

    print("\nGENERATED RESULTS\n"+str(df))

    df.to_csv("result.csv")

    return df

def generateAnti():
    print("generating antimatches...")
    for i in range(len(arr)):
        listP = []
        for j in range(len(arr)):
            listP.append(similarity(arr[i], arr[j]))
        totala.append(listP)
    #print(total)
    df = pd.DataFrame(totala, columns=labels, index=labels)
    print(df)

    df=df.multiply(1.4)

    print("\nGENERATED ANTI RESULTS\n"+str(df))

    df.to_csv("resultA.csv")

    return df

def getPreferencia():
    print("Generating preferencias...")
    for i in range(len(arr)):
        listT=[]
        for j in range(len(arr)):
            if arr[i][1] == "Mujer":
                if arr[i][0] == "Mujer":
                    if arr[j][0] == "Mujer" and (arr[j][1] == "Mujer" or arr[j][1] == "Ambos") :
                        listT.append(j)

                elif arr[i][0] == "Hombre":
                    if arr[j][0] == "Mujer" and (arr[j][1] == "Hombre" or arr[j][1] == "Ambos"):
                        listT.append(j)
                elif arr[i][0] == "Otro":
                    if arr[j][0] == "Mujer":
                        listT.append(j)
                elif arr[i][0] == "Prefiero no decirlo":
                    if arr[j][0] == "Mujer":
                        listT.append(j)


            elif arr[i][1] == "Hombre":
                if arr[i][0] == "Hombre":
                    if arr[j][0] == "Hombre" and (arr[j][1] == "Hombre" or arr[j][1] == "Ambos") :
                        listT.append(j)
                elif arr[i][0] == "Mujer":
                    if arr[j][0] == "Hombre" and (arr[j][1] == "Mujer" or arr[j][1] == "Ambos"):
                        listT.append(j)
                elif arr[i][0] == "Otro":
                    if arr[j][0] == "Hombre":
                        listT.append(j)
                elif arr[i][0] == "Prefiero no decirlo":
                    if arr[j][0] == "Hombre":
                        listT.append(j)

            elif arr[i][1] == "Ambos" and arr[i][0] == "Hombre":
                if arr[j][0] == "Mujer" or arr[j][1] == "Ambos" or (arr[j][1]=='Hombre'):
                    listT.append(j)

            elif arr[i][1] == "Ambos" and arr[i][0] == "Mujer":
                if arr[j][0] == "Hombre" or arr[j][1] == "Ambos" or (arr[j][1]=='Mujer'):
                    listT.append(j)
            elif arr[i][1] == "Ambos" and (arr[i][0] == "Prefiero no decirlo" or arr[i][0] == "No binario" or arr[i][0] == "Otro"):
                    listT.append(j)

        #print(listT)
        preferencias.append(listT)
    p=pd.DataFrame(preferencias)
    p.to_csv("prefrencias.csv")
    print("\nGENERATED PREFERENCIAS\n"+str(p))


def busquedaTop(nombre,cantidad):
    temporal=nombre#[nombre]
    #print(Head)
    iTemp= Head.index(temporal)

    #print(arrR[iTemp])
    listaTemp=[]
    #listaTemp.append(nombre)
    t = np.argsort(arrayResults[iTemp].astype(str))[::-1][:cantidad]
    for i in t:
        # if arrayResults[iTemp][i]< 0.6:
        #     al=arrayResults[iTemp][i]*1.5
        # elif 0.6 < arrayResults[iTemp][i] < 0.7:
        #     al = arrayResults[iTemp][i] * 1.4
        # elif 0.7 < arrayResults[iTemp][i] < 0.8:
        #     al = arrayResults[iTemp][i] * 1.2
        # elif 0.8< arrayResults[iTemp][i] < 0.9:
        #     al = arrayResults[iTemp][i] * 1.1
        # elif 0.9 < arrayResults[iTemp][i]<1:
        #     al = arrayResults[iTemp][i] * 1.01
        # elif arrayResults[iTemp][i] >1:
        #     al = arrayResults[iTemp][i]

        try:
            listaTemp.append(str(Head[i]+HeadIG[i])+str(arrayResults[iTemp][i]))
        except:
            listaTemp.append(str(Head[i-1]+HeadIG[i-1])+str(arrayResults[iTemp][i-1]))

    matches.append(listaTemp)
    print(listaTemp)

def busquedaAnti(nombre,cantidad):
    temporal = nombre
    iTemp = Head.index(temporal)
    listaTemp = []

    t = np.argsort(arrayAnti[iTemp].astype(str))[::1][:cantidad]
    for i in t:
        try:
            listaTemp.append(str(Head[i]+HeadIG[i])+str(arrayResults[iTemp][i]))
        except:
            listaTemp.append(str(Head[i-1]+HeadIG[i-1])+str(arrayResults[iTemp][i-1]))

    anti.append(listaTemp)

    print(t,str(nombre))



if __name__ == '__main__':

    vectors = pd.read_csv("Dragon4.csv", delimiter=',')
    labels = pd.read_csv("HeadersMail.csv", delimiter=',')
    labelsIG = pd.read_csv("HeadersIG.csv", delimiter=',')
    HeadIG= labelsIG.values.tolist()
    Head=labels.values.tolist()

    print(labelsIG)
    print(vectors)
    print(labels)

    nom=[]
    for i in range(len(Head)):
        nom.append(str(Head[i])+str(HeadIG[i]))

    nom= pd.DataFrame(nom)
    arr = vectors.to_numpy()
    getPreferencia()
    res=generateResults()
    an = generateAnti()

    res = pd.read_csv("result.csv", delimiter=',')
    an= pd.read_csv("resultA.csv", delimiter=',')
    arrayResults= res.to_numpy()
    arrayAnti= an.to_numpy()

    #busquedaTop()

    for nombre in range(0,len(labels)):
        busquedaTop(Head[nombre],10)
        busquedaAnti(Head[nombre],5)

    matches=pd.DataFrame(matches,index=nom)
    antim= pd.DataFrame(anti,index=nom)
    antim.to_excel("antimatches09-02.xlsx")
    matches.to_excel("matches09-02.xlsx")
