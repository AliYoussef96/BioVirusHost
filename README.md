# BioVirusHost
A simple Python interface to query the information from Virus-Host DB

[![Build Status](https://travis-ci.com/AliYoussef96/BioVirusHost.svg?token=anJWscmB7RsxdzyhVx5B&branch=master)](https://travis-ci.com/AliYoussef96/BioVirusHost)

# Statement of need

A simple Python interface to query information from Virus-Host database. Virus-Host DB provides a collection of viruses and their host information, and it is the biggest database present [see](https://www.genome.jp/virushostdb/stat.html ).
The need to access the information from the Virus-Host DB in a simple pythonic way is very useful for collecting data about viruses and hosts. BioVirusHost is a package that allows the connection to the Virus-Host DB API and parses information from it.
Virus-Host DB does not provide API documentation or examples, hence BioVirusHost was developed to connect, get, and parse information fast and easy.

# Dependencies

1- Biopython

2- pandas

# Installation Instructions

**Using pip**

```
pip install 
```

**Note:** Python >=3.7 is required.

# Contribution Guidelines


For bugs and suggestions, the most effective way is by raising an issue on the github issue tracker. 
Github allows you to classify your issues so that we know if it is a bug report, feature request or feedback to the authors.

If you wish to contribute some changes to the code then you should submit a [pull request](https://github.com/AliYoussef96/BioVirusHost/pulls)
How to create a Pull Request? [documentation on pull requests](https://help.github.com/en/articles/about-pull-requests)

# Usage

#### Example 1

Search for virus hosts by virus scientific name.

```
for i_result in v_search(["Caprine parainfluenza virus 3","Human parainfluenza virus 1 strain Washington/1964","Human parainfluenza virus 4a"]):
    print (i_result)
```

This will return generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

#### Example 2

Search for virus hosts by host scientific name.

```
for i_result in h_search(["Abutilon","Abelmoschus manihot"]):
    print (i_result)
```

This will return a generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

#### Example 3

Search for virus hosts by virus TAX id.

```
for i_result in v_tax_search([443876,438782]):
    print (i_result)
```

This will return generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

#### Example 4

Search for virus hosts by host tax id.

```
for i_result in h_tax_search([183220,3630]):
    print (i_result)
```

This will return a generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

#### Example 5

Advanced search for virus hosts using virus lineage and a specific host

```
for i_result in comp_query("phasianinae","adenoviridae"):
    print (i_result)
```

This will return a generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

#### Example 6

Get more information about the virus or its host.

This will return:

1- A data frame contains information about a virus (only) as genome type if host_info = False (default). 

```
print (more_info("318490", "A.N.Other@example.com"))
```

2- A generator object for Data frame(s) contains infromation about hosts (only), if host_info = T.

```
for i_result in more_info("318490", "A.N.Other@example.com",True):
    print (i_result)
```
