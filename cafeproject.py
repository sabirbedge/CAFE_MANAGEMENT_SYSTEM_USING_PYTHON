import sys
import mysql.connector

class BackEndOperation:
    def __init__(self):
        self.mydb=mysql.connector.connect(host='localhost',user='root',password='',database='pydb')
        self.mycur=self.mydb.cursor(buffered=True)

    def setUserData(self,cnm,cadd):
        sql='insert into tblcustomer(nm,addr) values(%s,%s)'
        val=(cnm,cadd)
        self.mycur.execute(sql,val)
        self.mydb.commit()
    
    def getUserData(self):
        data=[]
        self.mycur.execute("select * from tblcustomer order by id desc")
        data=self.mycur.fetchone()
        return data
    
    def setCustProd(self,pname,quantity,prc,cid):
        sql="insert into tblprod(pnm,qty,price,id) values('{}',{},{},{})".format(pname,quantity,prc,cid)
        self.mycur.execute(sql)
        self.mydb.commit()
    
    def getCustProdId(self,cid):
        custId=[]
        sql='select pid from tblprod where id={}'.format(cid)
        self.mycur.execute(sql)
        custId=self.mycur.fetchall()
        return custId
    
    def getUserId(self):
        self.mycur.execute("select id from tblcustomer order by id desc")
        cid=self.mycur.fetchone()
        return cid 
    
    def getCustProdDataById(self,cid):
        sql='select * from tblprod where pid=%s'
        val=(cid)
        self.mycur.execute(sql,val)
        custData=self.mycur.fetchall()
        for y in custData:
            print(y[1],' \t\t\t\t\t ',end='')#item nm
            print(y[2],end='')#item qty
            print('\t\t\t\t',y[3])#item price


class Home:
    def homeFun(this):
        print("\n\n====================================================================================================================")
        print("1- Menu")
        print("2- New Customer")
        print("3- Exit")
        ch1=int(input("Enter your choice :"))
        return ch1
        
class Customer(Home):
    obj=BackEndOperation()
    uid=0
    def custFun(this):
        print("\n\n======================================================================================================================")
        this.nm=str(input("Enter Customer Name - "))
        this.add=str(input("Enter Customer Address - "))
        obj.setUserData(this.nm,this.add)
        this.uid=obj.getUserId()
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Menu(Customer):
    def disMenu(this):
        print('\n\n==================================================== MENU =============================================================')
        print('1- Pizza')
        print('2- Burger')
        print('3- Sandwich')
        print('4- Ice-Cream')
        print('5- Tea')
        print('6- Coffe')
        print('7- Cold Drinks')
        print('8- Juice')
        print('9- Snakes')
        print('10- Exit')
        mc=int(input('\nEnter your choice-'))
        return mc

