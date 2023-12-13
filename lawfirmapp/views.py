from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import mysql.connector as MySQLdb
from django.core.files.storage import FileSystemStorage
import getpass
import os

db=MySQLdb.connect(
    host='localhost',
    user='root',
    password='',
    database='lawfirm')
c=db.cursor()


def index(request):
    return render(request,'index.html')

def login(request):
    msg = ""
    if(request.POST):
        email = request.POST.get("email")
        pwd = request.POST.get("pass")
        s = "SELECT COUNT(*) FROM tbllogin WHERE username='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            s = "SELECT * FROM tbllogin WHERE username='"+email+"'"
            c.execute(s)
            i = c.fetchone()
            if(i[2] == pwd):
                request.session['email']=email
                if(i[3] == "admin"):
                    return HttpResponseRedirect("/admin")
                elif(i[3] == "advocate"):
                    return HttpResponseRedirect("/advocate")
                elif(i[3] == "client"):
                    return HttpResponseRedirect("/client")
            else:
                msg = "Incorrect Password"
        else:
            msg = "User doesn't exist"
    return render(request,'login.html',{"msg":msg})

def contact(request):
    return render(request,'contact.html')

def signup(request):
    msg=""
    if(request.POST):
        adv_name=request.POST.get("adv_name")
        adv_spec=request.POST.get("adv_spec")
        adv_qual=request.POST.get("adv_qual")
        adv_email=request.POST.get("adv_email")
        adv_exp=request.POST.get("adv_exp")
        adv_roll=request.POST.get("adv_roll")
        adv_mob=request.POST.get("adv_mob")
        password=request.POST.get("password")
        s="select count(*) from tbllogin where username='"+str(adv_email)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Email Already Exists"
        else:
            s="INSERT INTO tbladv (adv_name,adv_spec,adv_qual,adv_email,adv_exp,adv_roll,adv_mob) values('"+str(adv_name)+"','"+str(adv_spec)+"','"+str(adv_qual)+"','"+str(adv_email)+"','"+str(adv_exp)+"','"+str(adv_roll)+"','"+str(adv_mob)+"')"
            print(s)
            try:
                c.execute(s)
                db.commit() 
            except:    
                msg="Sorry Registration Error"
            else:
                s="INSERT INTO tbllogin (username,password,type) values('"+str(adv_email)+"','"+str(password)+"','advocate')"
                try:  
                        c.execute(s)
                        db.commit()
                except:
                    msg="Sorry Login Error"
                else:
                    msg="Registration sucessfull"  
    return render(request,'signup.html',{"msg":msg})

def advocate(request):
    return render(request,'advocate.html')

def advipc(request):
    s1 = "select * from ipc"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    return render(request,'advipc.html',{"data":data})
    return render(request,'advipc.html')

def caseman(request):
    s1 = "select * from casedetails"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    return render(request,'caseman.html',{"data":data})
    return render(request,'caseman.html')

def advclman(request):
    s1 = "select * from tblcl a , tbllogin l where a.cl_mail = l.username  and l.type = 'client'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    if not bool(data):
        msg = "No Clients to show...."
    
        return render(request,"advclman.html",{"data":data,"msgg":msg})
    return render(request,'advclman.html',{"data":data})

def client(request):
    return render(request,'client.html')

def cladvlist(request):
    s1 = "select * from tbladv a , tbllogin l where a.adv_email = l.username  and l.type = 'advocate'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    if not bool(data):
        msg = "No Advocates to show...."
    
        return render(request,"cladvlist.html.html",{"data":data,"msgg":msg})
    return render(request,'cladvlist.html',{"data":data})

def clcase(request):
    msg=""
    if(request.POST):
        case_title=request.POST.get("case_title")
        case_desc=request.POST.get("case_desc")
        case_file=request.POST.get("case_file")
        case_adv=request.POST.get("case_adv")
        username=getpass.getuser()
        s="INSERT INTO casedetails (case_title,case_desc,case_file,adv_name,usename) values('"+str(case_title)+"','"+str(case_desc)+"','"+str(case_file)+"','"+str(case_adv)+"','"+str(username)+"')"
        print(s)
        try:
             c.execute(s)
             db.commit()
             msg="Your Case is Added"
        except:
             msg="Sorry... Error occured. Try Again...."        
    return render(request,'clcase.html',{"msg":msg})

