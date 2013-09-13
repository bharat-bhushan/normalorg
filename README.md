normalorg
=========

*Organization Entity Name Normalizing Library* 

This is a work in progress, but somewhat usable for the time being. Its goal is to normalize entity names (specifically companies, organizations, etc.) to assist in fuzzy name matching. After normalizing all names in a data set, computing a levenstein edit distance or other fuzzy matching technique should yeild markedly improved results.

To get started, simply:

    from normalorg import normalize
    
    normalize(u"Organization Name")

Thats it!