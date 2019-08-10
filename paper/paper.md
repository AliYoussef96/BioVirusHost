---
title: 'BioVirusHost: A simple Python interface to query the information from Virus-Host DB'
tags:
  - Virus-Host DB
  - Virus
  - python
  - virus-host interactions
  - database api
  - taxonomy
authors:
 - name: Ali Mostafa Anwar
   orcid: 0000-0002-5201-387X
   affiliation: "1"
affiliations:
 - name: Department of Genetics, Faculty of Agriculture, Cairo University, 12613, Cairo, Egypt
   index: 1
date: August 10, 2019
bibliography: paper.bib
---

# Summery

### Virus-Host DB

Virus-Host DB is a database providing data for the virus and its cellular hosts' relationships. It includes viruses with only whole genomes collected in NCBI/RefSeq and GenBank whose accession numbers are recorded in EBI Genomes. This kind of database help in environmental genomics studies where analysis of viruses community and the interaction networks between its hosts' are required.

### BioVirusHost

BioVirusHost is a simple Python interface to query information from Virus-Host database. Virus-Host DB provides a collection of viruses and their host information, and it is the biggest database present. The need to access the information from the Virus-Host DB in a simple pythonic way is very useful for collecting data about viruses and hosts. BioVirusHost is a package that allows the connection to the Virus-Host DB API and parses information from it. Since Virus-Host DB does not provide API documentation, BioVirusHost was developed to connect, get, and parse information fast and easy.

# Implementation

BioVirusHost was developed using Python 3.7, and it is available to be installed using pip:

```python
pip install

```

BioVirusHost in its present version provides six functions each request different query from the Virus-Host DB, the final output of this function is a generator object. The generator object yield to data frames contains the information retrieved from the Virus-Host DB.

# Usage

### Example

Search for virus hosts by virus scientific name.

```python
from BioVirusHost import BioVirusHost

for i_result in BioVirusHost.v_search(["Caprine parainfluenza virus 3","Human parainfluenza virus 1 strain Washington/1964","Human parainfluenza virus 4a"]):
    print (i_result)
```

### output

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Caprine parainfluenza virus 3 [TAX:1529392]|Viruses; Riboviria; Negarnaviricota; Haploviricotina; Monjiviricetes; Mononegavirales; Paramyxoviridae; Orthoparamyxovirinae; Respirovirus; Bovine respirovirus 3|Capra hircus [TAX:9925]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Laurasiatheria; Ruminantia; Pecora; Bovidae; Caprinae; Capra

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Human parainfluenza virus 1 strain Washington/1964 [TAX:188538]|Viruses; Riboviria; Negarnaviricota; Haploviricotina; Monjiviricetes; Mononegavirales; Paramyxoviridae; Orthoparamyxovirinae; Respirovirus; Human respirovirus 1|Homo sapiens [TAX:9606]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Euarchontoglires; Primates; Haplorrhini; Simiiformes; Catarrhini; Hominoidea; Hominidae; Homininae; Homo

Virus (species) name|Virus lineage|Host name|Host lineage
|-------------------|-------------|---------|------------|
Human parainfluenza virus 4a [TAX:11224]|Viruses; Riboviria; Negarnaviricota; Haploviricotina; Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirus; Human rubulavirus 4|Homo sapiens [TAX:9606]|Eukaryota; Metazoa; Chordata; Craniata; Sarcopterygii; Mammalia; Euarchontoglires; Primates; Haplorrhini; Simiiformes; Catarrhini; Hominoidea; Hominidae; Homininae; Homo
