# A bunch of functions that we'll need to deal with making an icartt header...
# no organization for now!


# Import the yaml
import yaml
def loadyaml(fin):
    """
    Loads a yaml file into the assigned variable:
    hdr = loadyaml(fin)
    
    hdr.keys() gives the dictionary
    """
    f = open(fin, 'r')
    hdr = yaml.load(f)
    return hdr