def mycases(request):
    username=getpass.getuser()
    s1 = "select * from casedetails where usename = 'username'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    if not bool(data):
        msg = "No Cases to show...."
    
        return render(request,"mycases.html",{"data":data,"msgg":msg})
    return render(request,'mycases.html',{"data":data})


def clfeedback(request):
    msg=""
    if(request.POST):
        feed_title=request.POST.get("feed_title")
        feed_desc=request.POST.get("feed_desc")
        s="INSERT INTO tblfeedback (feed_title,feed_desc) values('"+str(feed_title)+"','"+str(feed_desc)+"')"
        print(s)
        try:
             c.execute(s)
             db.commit()
             msg="Thank you for your feedback"
        except:
             msg="Sorry... Error occured. Try Again...."
    return render(request,'clfeedback.html',{"msg":msg})

def admin(request):
    return render(request,'admin.html')

def adcl(request):
    s1 = "select * from tblcl a , tbllogin l where a.cl_mail = l.username  and l.type = 'client'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    if not bool(data):
        msg = "No Clients to show...."
    
        return render(request,"adcl.html",{"data":data,"msgg":msg})
    return render(request,'adcl.html',{"data":data})

def adadv(request):
    s1 = "select * from tbladv a , tbllogin l where a.adv_email = l.username  and l.type = 'advocate'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    if not bool(data):
        msg = "No Advocates to show...."
    
        return render(request,"adadv.html",{"data":data,"msgg":msg})
    return render(request,'adadv.html',{"data":data})

def adcase(request):
    s1 = "select * from casedetails"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    return render(request,'adcase.html',{"data":data})
    return render(request,'adcase.html')

def adipc(request):
    ss = "select * from ipc"
    c.execute(ss)
    data1 = c.fetchall()
    if 'ipc' in request.POST:
        ipc_section = request.POST.get("ipc_section")
        ipc_description = request.POST.get("ipc_description")
        s = "select count(*) from ipc where ipc_section = '"+str(ipc_section)+"'"
        c.execute(s)
        data = c.fetchone()

        if data[0] == 0 :
            s1 = "insert into ipc(`ipc_section`,`ipc_description`) values('"+str(ipc_section)+"','"+str(ipc_description)+"')"
            c.execute(s1)
            db.commit()
            msg = str(ipc_section)+" added Successfully"
            return render(request,"adipc.html",{"data1":data1,"msg":msg})
        else:
            msg = str(ipc_section)+" already exists"
            return render(request,"adipc.html",{"msg":msg,"data1":data1})
    return render(request,'adipc.html',{"data1":data1})

def adfeedback(request):
    s1 = "select * from tblfeedback"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    return render(request,'adfeedback.html',{"data":data})
    return render(request,'adfeedback.html')

def practiceareas(request):
    return render(request,'practice-areas.html')

def user_register(request):
    msg=""
    if(request.POST):
        cl_name=request.POST.get("cl_name")
        cl_mail=request.POST.get("cl_mail")
        cl_mob=request.POST.get("cl_mob")
        cl_adhaar=request.POST.get("cl_adhaar")
        cl_address=request.POST.get("cl_address")
        password=request.POST.get("password")
        s="select count(*) from tbllogin where username='"+str(cl_mail)+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Email Already Exists"
        else:
            s="INSERT INTO tblcl (cl_name,cl_mail,cl_mob,cl_adhaar,cl_address) values('"+str(cl_name)+"','"+str(cl_mail)+"','"+str(cl_mob)+"','"+str(cl_adhaar)+"','"+str(cl_address)+"')"
            print(s)
            try:
                c.execute(s)
                db.commit()
            except:
             msg="Sorry Registration Error"
            else:
                s="INSERT INTO tbllogin (username,password,type) values('"+str(cl_mail)+"','"+str(password)+"','client')"
                try:
                    c.execute(s)
                    db.commit() 
                except:
                    msg="Sorry Login Error"
                else:
                    msg="Registration sucessfull"    
    return render(request,'user_register.html',{"msg":msg})
    
def home(request):
    return render(request,'index.html')

