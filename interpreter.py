import sys,random
s=sys.stdin.read()
i=input('Input: ')
if i.isdigit():
  acc=int(i)
else:
  acc=0
EOF='EOF'
direction='right'
X=1
Y=1
n=0
lines=s.split("\n")
wall=[[EOF]*len(lines[0])]
box=wall+[[EOF]+[*x]+[EOF]for x in lines]+wall
times=1
execute=True
codepage='iodcswh<>^v!~(){}'
directions={'<':'left','>':'right','^':'up','v':'down'}
token=box[X][Y]
commands={
'i':"acc+=1",
'o':"print(acc,end='')",
'd':"acc-=1",
'c':"print(chr(acc),end='')",
's':"acc**=2",
'w':"print('Hello, World!',end='')",
'h':"sys.exit()",
'<':"direction='left'",
'>':"direction='right'",
'^':"direction='up'",
'v':"direction='down'",
'~':"acc=0",
'{':"times*=10",
'}':"times//=10",
'(':"direction='right';execute=not(acc)",
')':"execute=True",
'!':"Y=random.choice(range(len(box[X])))"
}
while token!=EOF:
  token=box[X][Y]
  if token==')':execute=True
  if (token in codepage) and execute and (token not in '{}()'):
    for _ in range(times):
      exec(commands[token])
  if token in '{}()':
    exec(commands[token])
  if direction=='right':Y+=1
  if direction=='left':Y-=1
  if direction=='up':X-=1
  if direction=='down':X+=1
