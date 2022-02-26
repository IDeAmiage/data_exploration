import requests
import pandas as pd 
import json
import csv
import os


def list_datasets_v2(year):
    """This function can list all the datasets available in opendatasoft API V2

    Args:
        year (int): choose the year you want the list

    Raises:
        SystemExit: Connexion error to the API

    Returns:
        list: list of datasets that we can reach
    """
    try:
        response= requests.get(str('https://data.opendatasoft.com/api/v2/catalog/exports/json?lang=fr&refine=modified:'+str(year)))
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    obj2 = response.json()
    liste = []
    for i in range(len(obj2)):
        liste.append(obj2[i]['dataset_id'])
    return liste

def get_dataset_v2(dataset_id:str, save=False, folder="data"):
    """This function can get the dataset you passed in and export this as a csv file or a pandas dataframe

    Args:
        dataset_id (str): name of the dataset you want to get
        save (bool, optional): if true save the df as a csv file. Defaults to False.
        folder (str, optional): path of your folder you want to save. Defaults to "data".

    Raises:
        SystemExit: Connexion error to the API

    Returns:
        pd.DataFrame: return the desire dataframe
    """
    try:
        response = requests.get(str('https://data.opendatasoft.com/api/v2/catalog/datasets/'+dataset_id+'/exports/csv'))
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    obj = response.content.decode('utf-8')
    if obj == []:
        print("dataset is empty")    
    else:
        cr = csv.reader(obj.splitlines(), delimiter=';')
        df = pd.DataFrame(cr)
        df.rename(columns=df.iloc[0], inplace=True)
        df = df.iloc[1: , :]    
        if save == True:
            if folder is not None:
                df.to_csv(os.path.join(folder,str(dataset_id+'.csv')), index=False)
                return True
            else: 
                print("folder is not defined")
    return df

def get_dataset_v1(number_of_lines=200, save=False, folder="data", dataset_id="covid19-france-livraison-vaccin-region"):
    """Function to get dataset from the first API of opendatasoft

    Args:
        number_of_lines (int, optional): choose number of lines to get. Defaults to 200.
        save (bool, optional): if true save the df as a csv file. Defaults to False.
        folder (str, optional): path of your folder you want to save. Defaults to "data".
        dataset_id (str, optional): name of the dataset you want to get. Defaults to "covid19-france-livraison-vaccin-region".

    Returns:
        pd.DataFrame: return the desire dataframe
    """
    response = requests.get("https://public.opendatasoft.com/api/records/1.0/search/?dataset="+dataset_id+"&q=&rows="+str(number_of_lines))
    obj = response.json()
    df = pd.DataFrame(obj['records'])
    df = pd.json_normalize(df.fields)
    if save == True:
        if folder is not None:
            df.to_csv(os.path.join(folder,str(dataset_id+'.csv')), index=False)
            return True
        else: 
            print("folder is not defined")
    return df


print(get_dataset_v1())


