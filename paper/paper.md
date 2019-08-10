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

## Virus-Host DB

Virus-Host DB is a database providing data for the virus and its cellular hosts' relationships. It includes viruses with only whole genomes collected in NCBI/RefSeq and GenBank whose accession numbers are recorded in EBI Genomes. This kind of database help in environmental genomics studies where analysis of viruses community and the interaction networks between its hosts' are required.

## BioVirusHost

BioVirusHost is a simple Python interface to query information from Virus-Host database. Virus-Host DB provides a collection of viruses and their host information, and it is the biggest database present. The need to access the information from the Virus-Host DB in a simple pythonic way is very useful for collecting data about viruses and hosts. BioVirusHost is a package that allows the connection to the Virus-Host DB API and parses information from it. Since Virus-Host DB does not provide API documentation, BioVirusHost was developed to connect, get, and parse information fast and easy.
