'''
Write a function to flatten a deeply nested dictionary into a single-level dictionary.
'''

def flatten_dict(d, parent_key = '', sep = '_'):
  res = []
  for k, v in d.items():
    new_key = f"{parent_key}{sep}{k}" if parent_key else k
    if isinstance(v, dict):
      res.extend(flatten_dict(v, new_key, '_').items())
    else:
      res.append((new_key,v))
  return dict(res)
      
                   
