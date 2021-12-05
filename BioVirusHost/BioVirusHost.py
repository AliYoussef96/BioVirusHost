import pandas as pd
from pandas import DataFrame
from Bio import Entrez
import urllib

# must install BeautifulSoup4 for pandas.read.html

main_url = "https://www.genome.jp/virushostdb/"

def v_search(v_query):
    """

    Search for virus hosts by virus scientific name

    Args:

        v_query (list): list of virus(es) scientific name

    Returns:

        A generator object for Data frame(s) contains ( virus (species) name, virus lineage, host name, and host lineage )

    Raises:
        TypeError if argument (v_quer) is not a list

    """
    #rais error when the arg. is not a list
    if type (v_query) != list:
        raise TypeError ("v_search takes list as an argument")

    for i_virus in v_query:
        i_virus = i_virus.strip()
        i_virus = i_virus.capitalize()
      
        # creat the url
        sub_url = main_url + "view/?"
        dict_url = {"virus_scientific_name" : i_virus}
        api_request =  urllib.parse.urlencode(dict_url)
        api_request = sub_url + api_request

        #get the table results
        tables = pd.read_html(api_request)

        tables = tables[1]

        #correct the order

        tables = tables.iloc[::-1]

        #rest the index
        tables.reset_index(inplace=True, drop=True)

                #get the total result to view all of them 
        total = tables[1][1].split(" ")
        total = total[1]

        #reload the url to view all the result

        if len( set(tables[0]) ) - 2 != int(total):
            api_request = api_request + "&per_page=" + str(total)
            tables = pd.read_html(api_request)
            
            #get the table results
            tables = tables[1]

            #correct the order
            tables = tables.iloc[::-1]

            #rest the index
            tables.reset_index(inplace=True, drop=True)
        else:
            pass

        #drop unnecessarily row
        tables.drop([1],inplace = True,axis = 0)
        tables.drop([4,5,6],inplace = True,axis = 1)

        #firt row as header
        tables.reset_index(inplace=True, drop=True)
        tables.rename(columns=tables.iloc[0],inplace=True)
        tables.drop([0],inplace = True,axis = 0)

        #rest the index again
        tables.reset_index(inplace=True, drop=True)

        if len(tables) == 0:
            yield (f"No result found for {i_virus}")
        else:
            yield tables

def h_search(h_query):
    """

    Search for virus hosts by host scientific name

    Args:

        v_query (list): list of host(s) scientific name

    Returns:

        A generator object for Data frame(s) contains ( virus (species) name, virus lineage, host name, and host lineage )

    Raises:

        TypeError if argument (h_query) is not a list

      
    """
    #rais error when the arg. is not a list
    if type (h_query) != list:
        raise TypeError ("h_search takes list as an argument")

    for i_host in h_query:
        i_host = i_host.strip()
        i_host = i_host.capitalize()
      
        # creat the url
        sub_url = main_url + "view/?"
        dict_url = {"host_scientific_name" : i_host}
        api_request =  urllib.parse.urlencode(dict_url)
        api_request = sub_url + api_request

        #get the table results
        tables = pd.read_html(api_request)

        tables = tables[1]

        #correct the order
        tables = tables.iloc[::-1]

        #rest the index
        tables.reset_index(inplace=True, drop=True)

        #get the total result to view all of them 
        total = tables[1][1].split(" ")
        total = total[1]

        #reload the url to view all the result

        if len( set(tables[0]) ) - 2 != int(total):
            api_request = api_request + "&per_page=" + str(total)
            tables = pd.read_html(api_request)

            #get the table results
            tables = tables[1]

            #correct the order
            tables = tables.iloc[::-1]

            #rest the index
            tables.reset_index(inplace=True, drop=True)
        else:
            pass


        #drop unnecessarily row
        tables.drop([1],inplace = True,axis = 0)
        
        tables.drop([4,5,6],inplace = True,axis = 1)

        #firt row as header
        tables.reset_index(inplace=True, drop=True)
        tables.rename(columns=tables.iloc[0],inplace=True)
        tables.drop([0],inplace = True,axis = 0)


        #drop rows with no ( host name ) in host lineage 
        #get the fist name of the host name if it two parts
        host_first_name = i_host.split(" ")
        host_first_name = host_first_name[0]
        tables = tables[ tables["Host name"].str.contains(i_host)  | tables["Host lineage"].str.contains(i_host) |  tables["Host lineage"].str.contains(host_first_name) ] 

        #rest the index again
        tables.reset_index(inplace=True, drop=True)

        if len(tables) == 0:
            yield (f"No result found for {i_host}")
        else:
            yield tables


 
def v_tax_search(tax_query):
    """

    Search for virus hosts by virus TAX id

    Args:

        tax_query (list): list of virus(s) TAX id

    Returns:

        A generator object for Data frame(s) contains ( virus (species) name, virus lineage, host name, and host lineage )

    Raises:

        TypeError if argument (tax_query) is not a list

      
    """
    #rais error when the arg. is not a list
    if type (tax_query) != list:
        raise TypeError ("h_search takes list as an argument")

    all_virus_name = []
    for tax_id in tax_query:
        tax_id = str(tax_id)
        tax_id = tax_id.strip()
      
        # creat the url
        api_request = main_url + tax_id
       
        #get the table results
        tables = pd.read_html(api_request)
        tables = tables[2]

        #get the virus name
        all_virus_name.append(tables[0][0])

    return v_search(all_virus_name)


