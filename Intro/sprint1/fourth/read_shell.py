from collections import Counter, defaultdict

def read_pswd():
    with open('/etc/passwd', 'r') as f:
        lines = f.readlines()[10:]
    lines = list(map(lambda x: x.split(":")[0::6], lines))
    dd = defaultdict(list)
    print(lines[:][1])
    for l in lines: dd[l[1]].append(l[0])
    c = Counter([x[1] for x in lines])
    for k,v in dd.items():
       v.sort()
       print(f"{c[k]} - {k}\n{' '.join(v)}")

read_pswd()