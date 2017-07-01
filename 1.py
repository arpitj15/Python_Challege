"""
Challenge 1: Substitution Cypher 
"""

pt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
alpha = 'abcdefghijklmnopqrstuvwxyz'
special = [".", ",", "(", ")", " "]
ans = ''
for i in pt:
    if i in special:
        ans += i
        continue
    for j in alpha:
        if i == j:
            a = pt.index(j) 
            ans += alpha[(alpha.index(j)+2)%26]
            pt = pt[a+1:]
print(ans)