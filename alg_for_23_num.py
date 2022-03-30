def next_cmd(x,step,res=[]):
    if step==4:
        return res+[x]
    s1=next_cmd(x+1,step+1,res)
    s2=next_cmd(x+5,step+1,res)
    s3=next_cmd(x*3,step+1,res)
    return s1+s2+s3
    
def task():
    r=next_cmd(1,0,[])
    return len(list(set(r)))
    
print(task())
