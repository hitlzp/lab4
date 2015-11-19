from django.shortcuts import render_to_response
from book.models import Book, Author

def view_all(request):
    all_objects = Book.objects.all()
    return render_to_response('view_all.html',{'all_objects':all_objects})

flag2 = True
def addbooks(request):
    global flag2
    l = request.GET
    if l:
        author = Author.objects.filter(AuthorID = l['id'])
        if author:
            if flag2:
                auth = Author.objects.get(AuthorID = l['id'])
                flag2=False  
                return render_to_response('post2.html',{'author':auth})
            else:
                ADD3 = Book(ISBN=l['isbn'],
                            Title=l['title'],
                            AuthorID= Author.objects.get(AuthorID = l['id']),
                            Publisher=l['publisher'],
                            PublishDate=l['publishdate'],
                            Price=l['price'],)
                ADD3.save()
                flag2=True
                return render_to_response('finished.html',{'right':True})
        else:
            l = request.GET
            ADD = Author(AuthorID = l['id'],
                         Name = l['name'],
                         Age = l['age'],
                         Country = l['country'],
                         )
            ADD.save()
            ADD2 = Book(ISBN=l['isbn'],
                            Title=l['title'],
                            AuthorID= Author.objects.get(AuthorID = l['id']),
                            Publisher=l['publisher'],
                            PublishDate=l['publishdate'],
                            Price=l['price'],)
            ADD2.save()
            return render_to_response('finished.html',{'right':True})
    else:
        return render_to_response('post1.html',{'right':True})
    
def search(request):
    error = False
    if 'q' in request.GET :
        q = request.GET['q']
        if not q:
            error = True
            return render_to_response('search_form.html',{'error': error})
        else:
            query_list = Book.objects.filter(AuthorID__Name = q)
            if not query_list:
                return render_to_response('search_form.html',{'error': error})
            else:
                return render_to_response ('search_results_.html',{'query_list':query_list})
    else:
        error = True
        return render_to_response('search_form.html', {'error': error})

def list(request):
    all_objects = Book.objects.all()
    return render_to_response('list.html',{'all_objects':all_objects})

def list(request):
    all_objects = Book.objects.all()
    return render_to_response('list.html',{'all_objects':all_objects})

def delete(request):
    id1 = request.GET["id"] 
    Book.objects.filter(ISBN=id1).delete()
    all_objects = Book.objects.all()
    return render_to_response('view_all.html',{'all_objects':all_objects})

def change(request):
    global flag, book, author
    flag = id1 = request.GET["judge"]
    if flag == 'True':
        id1 = request.GET["id"]
        book = Book.objects.get(ISBN=id1)
        author = book.AuthorID
        dic = {'book':book, 'author':author}
        flag=False
        return render_to_response('change1.html', dic)
    else:
        l = request.GET
        author.AuthorID = l["id"]
        author.Name = l["name"]
        author.Age = l["age"]
        author.Country = l['country'] 
        author.save()
        book.ISBN=l['isbn']
        book.Title=l['title']
        book.AuthorID= Author.objects.get(AuthorID = l['id'])
        book.Publisher=l['publisher']
        book.PublishDate=l['publishdate']
        book.Price=l['price']
        book.save()
        flag=True
        dic = {'book':book, 'author':author}
        return render_to_response('choose.html',dic)
    
def show(request):
    id1 = request.GET["id2"]
    book = Book.objects.get(Title=id1)
    author = book.AuthorID
    dic = {'book':book, 'author':author}
    return render_to_response('choose.html',dic)
    
