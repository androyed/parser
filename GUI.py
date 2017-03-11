try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from lxml import etree

class MultipleScrollingListbox(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Biosphera')
        self.mask1 = StringVar()
        self.mask2 = StringVar()
        self.label1 = Label(self, text = 'Название препарата')
        self.label2 = Label(self, text = 'Цена')
        self.label3 = Label(self, text = 'Активное вещество')

        self.entry1 = Entry (self, textvariable=self.mask1)
        #self.entry1.bind('<key>', self.key)
        self.entry1.bind('<Return>', self.get_product)
        
        self.entryText = StringVar()
        self.entry2 = Entry (self, textvariable=self.entryText , width = 50)
        self.entry3 = Entry (self, textvariable=self.mask2)
        self.entry3.bind('<Return>', self.get_active)

        #the shared scrollbar
        self.scrollbar = Scrollbar(self, orient='vertical')

        #note that yscrollcommand is set to a custom method for each listbox
        self.list1 = Listbox(self, yscrollcommand=self.yscroll1, width = 50, height = 50)
        #self.list1.pack(fill='y', side='left')

        self.list2 = Listbox(self, yscrollcommand=self.yscroll2, width = 50, height = 50)
        #self.list2.pack(expand=1, fill='both', side='left')

        self.list3 = Listbox(self, yscrollcommand=self.yscroll3, width = 50, height = 50)
        #self.list3.pack(fill='y', side='left')

        self.scrollbar.config(command=self.yview)
        #self.scrollbar.pack(side='right', fill='y')

        #self.scrollbar.grid(row=0, column=3, rowspan=3 )
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=0, column=1)
        self.label3.grid(row=0, column=2)

        self.entry1.grid(row=1,column=0)
        self.entry2.grid(row=1,column=1)
        self.entry3.grid(row=1,column=2)

        self.list1.bind('<<ListboxSelect>>', self.onselect)
        self.list1.grid(row=2,column=0)
        self.list3.bind('<<ListboxSelect>>', self.onselect)
        self.list3.grid(row=2,column=1)
        self.list2.bind('<<ListboxSelect>>', self.onselect)
        self.list2.grid(row=2,column=2)

        
        
    
        self.tree = etree.parse("minidom_example.xml")

        
        #self.mask.set("a")
        #Работает вытаскивает только имена массивом
        #nodes = tree.xpath('/products/product/name[contains(., '+ str(self.mask) +')]/text()')

        #Вытаскивает активное вещество
        #nodes1 = tree.xpath('/products/product/name[contains(., '+ str(self.mask) +')]//..//active/text()')

        #Вытаскивает цену массивом
        #nodes2 = tree.xpath('/products/product/name[contains(., '+ str(self.mask) +')]//..//price/text()')

        #self.list1.delete(0, END)
        #self.list2.delete(0, END)
        #self.list3.delete(0, END)
        #for i in nodes:
        #    self.list1.insert(END,i)
        #for i in nodes1:
        #    self.list2.insert(END,i)
        #for i in nodes2:
        #    self.list3.insert(END,i)
        #print ("ok")

    def updateListBoxesProduct(self, mask_new):
        
        print ('mask_product=' + mask_new)
        #mask_new = 'Грип'
        nodes = self.tree.xpath('/products/product/name[contains(.,"'+str(mask_new)+'")]/text()')
        
        #Работает вытаскивает только имена массивом
        #Вытаскивает активное вещество
        nodes1 = self.tree.xpath('/products/product/name[contains(.,"'+str(mask_new)+'")]//..//active/text()')
        #Вытаскивает цену массивом
        nodes2 = self.tree.xpath('/products/product/name[contains(.,"'+str(mask_new)+'")]//..//price/text()')
        self.list1.delete(0, END)
        self.list2.delete(0, END)
        self.list3.delete(0, END)
        for i in nodes:
            self.list1.insert(END,i)
        for i in nodes1:
            self.list2.insert(END,i)
        for i in nodes2:
            self.list3.insert(END,i)

    def updateListBoxesActive(self, mask_new):
        
        print ('mask_active=' + mask_new)
        #mask_new = 'Грип'
        nodes = self.tree.xpath('/products/product/active[contains(.,"'+str(mask_new)+'")]//..//name/text()')
        
        #Работает вытаскивает только имена массивом
        #Вытаскивает активное вещество
        nodes1 = self.tree.xpath('/products/product/active[contains(.,"'+str(mask_new)+'")]/text()')
        #Вытаскивает цену массивом
        nodes2 = self.tree.xpath('/products/product/active[contains(.,"'+str(mask_new)+'")]//..//price/text()')
        self.list1.delete(0, END)
        self.list2.delete(0, END)
        self.list3.delete(0, END)
        for i in nodes:
            self.list1.insert(END,i)
        for i in nodes1:
            self.list2.insert(END,i)
        for i in nodes2:
            self.list3.insert(END,i)

    #def ret(self, event):
        
    def get_product(self, event):
        #print (event.widget.get())
        self.updateListBoxesProduct(event.widget.get())

    def get_active(self, event):
        #print (event.widget.get())
        self.updateListBoxesActive(event.widget.get())
        
    def key(self, event):
        print ('a')
        
#for i in list1:
#    listbox1.insert(END,i)



        #fill the listboxes with stuff
        #for x in range(30):
        #    self.list1.insert('end', x)
        #    self.list2.insert('end', x)
        #    self.list3.insert('end', x)

    #I'm sure there's probably a slightly cleaner way to do it than this
    #Nevertheless - whenever one listbox updates its vertical position,
    #the method checks to make sure that the other one gets updated as well.
    #Without the check, I *think* it might recurse infinitely.
    #Never tested, though.
    def yscroll1(self, *args):
        if (self.list2.yview() != self.list1.yview())and(self.list3.yview() != self.list1.yview()):
            self.list2.yview_moveto(args[0])
            self.list3.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yscroll2(self, *args):
        if (self.list1.yview() != self.list2.yview())and(self.list3.yview() != self.list2.yview()):
            self.list1.yview_moveto(args[0])
            self.list3.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yscroll3(self, *args):
        if (self.list1.yview() != self.list3.yview())and(self.list2.yview() != self.list3.yview()):
            self.list1.yview_moveto(args[0])
            self.list2.yview_moveto(args[0])
        self.scrollbar.set(*args)

  
    def yview(self, *args):
        self.list1.yview(*args)
        self.list2.yview(*args)
        self.list3.yview(*args)
        
#ListBox Element Selected
    def onselect(self ,evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        #print ('You selected item %d: "%s"' % (index, value))
        self.entryText.set(value)

if __name__ == "__main__":
    root = MultipleScrollingListbox()
    root.mainloop()
