class Book():
    def __init__(self,ISBN,Title,Author,publisher):
        self.ISBN=ISBN
        self.Title=Title
        self.Author=Author
        self.publisher=publisher


    def show(self):
        print(self.ISBN,self.Title,self.Author,self.publisher)

class Booklist():
    def __init__(self):
        self.books=[]

    def show(self):
        print('ISBN','Title','Author','publisher')
        for s in self.books:
            s.show()

    def __insert(self,s):
        i=0
        while(i<len(self.books)and s.ISBN>self.books[i].ISBN):
            i=i+1
            if (i<len(self.books)and s.ISBN==self.books[i].ISBN):
                print(s.ISBN+'已经存在')
                return False
            self.books.insert(i,s)
            print('增加成功')
            return True

    def __update(self,s):
        flag=False
        for i in range(len(self.books)):
            if (s.ISBN==self.books[i].ISBN):
                self.books[i].Title=s.Title
                self.books[i].Author=s.Author
                self.books[i].publisher
                print('修改成功')
                flag=True
                break
        if (not flag):
            print('没有这个教材')
        return flag

    def __delete(self,ISBN):
        flag=False
        for i in range(len(self.books)):
            if(self.books[i].ISBN==ISBN):
                del self.books[i]
                print('删除成功')
                flag=True
                break
        if (not flag):
            print('没有这个教材')
            return flag

    def delete(self):
        ISBN=input('ISBN=')
        if (ISBN !=''):
            self.__delete(ISBN)

    def insert(self):
        ISBN=input('ISBN=')
        Title=input('Title=')
        Author=input('Author=')
        publisher=input('publisher=')
        if ISBN !='' and Title !='':
            self.__insert(Book(ISBN,Title,Author,publisher))
        else:
            print('ISBN教材名不能为空')

    def update(self):
        ISBN = input('ISBN=')
        Title = input('Title=')
        Author = input('Author=')
        publisher = input('publisher=')
        if ISBN != '' and Title != '':
            self.__insert(Book(ISBN, Title, Author, publisher))
        else:
            print('ISBN教材名不能为空')

    def save(self):
        try:
            f=open('books.txt','wt')
            for b in self.books:
                f.write(b.ISBN+'\n')
                f.write(b.Title+'\n')
                f.write(b.Author+'\n')
                f.write(b.publisher+'\n')
            f.close()
        except Exception as err:
            print(err)

    def read(self):
        self.books=[]
        try:
            f=open('books.txt','rt')
            while True:
                ISBN=f.readline().strip('\n')
                ISBN = f.readline().strip('\n')
                ISBN = f.readline().strip('\n')
                ISBN = f.readline().strip('\n')
                if ISBN !=''and Title !='' and Author !='' and publisher!='':
                    b=Book(ISBN,Title,Author,publisher)
                    self.books.append(b)
                else:
                    break
            f.close()
        except:
            pass

    def process(self):
        self.read()
        while True:
            s=input('>')
            if (s=='show'):
                self.show()
            elif (s=='insert'):
                self.insert
            elif (s=='delete'):
                self.delete()
            elif (s=='exit'):
                break
            else:
                print('show:show books')
                print('insert:insert a new book')
                print('update:insert a new book')
                print('delete :delete a book')
                print('exit: exit')
        self.save()

books=Booklist
books.process()











