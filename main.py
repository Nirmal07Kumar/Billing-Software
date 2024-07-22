from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")


        # ====================Variables================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        # Product Categories List
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]

        # SubCatClothing
        self.SubCatClothing=["Pant","T-Shirt","Shirt",]
        self.pant=["Levis","Murfi","Spykar"]
        self.price_levis=5000
        self.price_murfi=700
        self.price_spykar=8000

        self.T_Shirt=["Polo","Raodster","Jack&Jones"]
        self.price_polo=1500
        self.price_Roadster=1800
        self.price_JackJones=1700

        self.Shirt=["Peter England","Louis Phillips","Park Avenue"]
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_Park=1740

        # SubCatLifeStyle
        self.SubCatLifeStyle=["Bath Soap","Face Creame","Hair Oil"]
        self.Bath_soap=["LifeBuoy","Lux","Santoor","Pearls"]
        self.price_lifebuoy=float(18)
        self.price_lux=38
        self.price_santoor=40
        self.price_pearls=60

        self.Face_creame=["Fair","Ponds","Olay","Garnier"]
        self.price_fair=40
        self.price_ponds=50
        self.price_olay=90
        self.price_garnier=110

        self.Hair_oil=["Parachute","Jasmine","VVD GOld","Mantra"]
        self.price_para=20
        self.price_jasmine=40
        self.price_VVD_gold=25
        self.price_mantra=30

        # SubCatMobiles
        self.SubCatMobiles=["Oppo","Samsung","Xiomi","RealMe","OnePlus"]
        self.Oppo=["Oppo A9 2020","Oppo A59","Oppo F25"]
        self.price_OA9_2020=23000
        self.price_OA59=20000
        self.price_OF25=33000

        self.Samsung=["Galaxy M35","Galaxy M34","Galaxy S23"]
        self.price_GM35=18990
        self.price_GM34=15000
        self.price_GS23=64000

        self.Xiomi=["Red11","Redme-12","RedmePro"]
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.RealMe=["RealMe 12","RealMe 13","RealMe Pro"]
        self.price_real12=25000
        self.price_real13=22000
        self.price_realpro=30000

        self.OnePlus=["OnePlus1","OnePlus2","OnePlus3"]
        self.price_one1=45000
        self.price_one2=60000
        self.price_one3=50000

        # ==============Image 1============
        img = Image.open(r"C:\Users\nirma\Desktop\Billing Software\img\b1.jpg")
        img=img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        # =======Image 2==========
        img_1 = Image.open(r"C:\Users\nirma\Desktop\Billing Software\img\girls.jpg")
        img_1=img_1.resize((500, 130), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)

        # ==========Image 3=========
        img_2 = Image.open(r"C:\Users\nirma\Desktop\Billing Software\img\girl1.jpg")
        img_2=img_2.resize((520, 130), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=500,height=130)

        lbl_title=Label(self.root,text="BILLING SOTFWARE",font=("Bookman Old Style",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

            lbl = Label(lbl_title, font=('times new roman',16,'bold'),background='white',foreground='blue')
            lbl.place(x=0,y=0,width=120,height=45)
            time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No",font=("arial",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblEmail=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)

        #Category
        self.lblCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,values=self.Category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #SubCategory
        self.lblSubCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,values=[""],state="readonly",font=("arial",10,"bold"),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)
   
        #Product Name
        self.lblproduct=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=("arial",10,"bold"),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>> ",self.price)

        #Price
        self.lblPrice=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,state="readonly",font=("arial",10,"bold"),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        # Middle Frame
        Middle_Frame=Frame(Main_Frame,bd=10)
        Middle_Frame.place(x=10,y=150,width=980,height=340)

        # ==============Image 1============
        img_12 = Image.open(r"C:\Users\nirma\Desktop\Billing Software\img\good.jpg")
        img_12=img_12.resize((490, 340), Image.LANCZOS)
        self.photoimg_12 = ImageTk.PhotoImage(img_12)

        lbl_img12=Label(Middle_Frame,image=self.photoimg_12)
        lbl_img12.place(x=0,y=0,width=500,height=340)

        # =======Image 2==========
        img_13 = Image.open(r"C:\Users\nirma\Desktop\Billing Software\img\mall.jpg")
        img_13=img_13.resize((490, 340), Image.LANCZOS)
        self.photoimg_13 = ImageTk.PhotoImage(img_13)

        lbl_img_13=Label(Middle_Frame,image=self.photoimg_13)
        lbl_img_13.place(x=490,y=0,width=500,height=340)


        # Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,font=("arial",12,"bold"),fg="white",bg="red",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        # RightFrame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)


        # Sub Total
        self.lblSubTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        # Govt Tax
        self.lbl_tax=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Govt tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        # Total Amount
        self.lblAmountTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Total Amount",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.inprint,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
    # ================Funtion Declaration==============
    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome Nirmal's Mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")


        self.textarea.insert(END,"\n ================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n================================================\n")



    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error", "Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l))- (self.prices.get()))*Tax)/100)))))
    
    def gen_bill(self):
        if self.product.get()=="": 
            messagebox.showerror("Error", "Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}") 
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n================================================\n")

    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()

    def inprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No!")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l[0]
        self.total.set("")
        self.tax_input.set('')
        self.welcome()
                 



    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(values=self.SubCatClothing)
            self.ComboSubCategory.current(0)
        
        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(values=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(values=self.SubCatMobiles)
            self.ComboSubCategory.current(0)


    def Product_add(self,event=""):
        # Cloathings
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(values=self.pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="T-Shirt":
            self.ComboProduct.config(values=self.T_Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(values=self.Shirt)
            self.ComboProduct.current(0)


        # LifeStyles
        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(values=self.Bath_soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face Creame":
            self.ComboProduct.config(values=self.Face_creame)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(values=self.Hair_oil )
            self.ComboProduct.current(0)

        # Mobiles
        if self.ComboSubCategory.get()=="Oppo":
            self.ComboProduct.config(values=self.Oppo)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(values=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Xiomi":
            self.ComboProduct.config(values=self.Xiomi)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="RealMe":
            self.ComboProduct.config(values=self.RealMe)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="OnePlus":
            self.ComboProduct.config(values=self.OnePlus)
            self.ComboProduct.current(0)

    
    def price(self,event=""):

        #pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(values=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Murfi":
            self.ComboPrice.config(values=self.price_murfi)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(values=self.price_spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # T-Shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(values=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(values=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(values=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Shirt
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(values=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Phillips":
            self.ComboPrice.config(values=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(values=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Bath Soap
        if self.ComboProduct.get()=="LifeBuoy":
            self.ComboPrice.config(values=self.price_lifebuoy)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(values=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(values=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pearls":
            self.ComboPrice.config(values=self.price_pearls)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Face Creame
        if self.ComboProduct.get()=="Fair":
            self.ComboPrice.config(values=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(values=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(values=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(values=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        # Hair Oil
        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(values=self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jashmine":
            self.ComboPrice.config(values=self.price_jasmine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="VVD Gold":
            self.ComboPrice.config(values=self.price_VVD_gold)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mantra":
            self.ComboPrice.config(values=self.price_mantra)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Mobiles
        if self.ComboProduct.get()=="Oppo A9 2020":
            self.ComboPrice.config(values=self.price_OA9_2020)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Oppo A59":
            self.ComboPrice.config(values=self.price_OA59)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Oppo F25":
            self.ComboPrice.config(values=self.price_OF25)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Galaxy M34":
            self.ComboPrice.config(values=self.price_GM34)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Galaxy M35":
            self.ComboPrice.config(values=self.price_GM35)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Galaxy S23":
            self.ComboPrice.config(values=self.price_GS23)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Red11":
            self.ComboPrice.config(values=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Redme-12":
            self.ComboPrice.config(values=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RedmePro":
            self.ComboPrice.config(values=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(values=self.price_real12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(values=self.price_real13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe Pro":
            self.ComboPrice.config(values=self.price_realpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus1":
            self.ComboPrice.config(values=self.price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus2":
            self.ComboPrice.config(values=self.price_one2)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus3":
            self.ComboPrice.config(values=self.price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)









if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()