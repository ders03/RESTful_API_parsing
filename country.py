import json 
import urllib.request 
import urllib.parse 

def make_country(name): 
    url = "https://restcountries.eu/rest/v2/name/" + name + "?fullText=true" 
    response = urllib.request.urlopen(url)
    raw = response.read()  
    data = json.loads(raw) 
    #data returns [{dict}], easist to remove dict from ls for flow in other functions
    return(data[0])

def get_name(country): 
    return country["name"] 
    
def get_longitude(country): 
    for obj in country["latlng"]: 
        if obj == None: 
            return(None) 
        else:
            return(country["latlng"][1])  

def get_latitude(country): 
    for obj in country["latlng"]: 
        if obj == None: 
            return(None)
        else:
            return(country["latlng"][0]) 
            
def currency_codes(country): 
    ls = []
    for obj in country["currencies"]: 
        #append obj AT key=code to go through list of dicts
        ls.append(obj["code"]) 
    return(ls)  
    
def neighbors(country): 
    sub_region = country["subregion"] 
    #some regions have spaces that break the url
    formated = sub_region.replace(" ", "%20")
    #points to database by subregion
    url = "https://restcountries.eu/rest/v2/subregion/" + formated  
    response = urllib.request.urlopen(url) 
    raw = response.read() 
    data = json.loads(raw) 
    #data contains the entire subregion, need to remove our host country
    for dict in data: 
        if dict["name"] == get_name(country):
            data.remove(dict)
    return(data) 

def main(): 
    make_country(name)
    get_name(country) 
    get_longitude(country)
    get_latitude(country)  
    currency_codes(country) 
    neighbors(country)
    
    
    if __name__ == "__main__": 
        main()

