i=input
for _ in [0]*int(i()):
  a=i().replace(":","1=").replace(",",";");x=1e9
  for j in i().split("|"):exec(f'{a};global x;x=min(x,max(0,int({j.replace("&","1),int(")}1)))')
  print(x)