class Pizza(Menu):
    p=[]
    pt=1
    def disPizza(this):
        print('\n\n================================================== Pizza Items ================================================')
        print('Item Name \t\t\t\t Price')
        print("---------------------------------------------------------------------------------------------------------------------")
        print('a- Margherita \t\t\t\t ₹ 70')
        print('b- Cheese Margherita \t\t\t ₹ 100')
        print('c- Paneer Makhani \t\t\t ₹ 80')
        print('d- Tandoori Paneer \t\t\t ₹ 90')
        pc=input('\nEnter your order-')
        pq=int(input('Enter quantity-'))
        if pc=='a':
            pc='Margherita'
            pt=70*pq
        if pc=='b':
            pc='Cheese Margherita'
            pt=100*pq
        if pc=='c':
            pc='Paneer Makhani'
            pt=80*pq
        if pc=='d':
            pc='Tandoori Paneer'
            pt=90*pq
        this.p.append(pc)
        this.p.append(pq)
        this.p.append(pt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Burger(Pizza):
    b=[]
    bt=1
    def disBurger(this):
        print('\n\n========================================== Burger Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Veg Burger \t\t\t\t ₹ 70')
        print('b- Crunchy Veg Burger \t\t\t ₹ 80')
        print('c- Chicken Burger \t\t\t ₹ 90')
        print('d- Crunchy Chicken Burger \t\t\t ₹ 100')
        bc=input('\nEnter your order-')
        bq=int(input('Enter quantity-'))
        if bc=='a':
            bc='Veg Burger'
            bt=70*bq
        if bc=='b':
            bc='Crunchy Veg Burger'
            bt=80*bq
        if bc=='c':
            bc='Chicken Burger'
            bt=90*bq
        if bc=='d':
            bc='Crunchy Chicken Burger'
            bt=100*bq
        this.b.append(bc)
        this.b.append(bq)
        this.b.append(bt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Sandwich(Burger):
    s=[]
    st=1
    def disSandwich(this):
        print('\n\n========================================== Sandwich Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Veg Sandwich \t\t\t\t ₹ 40')
        print('b- Cheese  Sandwich \t\t\t ₹ 50')
        print('c- Chicken Sandwich \t\t\t ₹ 60')
        print('d- Egg Sandwich \t\t\t ₹ 45')
        sc=input('\nEnter your order-')
        sq=int(input('Enter quantity-'))
        if sc=='a':
            sc='Veg Sandwich'
            st=40*sq
        if sc=='b':
            sc='Cheese Sandwich'
            st=50*sq
        if sc=='c':
            sc='Chicken Sandwich'
            st=60*sq
        if sc=='d':
            sc='Egg Sandwich'
            st=45*sq
        this.s.append(sc)
        this.s.append(sq)
        this.s.append(st)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Ice_cream(Sandwich):
    i=[]
    it=1
    def disIce_cream(this):
        print('\n\n========================================== Ice-Cream Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Vanila Ice-Cream \t\t\t\t ₹ 40')
        print('b- Chocolate Ice-Cream \t\t\t ₹ 50')
        print('c- Kulfi \t\t\t ₹ 20')
        print('d- Mango Ice-Cream \t\t\t ₹ 30')
        ic=input('\nEnter your order-')
        iq=int(input('Enter quantity-'))
        if ic=='a':
            ic='Vanila Ice-Cream'
            it=40*iq
        if ic=='b':
            ic='Chocolate Ice-Cream'
            it=50*iq
        if ic=='c':
            ic='Kulfi'
            it=20*iq
        if ic=='d':
            ic='Mango Ice-Cream'
            it=30*iq
        this.i.append(ic)
        this.i.append(iq)
        this.i.append(it)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Tea(Ice_cream):
    t=[]
    tt=1
    def disTea(this):
        print('\n\n========================================== Tea Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- White Tea \t\t\t\t ₹ 10')
        print('b- Black Tea \t\t\t ₹ 15')
        print('c- Green \t\t\t ₹ 20')
        print('d- Herbal Tea\t\t\t ₹ 30')
        tc=input('\nEnter your order-')
        tq=int(input('Enter quantity-'))
        if tc=='a':
            tc='White Tea'
            tt=10*tq
        if tc=='b':
            tc='Black Tea'
            tt=15*tq
        if tc=='c':
            tc='Green Tea'
            tt=20*tq
        if tc=='d':
            tc='Herbal Tea'
            tt=30*tq
        this.t.append(tc)
        this.t.append(tq)
        this.t.append(tt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Coffee(Tea):
    cf=[]
    cft=1
    def disCoffee(this):
        print('\n\n========================================== Coffee Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Cold Coffee \t\t\t\t ₹ 100')
        print('b- Hot Coffee \t\t\t ₹ 50')
        print('c- Chocolate Coffee \t\t\t ₹ 150')
        cfc=input('\nEnter your order-')
        cfq=int(input('Enter quantity-'))
        if cfc=='a':
            cfc='Cold Coffee'
            cft=100*cfq
        if cfc=='b':
            cfc='Hot Coffee'
            cft=50*cfq
        if cfc=='c':
            cfc='Chocolate Coffee'
            cft=150*cfq
        this.cf.append(cfc)
        this.cf.append(cfq)
        this.cf.append(cft)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class ColdDrink(Coffee):
    cd=[]
    cdt=1
    def disColdDrink(this):
        print('\n\n========================================== Cold Drink Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Thumbs-up \t\t\t\t ₹ 20')
        print('b- Sprite \t\t\t ₹ 30')
        print('c- Mountain-Dew \t\t\t ₹ 50')
        print('d- Mirinda \t\t\t ₹ 50')
        print('e- CoCo-Cola \t\t\t ₹ 30')
        print('f- Jira-Soda \t\t\t ₹ 30')
        print('g- Red-Bull \t\t\t ₹ 100')
        cdc=input('\nEnter your order-')
        cdq=int(input('Enter quantity-'))
        if cdc=='a':
            cdc='Thumbs-up'
            cdt=20*cdq
        if cdc=='b':
            cdc='Sprite'
            cdt=30*cdq
        if cdc=='c':
            cdc='Mountain-Dew'
            cdt=50*cdq
        if cdc=='d':
            cdc='Mirinda'
            cdt=50*cdq
        if cdc=='e':
            cdc='CoCo-Cola'
            cdt=30*cdq
        if cdc=='f':
            cdc='Jira-Soda'
            cdt=30*cdq
        if cdc=='g':
            cdc='Red-Bull'
            cdt=100*cdq
        this.cd.append(cdc)
        this.cd.append(cdq)
        this.cd.append(cdt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Juice(ColdDrink):
    j=[]
    jt=1
    def disJuice(this):
        print('\n\n========================================== Juice Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Mango \t\t\t\t ₹ 30')
        print('b- Pineapple \t\t\t ₹ 30')
        print('c- Apple \t\t\t ₹ 50')
        print('d- Banana \t\t\t ₹ 20')
        print('e- Orange \t\t\t ₹ 20')
        print('f- Water-Melon \t\t\t ₹ 20')
        jc=input('\nEnter your order-')
        jq=int(input('Enter quantity-'))
        if jc=='a':
            jc='Mango'
            jt=30*jq
        if jc=='b':
            jc='Pineapple'
            jt=30*jq
        if jc=='c':
            jc='Apple'
            jt=50*jq
        if jc=='d':
            jc='Banana'
            jt=20*jq
        if jc=='e':
            jc='Orange'
            jt=20*jq
        if jc=='f':
            jc='Water-Melon'
            jt=20*jq
        this.j.append(jc)
        this.j.append(jq)
        this.j.append(jt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

class Snaks(Juice):
    sn=[]
    snt=1
    total=0         
    id=0
    def disSnaks(this):
        print('\n\n========================================== Snaks Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- French-Fry \t\t\t\t ₹ 20')
        print('b- Pop-corn \t\t\t ₹ 20')
        print('c- Potato-Chips \t\t\t ₹ 20')
        print('d- Banana-Chips \t\t\t ₹ 20')
        print('e- Kurkure \t\t\t ₹ 20')
        snc=input('\nEnter your order-')
        snq=int(input('Enter quantity-'))
        if snc=='a':
            snc='French-Fry'
            snt=20*snq
        if snc=='b':
            snc='Pop-corn'
            snt=20*snq
        if snc=='c':
            snc='Potato-Chips'
            snt=20*snq
        if snc=='d':
            snc='Banana-Chips'
            snt=20*snq
        if snc=='e':
            snc='Kurkure'
            snt=20*snq
        this.sn.append(snc)
        this.sn.append(snq)
        this.sn.append(snt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy
    
    def end(this):
        obj=BackEndOperation()
       # cl=len(this.c)
        pl=len(this.p)
        #print(pl)
        bl=len(this.b)
        sl=len(this.s)
        il=len(this.i)
        tl=len(this.t)
        cfl=len(this.cf)
        cdl=len(this.cd)
        jl=len(this.j)
        snl=len(this.sn)
        global data
        data=obj.getUserData()
        global uid
        uid=data[0]
        print("\n\n********************************************************************************************************************")
        print("\n================================================== BILL ===============================================================")
        print("Customer Details-")
        print("Customer Id - ",data[0])
        print("Customer Name - ",data[1])
        print("Customer City - ",data[2])
        print('\n\n=====================================================================================================================')
        print('Item Name \t\t\t\t\t Quantity \t\t\t Total')
        print("-------------------------------------------------------------------------------------------------------------------------")
        #pizza block started
        if pl>0:
            #print(pl)
            pdata=[]
            temp=0
            while temp<pl:
                #print(this.p[temp],' \t\t\t\t\t ',end='')#item nm
                pdata.append(this.p[temp])
                temp+=1
                #print(this.p[temp],end='')#item qty
                pdata.append(this.p[temp])
                temp+=1
                #print('\t\t\t\t',this.p[temp])#item price
                pdata.append(this.p[temp])
                this.total=this.total+int(this.p[temp])
                temp+=1
                # print(pdata)
            
            #data=obj.getUserData()
            temp=0
            pdatalen=len(pdata)
            while temp<pdatalen:
                #uid=data[0]
                pnm=pdata[temp]
                temp+=1
                qty=pdata[temp]
                temp+=1
                price=pdata[temp]
                temp+=1
                obj.setCustProd(pnm,qty,price,uid)
        #pizza block ended

        #burger block started
        if bl>0:
            bdata=[]
            temp=0
            while temp<pl:
                bdata.append(this.b[temp])
                temp+=1
                bdata.append(this.b[temp])
                temp+=1
                bdata.append(this.b[temp])
                this.total=this.total+int(this.b[temp])
                temp+=1
            
            temp=0
            bdatalen=len(bdata)
            while temp<bdatalen:
                #uid=data[0]
                pnm=bdata[temp]
                temp+=1
                qty=bdata[temp]
                temp+=1
                price=bdata[temp]
                temp+=1
                obj.setCustProd(pnm,qty,price,uid)
        #burger block ended

        #Sandwich block started
        if sl>0:
            sdata=[]
            temp=0
            while temp<pl:
                sdata.append(this.s[temp])
                temp+=1
                sdata.append(this.s[temp])
                temp+=1
                sdata.append(this.s[temp])
                this.total=this.total+int(this.s[temp])
                temp+=1
            
            temp=0
            sdatalen=len(sdata)
            while temp<sdatalen:
                #uid=data[0]
                pnm=sdata[temp]
                temp+=1
                qty=sdata[temp]
                temp+=1
                price=sdata[temp]
                temp+=1
                obj.setCustProd(pnm,qty,price,uid)
        #sandwich block ended

    #Ice-cream block started
        if il>0:
            idata=[]
            temp=0
            while temp<il:
                idata.append(this.i[temp])
                temp+=1
                idata.append(this.i[temp])
                temp+=1
                idata.append(this.i[temp])
                this.total=this.total+int(this.i[temp])
                temp+=1
            
            temp=0
            idatalen=len(idata)
            while temp<idatalen:
                #uid=data[0]
                pnm=idata[temp]
                temp+=1
                qty=idata[temp]
                temp+=1
                price=idata[temp]
                temp+=1
                obj.setCustProd(pnm,qty,price,uid)
        #Ice-cream block ended

        #Tea block started
        if tl>0:
            tdata=[]
            temp=0
            while temp<tl:
                tdata.append(this.t[temp])
                temp+=1
                tdata.append(this.t[temp])
                temp+=1
                tdata.append(this.t[temp])
                this.total=this.total+int(this.t[temp])
                temp+=1
            
            temp=0
            tdatalen=len(tdata)
            while temp<tdatalen:
                #uid=data[0]
                pnm=tdata[temp]
                temp+=1
                qty=tdata[temp]
                temp+=1
                price=tdata[temp]
                temp+=1
                obj.setCustProd(pnm,qty,price,uid)
        #Tea block ended

        #Coffe block started
        if cfl>0:
            cfdata=[]
            temp=0
            while temp<cfl:
                cfdata.append(this.cf[temp])
                temp+=1
                cfdata.append(this.cf[temp])
                temp+=1
                cfdata.append(this.cf[temp])
                this.total=this.total+int(this.cf[temp])
                temp+=1
            
            temp=0
            cfdatalen=len(cfdata)
            while temp<cfdatalen:
                #uid=data[0]
                pnm=cfdata[temp]
                temp+=1
                qty=cfdata[temp]
                temp+=1
                price=cfdata[temp]
                temp+=1
                obj.setCustProd(pnm,qty,price,uid)
        #Coffe block ended

        #Cold drink block started
        if cdl>0:
            cddata=[]
            temp=0
            while temp<cdl:
                cddata.append(this.cd[temp])
                temp+=1
                cddata.append(this.cd[temp])
                temp+=1
                cddata.append(this.cd[temp])
                this.total=this.total+int(this.cd[temp])
                temp+=1
            
            temp=0
            cddatalen=len(cddata)
            while temp<cddatalen:
                #uid=data[0]
                pnm=cddata[temp]
                temp+=1
                qty=cddata[temp]
                temp+=1
                price=cddata[temp]
                temp+=1
                obj.setCustProd(pnm,qty,price,uid)
        #Cold drink  block ended

        #Juice block started
        if jl>0:
            jdata=[]
            temp=0
            while temp<jl:
                jdata.append(this.j[temp])
                temp+=1
                jdata.append(this.j[temp])
                temp+=1
                jdata.append(this.j[temp])
                this.total=this.total+int(this.j[temp])
                temp+=1
            
            temp=0
            jdatalen=len(jdata)
            while temp<jdatalen:
               # uid=data[0]
                pnm=jdata[temp]
                temp+=1
                qty=jdata[temp]
                temp+=1
                price=jdata[temp]
                temp+=1
                obj.setCustProd(pnm,qty,price,uid)
        #Juice  block ended

        #Juice block started
        if snl>0:
            sndata=[]
            temp=0
            while temp<jl:
                sndata.append(this.sn[temp])
                temp+=1
                sndata.append(this.sn[temp])
                temp+=1
                sndata.append(this.sn[temp])
                this.total=this.total+int(this.sn[temp])
                temp+=1
            
            temp=0
            sndatalen=len(sndata)
            while temp<sndatalen:
               # uid=data[0]
                pnm=sndata[temp]
                temp+=1
                qty=sndata[temp]
                temp+=1
                price=sndata[temp]
                temp+=1
                obj.setCustProd(pnm,qty,price,uid)
        #Juice  block ended
        custProdId=obj.getCustProdId(uid)
        for x in custProdId:
                obj.getCustProdDataById(x)
        print("----------------------------------------------------------------------------------")
        print('Total Amount : ',this.total)
        sys.exit()
        
while True:
        h=Snaks()
        obj=BackEndOperation()#for db operations
        ch=h.homeFun()
        if(ch==1):#for displaying menu
            mc=h.disMenu()
            if mc==10:#for displaying home menu
                ch=h.homeFun()
            if mc==1:#for displaying Pizza menu
                dy=h.disPizza()
                if dy=='y':
                    continue
                if dy=='n':
                    h.end()
            if mc==2:#for displaying Burger menu
                dy=h.disBurger()
                if dy=='y':
                    continue
                if dy=='n':
                    h.end()
            if mc==3:#for displaying Sandwich menu
                dy=h.disSandwich()
                if dy=='y':
                    continue
                if dy=='n':
                    h.end()
            if mc==4:#for displaying Ice_cream menu
                dy=h.disIce_cream()
                if dy=='y':
                    continue
                if dy=='n':
                    h.end()
            if mc==5:#for displaying Tea menu
                dy=h.disTea()
                if dy=='y':
                    continue
                if dy=='n':
                    h.end()
            if mc==6:#for displaying Coffee menu
                dy=h.disCoffee()
                if dy=='y':
                    continue
                if dy=='n':
                    h.end()
            if mc==7:#for displaying ColdDrink menu
                dy=h.disColdDrink()
                if dy=='y':
                    continue
                if dy=='n':
                    h.end()
            if mc==8:#for displaying Juice menu
                dy=h.disJuice()
                if dy=='y':
                    continue
                if dy=='n':
                    h.end()
            if mc==9:#for displaying Snaks menu
                dy=h.disSnaks()
                if dy=='y':
                    continue
                if dy=='n':
                    h.end()
                    
        if(ch==2):
            dy=h.custFun()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if(ch==3):#for displaying exit
            h.end()

    
        
    



            
        
            
        


