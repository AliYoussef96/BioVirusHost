# BioVirusHost
A simple Python interface to query the information from Virus-Host DB

[![Build Status](https://travis-ci.com/AliYoussef96/BioVirusHost.svg?token=anJWscmB7RsxdzyhVx5B&branch=master)](https://travis-ci.com/AliYoussef96/BioVirusHost)
[![Documentation Status](https://readthedocs.org/projects/biovirushost/badge/?version=latest)](https://biovirushost.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/BioVirusHost.svg)](https://badge.fury.io/py/BioVirusHost)
[![DOI](https://zenodo.org/badge/201461516.svg)](https://zenodo.org/badge/latestdoi/201461516)


# Statement of need

BioVirusHost is a simple Python interface to query information from Virus-Host database. Virus-Host DB provides a collection of viruses and their host information, and it is the biggest database present [see](https://www.genome.jp/virushostdb/stat.html ).
The need to access the information from the Virus-Host DB in a simple pythonic way is very useful for collecting data about viruses and hosts. BioVirusHost is a package that allows the connection to the Virus-Host DB API and parses information from it.
Virus-Host DB does not provide API documentation or examples, hence BioVirusHost was developed to connect, get, and parse information fast and easy.

# Dependencies

1- Biopython

2- pandas

# Installation Instructions

**Using pip**

```python
pip install BioVirusHost
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

```python
from BioVirusHost import BioVirusHost

for i_result in BioVirusHost.v_search(["Caprine parainfluenza virus 3","Human parainfluenza virus 1 strain Washington/1964","Human parainfluenza virus 4a"]):
    print (i_result)
```

**output**

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Caprine parainfluenza virus 3 [TAX:1529392]|Viruses; Riboviria; Negarnaviricota; Haploviricotina; Monjiviricetes; Mononegavirales; Paramyxoviridae; Orthoparamyxovirinae; Respirovirus; Bovine respirovirus 3|Capra hircus [TAX:9925]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Laurasiatheria; Ruminantia; Pecora; Bovidae; Caprinae; Capra

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Human parainfluenza virus 1 strain Washington/1964 [TAX:188538]|Viruses; Riboviria; Negarnaviricota; Haploviricotina; Monjiviricetes; Mononegavirales; Paramyxoviridae; Orthoparamyxovirinae; Respirovirus; Human respirovirus 1|Homo sapiens [TAX:9606]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Euarchontoglires; Primates; Haplorrhini; Simiiformes; Catarrhini; Hominoidea; Hominidae; Homininae; Homo

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Human parainfluenza virus 4a [TAX:11224]|Viruses; Riboviria; Negarnaviricota; Haploviricotina; Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirus; Human rubulavirus 4|Homo sapiens [TAX:9606]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Euarchontoglires; Primates; Haplorrhini; Simiiformes; Catarrhini; Hominoidea; Hominidae; Homininae; Homo


#### Example 2

Search for virus hosts by host scientific name.

```python
from BioVirusHost import BioVirusHost

for i_result in BioVirusHost.h_search(["Abutilon","Abelmoschus manihot"]):
    print (i_result)
```

**output**

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Abutilon mosaic virus [TAX:10815]|Viruses; Geminiviridae; Begomovirus|Abutilon [TAX:3630]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae
Abutilon mosaic Bolivia virus [TAX:932071]|Viruses; Geminiviridae; Begomovirus|Abutilon [TAX:3630]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae
Abutilon golden mosaic Yucatan virus [TAX:1312723]|Viruses; Geminiviridae; Begomovirus; Abutilon golden mosaic virus|Abutilon permolle [TAX:1312722]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae; Abutilon
Abutilon Brazil virus [TAX:665102]|Viruses; Geminiviridae; Begomovirus|Abutilon [TAX:3630]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Ageratum conyzoides symptomless alphasatellite [TAX:1705092]|Viruses; Alphasatellitidae; Geminialphasatellitinae; unclassified Begomovirus-associated alphasatellites|Abelmoschus manihot subsp. tetraphyllus [TAX:1610811]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae; Abelmoschus; Abelmoschus manihot
Ageratum conyzoides symptomless alphasatellite [TAX:1705092]|Viruses; Alphasatellitidae; Geminialphasatellitinae; unclassified Begomovirus-associated alphasatellites|Abelmoschus manihot [TAX:183220]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae; Abelmoschus


#### Example 3

Search for virus hosts by virus TAX id.

```python
from BioVirusHost import BioVirusHost

for i_result in BioVirusHost.v_tax_search([443876,438782]):
    print (i_result)
```

**output**

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
African swine fever virus Benin 97/1 [TAX:443876]|Viruses; Asfarviridae; Asfivirus; African swine fever virus|Potamochoerus larvatus [TAX:273792]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Laurasiatheria; Suina; Suidae; Potamochoerus
African swine fever virus Benin 97/1 [TAX:443876]|Viruses; Asfarviridae; Asfivirus; African swine fever virus|Phacochoerus aethiopicus [TAX:85517]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Laurasiatheria; Suina; Suidae; Phacochoerus
African swine fever virus Benin 97/1 [TAX:443876]|Viruses; Asfarviridae; Asfivirus; African swine fever virus|Phacochoerus africanus [TAX:41426]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Laurasiatheria; Suina; Suidae; Phacochoerus
African swine fever virus Benin 97/1 [TAX:443876]|Viruses; Asfarviridae; Asfivirus; African swine fever virus|Sus scrofa [TAX:9823]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Laurasiatheria; Suina; Suidae; Sus
African swine fever virus Benin 97/1 [TAX:443876]|Viruses; Asfarviridae; Asfivirus; African swine fever virus|Ornithodoros [TAX:6937]|Eukaryota; Metazoa; Arthropoda; Chelicerata; Arachnida; Acari; Parasitiformes; Ixodida; Ixodoidea; Argasidae

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Abaca bunchy top virus [TAX:438782]|Viruses; Nanoviridae; Babuvirus|Musa acuminata AAA Group [TAX:214697]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Liliopsida; Petrosaviidae; Zingiberales; Musaceae; Musa
Abaca bunchy top virus [TAX:438782]|Viruses; Nanoviridae; Babuvirus|Musa sp. [TAX:46838]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Liliopsida; Petrosaviidae; Zingiberales; Musaceae; Musa


#### Example 4

Search for virus hosts by host tax id.

```python
from BioVirusHost import BioVirusHost

for i_result in BioVirusHost.h_tax_search([183220,3630]):
    print (i_result)
```

**output**

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Ageratum conyzoides symptomless alphasatellite [TAX:1705092]|Viruses; Alphasatellitidae; Geminialphasatellitinae; unclassified Begomovirus-associated alphasatellites|Abelmoschus manihot subsp. tetraphyllus [TAX:1610811]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae; Abelmoschus; Abelmoschus manihot
Ageratum conyzoides symptomless alphasatellite [TAX:1705092]|Viruses; Alphasatellitidae; Geminialphasatellitinae; unclassified Begomovirus-associated alphasatellites|Abelmoschus manihot [TAX:183220]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae; Abelmoschus

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Abutilon mosaic virus [TAX:10815]|Viruses; Geminiviridae; Begomovirus|Abutilon [TAX:3630]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae
Abutilon mosaic Bolivia virus [TAX:932071]|Viruses; Geminiviridae; Begomovirus|Abutilon [TAX:3630]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae
Abutilon golden mosaic Yucatan virus [TAX:1312723]|Viruses; Geminiviridae; Begomovirus; Abutilon golden mosaic virus|Abutilon permolle [TAX:1312722]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae; Abutilon
Abutilon Brazil virus [TAX:665102]|Viruses; Geminiviridae; Begomovirus|Abutilon [TAX:3630]|Eukaryota; Viridiplantae; Streptophyta; Streptophytina; Malvales; Malvaceae; Malvoideae


#### Example 5

Advanced search for virus hosts using virus lineage and a specific host

```python
from BioVirusHost import BioVirusHost

for i_result in BioVirusHost.comp_query("phasianinae","adenoviridae"):
    print (i_result)
```

**output**

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Avirulent turkey hemorrhagic enteritis virus [TAX:318490]|Viruses; Adenoviridae; Siadenovirus; Turkey siadenovirus A|Phasianinae [TAX:9072]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Aves; Neognathae; Galloanserae; Galliformes; Phasianidae


#### Example 6

Get more information about the virus or its host.

This will return:

1- A data frame contains information about a virus (only) as genome type if host_info = False (default). 

```python
from BioVirusHost import BioVirusHost

for i_result in BioVirusHost.more_info("318490", "A.N.Other@example.com",False):
    print (i_result)
```

2- A generator object for Data frame(s) contains infromation about hosts (only), if host_info = T.

```python
from BioVirusHost import BioVirusHost

for i_result in BioVirusHost.more_info("318490", "A.N.Other@example.com",True):
    print (i_result)
```
**output**

0|1
|-------------------|-------------|
Scientific Name|Phasianinae [TAX:9072]
Lineage|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Aves; Neognathae; Galloanserae; Galliformes; Phasianidae
Evidence|Literature
Reference|PMID: 19386786
Authors|"Beach NM| Duncan RB| Larsen CT| Meng XJ| Sriranganathan N| Pierson FW"
Title|Comparison of 12 turkey hemorrhagic enteritis virus isolates allows prediction of genetic factors affecting virulence.
Journal|J Gen Virol. 2009 Aug;90(Pt 8):1978-85.


0|1
|-------------------|----------
Scientific Name|Meleagris gallopavo [TAX:9103]
Lineage|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Aves; Neognathae; Galloanserae; Galliformes; Phasianidae; Meleagridinae; Meleagris
Evidence|Literature
Reference|PMID: 19386786
Authors|"Beach NM| Duncan RB| Larsen CT| Meng XJ| Sriranganathan N| Pierson FW"
Title|Comparison of 12 turkey hemorrhagic enteritis virus isolates allows prediction of genetic factors affecting virulence.
Journal|J Gen Virol. 2009 Aug;90(Pt 8):1978-85.
DBLINKS|KEGG GENOME: T01523

# Citation

Ali Mostafa Anwar. (2019, August 14). BioVirusHost: A simple Python interface to query the information from Virus-Host DB (Version v1.0.1). Zenodo. http://doi.org/10.5281/zenodo.3368326
