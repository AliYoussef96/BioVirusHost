Usage
=====

Example 1
^^^^^^^^^^

Search for virus hosts by virus scientific name.

        for i_result in BioVirusHost.v_search(["Caprine parainfluenza virus 3","Human parainfluenza virus 1 strain Washington/1964","Human parainfluenza virus 4a"]):
            print (i_result)
		

This will return generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

Example 2
^^^^^^^^^^

Search for virus hosts by host scientific name.

        for i_result in BioVirusHost.h_search(["Abutilon","Abelmoschus manihot"]):
            print (i_result)

This will return a generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

Example 3
^^^^^^^^^^

Search for virus hosts by virus TAX id.

        for i_result in BioVirusHost.v_tax_search([443876,438782]):
            print (i_result)

This will return generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

Example 4
^^^^^^^^^^

Search for virus hosts by host tax id.

        for i_result in BioVirusHost.h_tax_search([183220,3630]):
            print (i_result)

This will return a generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

Example 5
^^^^^^^^^^

Advanced search for virus hosts using virus lineage and a specific host.

        for i_result in BioVirusHost.comp_query("phasianinae","adenoviridae"):
            print (i_result)

This will return a generator object for Data frame(s) contains ( virus (species) name, virus lineage, hostname, and host lineage ).

Example 6
^^^^^^^^^^

Get more information about the virus or its host.

This will return:

1- A data frame contains information about a virus (only) as genome type if host_info = False (default). 

        print (BioVirusHost.more_info("318490", "A.N.Other@example.com"))

2- A generator object for Data frame(s) contains infromation about hosts (only), if host_info = T.


        for i_result in BioVirusHost.more_info("318490", "A.N.Other@example.com",True):
            print (i_result)
      




