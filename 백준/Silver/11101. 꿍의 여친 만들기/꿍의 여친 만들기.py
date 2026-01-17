I=input
exec("d=dict(e.split(':')for e in I().split(','));print(min(max(int(d[i])for i in e.split('&'))for e in I().split('|')));"*int(input()))