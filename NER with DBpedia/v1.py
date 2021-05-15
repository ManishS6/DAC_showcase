from bs4 import BeautifulSoup
import requests
import json
import time
import xml
import parser
############# links
query_search ="https://lookup.dbpedia.org/api/search.asmx/KeywordSearch?MaxHits=1&QueryString="
# only one result
page_url='http://dbpedia.org/page/'

## for json ##
page_data_url ='http://dbpedia.org/data/'  #get json
page_resource_url="http://dbpedia.org/resource/"
page_ontology_url='http://dbpedia.org/ontology/' 
page_property_url='http://dbpedia.org/property/'


def get_page_label(search):
    results = requests.get(query_search+search).text
    label = BeautifulSoup(results,'xml').find('Label').text
    return label

def get_link(page_url_data,label):
    return page_url_data+'_'.join(label.split(' '))


def get_readable_value(page_link_in_value,value_link):
    if len(value_link)<len(page_link_in_value):
        return value_link
    return ' '.join(value_link[len(page_link_in_value):].split('_'))




def get_data(label): #redirect or direct data
    data=json.loads(requests.get(get_link(page_data_url,label)+'.json').text)
    new_label=label
    try:
        redirect_link=data[get_link(page_resource_url,label)]['http://dbpedia.org/ontology/wikiPageRedirects'][0]['value']
        new_data_link=get_link(page_data_url,get_readable_value(page_resource_url,redirect_link))
        data= json.loads(requests.get(new_data_link+'.json').text)
        new_label=get_readable_value(page_data_url,new_data_link)
        print('redirected : '+new_label)
    except:
        pass
    return (data,new_label)
    

def get_value(label,property_):
    results=[]
    
    data,label = get_data(label)
    try:
        dict_data = data[get_link(page_resource_url,label)][page_ontology_url+property_]
    except:
        try:
            dict_data = data[get_link(page_resource_url,label)][page_property_url+property_]
        except:
            dict_data ={}
            print('Ontology/Property Not found')
            pass
        
    for _ in dict_data:
        results.append(_['value'])
    return results


def search_(search,property__):
    label = get_page_label(search)
    print(label)
    value = get_value(label,property__)
    print(property__+': ')
    for _ in value:
        print(get_readable_value(page_resource_url,str(_)))

search_("gameloft","owner")