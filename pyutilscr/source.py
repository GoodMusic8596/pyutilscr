import inspect



def method_source(method):
    raw_code=inspect.getsourcelines(method)
    return "".join(raw_code[0])

def file_source(file):
  return inspect.getsourcefile(file)