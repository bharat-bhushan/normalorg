#! python
#! coding: utf-8

import os
import yaml

_thisLoc = os.path.dirname(__file__)
_entityTypes = yaml.load(open(os.path.join(_thisLoc, "../resources", "entityTypes.yaml"), "r"))
_puncToCollapse = yaml.load(open(os.path.join(_thisLoc, "../resources", "puncToCollapse.yaml"), "r"))
_puncToRemove = yaml.load(open(os.path.join(_thisLoc, "../resources", "puncToRemove.yaml"), "r"))


def normalize(org):
    """ primary method used to normalize an org name
        accepts: organization name
        returns: normalized org name

        assumes that the user wants shortest strings possible, which is helpful when
        computing edit distance between two strings. therefore incorporated is shortened
        to inc rather than inc being expanded to incorporated.
    """
    if org is None: return None
    for x in _puncToCollapse: org = org.replace(x, '')
    for x in _puncToRemove: org = org.replace(x, ' ')
    org = org.lower().strip()
    org = " ".join([_entityTypes[x] if x in _entityTypes else x for x in org.split(" ")])  # replace synonyms
    return " ".join(org.split())  # removes any multiples of white space in middle of strings


def main():
    """ temporary main for testing only. will be replaced with a test class
    """

    print normalize("macy's & company")
    print normalize("williams sanoma s.b.a.")
    print normalize("ck life sciences int'l")
    print "todo: multiple word syn replacement"
    print normalize("flughafen hamburg gesellschaft mit beschrankter haftung")

if __name__ == '__main__':
    main()
