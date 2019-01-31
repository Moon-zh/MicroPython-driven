def _init():
	global a
	a={}
	
def set_value(name, value):
    a[name] = value
	
def get_value(name, defValue=None):
    try:
        return a[name]
    except KeyError:
        return defValue