def h_tax_search(tax_query):
    """

    Search for virus hosts by host tax id

    Args:

        tax_query (list): list of host(s) tax id

    Returns:

        A generator object for Data frame(s) contains ( virus (species) name, virus lineage, host name, and host lineage )

    Raises:

        TypeError if argument (tax_query) is not a list

    """
    #rais error when the arg. is not a list
    if type (tax_query) != list:
        raise TypeError ("h_search takes list as an argument")

    all_host_name = []
    for tax_id in tax_query:
        tax_id = str(tax_id)
        tax_id = tax_id.strip()
      
        # creat the url
        api_request = main_url + tax_id
       
        #get the table results
        tables = pd.read_html(api_request)
        tables = tables[2]

        #get the virus name
        all_host_name.append(tables[0][0])

    return h_search(all_host_name)


def comp_query(host, virus_lineage):
    """

    Advanced search for virus hosts using virus lineage and a specific host

    Args:

        host (str): target host name or tax id

        virus_lineage (str): virus lineage

    Returns:

        A generator object for Data frame(s) contains ( virus (species) name, virus lineage, host name, and host lineage )

    Raises:

        TypeError if argument (host) is not a str

        TypeError if argument (virus_lineage) is not a str
      
    """
    #rais error when the arg. is not a list
    if type (host) != str or type(virus_lineage) != str:
        raise TypeError ("comp_query takes arguments as str")

    # creat the url
    host = host.strip()
    host = host.capitalize()
    virus_lineage = virus_lineage.strip()
    virus_lineage = virus_lineage.capitalize()
    

    sub_url = main_url + "view/?"

    dict_url = {"host_scientific_name" : host, "virus_lineage" : virus_lineage }
    api_request =  urllib.parse.urlencode(dict_url)
    api_request = sub_url + api_request

    #get the table results
    tables = pd.read_html(api_request)

    tables = tables[1]

    #correct the order
    tables = tables.iloc[::-1]

    #rest the index
    tables.reset_index(inplace=True, drop=True)

    #get the total result to view all of them 
    total = tables[1][1].split(" ")
    total = total[1]
    
     #reload the url to view all the result

    if len( set(tables[0]) ) - 2 != int(total):
        api_request = api_request + "&per_page=" + str(total)
        tables = pd.read_html(api_request)

        #get the table results
        tables = tables[1]

        #correct the order
        tables = tables.iloc[::-1]

        #rest the index
        tables.reset_index(inplace=True, drop=True)
    else:
        pass


    #drop unnecessarily row
    tables.drop([1],inplace = True,axis = 0)
    tables.drop([4,5,6],inplace = True,axis = 1)

    #firt row as header
    tables.reset_index(inplace=True, drop=True)
    tables.rename(columns=tables.iloc[0],inplace=True)
    tables.drop([0],inplace = True,axis = 0)


    #drop rows with no ( host name ) in host lineage 
    #get the fist name of the host name if it two parts
    host_first_name = host.split(" ")
    host_first_name = host_first_name[0]
    tables = tables[ tables["Host name"].str.contains(host)  | tables["Host lineage"].str.contains(host) |  tables["Host lineage"].str.contains(host_first_name) ] 
    
    #rest the index again
    tables.reset_index(inplace=True, drop=True)

    if len(tables) == 0:
        yield (f"No result found for {host} and {virus_lineage}")
    else:
        yield tables

def more_info(v_query, email, host_info= False):

    """
    Get more information about the virus or its host

    Args:

        v_query (str or int): target virus name or tax id 

        email (str): your email address, required by the NCBI server

        host_info (bool): default = False

    Returns:

        A dataframe contains information about a virus (only) as genome type, if host_info = False (default) 

        A generator object for Data frame(s) contains infromation about hosts (only), if host_info = True 

    Raises:

        TypeError if argument (v_query) is not a str

        TypeError if argument (email) is not a str
      
    """
    if type(v_query) != str:
        raise TypeError ("more_info takes v_query argument as str")

    if type(email) != str:
        raise TypeError ("more_info takes email argument as str")

    #see of it tax id or name
    try:
        v_query = int(v_query) #if true so it is tax id
        tax_id = str (v_query)
    except:
        v_query = v_query.strip()
        v_query = v_query.capitalize()
        #get the tax id from the virus name
        Entrez.email = email # Always tell NCBI who you are
        handle = Entrez.esearch(db="taxonomy",term = v_query )
        record = Entrez.read(handle)
        name = record["TranslationStack"]
        name = name[0]["Term"]
        name = name[:name.find("[All Names]")] 
        if name.strip() == v_query:
            tax_id = str ( (record["IdList"][0]) )

    #creat the url 
    api_request = main_url + str(tax_id)

    tables = pd.read_html(api_request)


    if host_info == False:
       yield tables[3] #the virus dataframe

    elif host_info == True:
        for i in range(len(tables))[4:]:
            yield tables[i]
        

