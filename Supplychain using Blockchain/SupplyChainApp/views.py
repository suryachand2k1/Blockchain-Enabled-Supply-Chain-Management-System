from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
import pymysql
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from Blockchain import *
from Block import *
from datetime import date

blockchain = Blockchain()
if os.path.exists('blockchain_contract.txt'):
    with open('blockchain_contract.txt', 'rb') as fileinput:
        blockchain = pickle.load(fileinput)
    fileinput.close()

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})    

def BrowseProducts(request):
    if request.method == 'GET':
       return render(request, 'BrowseProducts.html', {})

def Login(request):
    if request.method == 'GET':
       return render(request, 'Login.html', {})
    
def ViewOrders(request):
    if request.method == 'GET':
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Product Name</font></th>'
        output+='<th><font size=3 color=black>Customer Name</font></th>'
        output+='<th><font size=3 color=black>Contact No</font></th>'
        output+='<th><font size=3 color=black>Email ID</font></th>'
        output+='<th><font size=3 color=black>Address</font></th>'
        output+='<th><font size=3 color=black>Ordered Date</font></th></tr>'
       
        for i in range(len(blockchain.chain)):
          if i > 0:
              b = blockchain.chain[i]
              data = b.transactions[0]
              arr = data.split("#")
              if len(arr) > 5:
                  print(data)
                  if arr[6] == 'BookOrder':
                      output+='<tr><td><font size=3 color=black>'+arr[0]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[1]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[2]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[3]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[4]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[5]+'</font></td></tr>'
                  
        output+="</table><br/><br/><br/><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'ViewOrders.html', context)     

def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})

def AddProduct(request):
    if request.method == 'GET':
       return render(request, 'AddProduct.html', {})

def BookOrder(request):
    if request.method == 'GET':
        pid = request.GET['id']
        user = ''
        with open("session.txt", "r") as file:
            for line in file:
                user = line.strip('\n')
        file.close()
        details = ''
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'rootroot', database = 'Supplychain',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM register where username='"+user+"'")
            rows = cur.fetchall()
            for row in rows:
                details = row[2]+"#"+row[3]+"#"+row[4]
        today = date.today()
        data = pid+"#"+user+"#"+details+"#"+str(today)+"#BookOrder"
        blockchain.add_new_transaction(data)
        hash = blockchain.mine()
        b = blockchain.chain[len(blockchain.chain)-1]
        print("Previous Hash : "+str(b.previous_hash)+" Block No : "+str(b.index)+" Current Hash : "+str(b.hash))
        bc = "Previous Hash : "+str(b.previous_hash)+"<br/>Block No : "+str(b.index)+"<br/>Current Hash : "+str(b.hash)
        blockchain.save_object(blockchain,'blockchain_contract.txt')
        context= {'data':'Your Order Updated in Supply Chain Block<br/>'+bc}
        return render(request, 'BrowseProducts.html', context)
        
                
        

def UpdateQuantity(request):
    if request.method == 'GET':
        output = ''
        user = ''
        with open("session.txt", "r") as file:
            for line in file:
                user = line.strip('\n')
        file.close()        
        output = '<tr><td><font size="" color="black">Product&nbsp;Name</font></td><td><select name="t1">'
        for i in range(len(blockchain.chain)):
            if i > 0:
                b = blockchain.chain[i]
                data = b.transactions[0]
                print(data)
                arr = data.split("#")
                if len(arr) > 8:
                    if arr[7] == user:
                        output+='<option value='+arr[0]+'>'+arr[0]+'</option>'
        output+="</select></td></tr>"
        context= {'data':output}
        return render(request, 'UpdateQuantity.html', context)

def SearchProductAction(request):
    if request.method == 'POST':
        ptype = request.POST.get('t1', False)
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Product Name</font></th>'
        output+='<th><font size=3 color=black>Company Name</font></th>'
        output+='<th><font size=3 color=black>Product Type</font></th>'
        output+='<th><font size=3 color=black>Quantity</font></th>'
        output+='<th><font size=3 color=black>Price</font></th>'
        output+='<th><font size=3 color=black>Description</font></th>'
        output+='<th><font size=3 color=black>Image</font></th>'
        output+='<th><font size=3 color=black>Book Product</font></th></tr>'
       
        for i in range(len(blockchain.chain)):
          if i > 0:
              b = blockchain.chain[i]
              data = b.transactions[0]
              arr = data.split("#")
              if len(arr) > 8:
                  if arr[2] == ptype:
                      output+='<tr><td><font size=3 color=black>'+arr[0]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[1]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[2]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[3]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[4]+'</font></td>'
                      output+='<td><font size=3 color=black>'+arr[5]+'</font></td>'
                      output+='<td><img src=/static/products/'+arr[6]+'.png width=200 height=200></img></td>'
                      output+='<td><a href=\'BookOrder?id='+arr[0]+'\'><font size=3 color=black>Click Here</font></a></td></tr>'
        output+="</table><br/><br/><br/><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'SearchProducts.html', context)              
        
    
    
