def display_info(a,b,*args,instructor="Colt",**kwargs):
    return [a,b,args,instructor,kwargs]

print(display_info(1,2,3,last_name="Steele",job="Instructor"))