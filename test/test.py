import pytest
from BioVirusHost import BioVirusHost


def test_test():
        with pytest.raises(TypeError):
                test = [ i for i in BioVirusHost.v_search("virus") ]
        with pytest.raises(TypeError):
                test = [ i for i in BioVirusHost.h_search("host") ]
        with pytest.raises(TypeError):
                test = [ i for i in BioVirusHost.v_tax_search("virus") ]
        with pytest.raises(TypeError):
                test = [ i for i in BioVirusHost.h_tax_search("host") ]
        with pytest.raises(TypeError):
                test = [ i for i in BioVirusHost.comp_query(["host"],["virus"]) ]
        with pytest.raises(TypeError):
                test = [ i for i in BioVirusHost.more_info(["virus"],["test@gmail.com"]) ]

