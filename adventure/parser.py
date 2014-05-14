from constants import WIDTH

def parse(line):
  return line.split('>')[1:]

def enshorten(line):
  out=''
  count=0
  for i in line.split():
    if (len(out) + len(i+' ')) / WIDTH > count:
      count+=1
      out+='\n  '
    out += i+' '
  out+='\n'
  return out