def QuantityUpdateAction(request):
    if request.method == 'POST':
      pname = request.POST.get('t1', False)
      qty = request.POST.get('t2', False)
      user = ''
      with open("session.txt", "r") as file:
          for line in file:
              user = line.strip('\n')
      file.close()
      index = 0
      record = 'none'
      for i in range(len(blockchain.chain)):
          if i > 0:
              b = blockchain.chain[i]
              data = b.transactions[0]
              arr = data.split("#")
              if len(arr) > 8:
                  if arr[7] == user and arr[0] == pname:
                      tot_qty = int(arr[3])
                      tot_qty = tot_qty + int(qty)
                      index = i
                      record = arr[0]+"#"+arr[1]+"#"+arr[2]+"#"+str(tot_qty)+"#"+arr[4]+"#"+arr[5]+"#"+arr[6]+"#"+arr[7]+"#"+arr[8]
      output =''
      if record != 'none':
          blockchain.chain.pop(index)
          blockchain.add_new_transaction(record)
          hash = blockchain.mine()
          b = blockchain.chain[len(blockchain.chain)-1]
          print("Previous Hash : "+str(b.previous_hash)+" Block No : "+str(b.index)+" Current Hash : "+str(b.hash))
          bc = "Previous Hash : "+str(b.previous_hash)+"<br/>Block No : "+str(b.index)+"<br/>Current Hash : "+str(b.hash)
          output = 'Product Quantity Details Updated in Supply Chain Block<br/>'+bc
          blockchain.save_object(blockchain,'blockchain_contract.txt')
      else:
          output = 'record not found'
      context= {'data':output}
      return render(request, 'SupplierScreen.html', context)
          
                    
      

def AddProductAction(request):
    if request.method == 'POST':
      pname = request.POST.get('t1', False)
      cname = request.POST.get('t2', False)
      ptype = request.POST.get('t3', False)
      qty = request.POST.get('t4', False)
      price = request.POST.get('t5', False)
      desc = request.POST.get('t6', False)
      image = request.FILES['t7']
      imagename = request.FILES['t7'].name

      user = ''
      with open("session.txt", "r") as file:
          for line in file:
              user = line.strip('\n')
      file.close()        

      fs = FileSystemStorage()
      filename = fs.save('/Users/suryachand/Desktop/Supplychain using Blockchain/SupplyChainApp/static/products/'+imagename+'.png', image)
      data = pname+"#"+cname+"#"+ptype+"#"+qty+"#"+price+"#"+desc+"#"+imagename+"#"+user+"#AddProduct"
      blockchain.add_new_transaction(data)
      hash = blockchain.mine()
      b = blockchain.chain[len(blockchain.chain)-1]
      print("Previous Hash : "+str(b.previous_hash)+" Block No : "+str(b.index)+" Current Hash : "+str(b.hash))
      bc = "Previous Hash : "+str(b.previous_hash)+"<br/>Block No : "+str(b.index)+"<br/>Current Hash : "+str(b.hash)
      blockchain.save_object(blockchain,'blockchain_contract.txt')
      context= {'data':'New Product Details Updated in Supply Chain Block<br/>'+bc}
      return render(request, 'AddProduct.html', context)
      
   
def Signup(request):
    if request.method == 'POST':
      username = request.POST.get('username', False)
      password = request.POST.get('password', False)
      contact = request.POST.get('contact', False)
      email = request.POST.get('email', False)
      address = request.POST.get('address', False)
      usertype = request.POST.get('type', False)

      db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'rootroot', database = 'Supplychain',charset='utf8')
      db_cursor = db_connection.cursor()
      student_sql_query = "INSERT INTO register(username,password,contact,email,address,usertype) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"','"+usertype+"')"
      db_cursor.execute(student_sql_query)
      db_connection.commit()
      print(db_cursor.rowcount, "Record Inserted")
      if db_cursor.rowcount == 1:
       context= {'data':'Signup Process Completed'}
       return render(request, 'Register.html', context)
      else:
       context= {'data':'Error in signup process'}
       return render(request, 'Register.html', context)


def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        usertype = request.POST.get('type', False)
        status = 'none'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'rootroot', database = 'Supplychain',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and row[1] == password and row[5] == usertype:
                    status = 'success'
                    break
                
        if status == 'success' and usertype == 'Supplier':
            file = open('session.txt','w')
            file.write(username)
            file.close()
            context= {'data':"Welcome "+username}
            return render(request, 'SupplierScreen.html', context)
        elif status == 'success' and usertype == 'Consumer':
            file = open('session.txt','w')
            file.write(username)
            file.close()
            context= {'data':"Welcome "+username}
            return render(request, 'ConsumerScreen.html', context)
        else:
            context= {'data':'Invalid login details'}
            return render(request, 'Login.html', context)





        
            
