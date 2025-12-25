from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def templates(request):
    user={'name':'John Doe', 'age':30, 'city':'New York','lst':{'python','django','html','css','javascript'},'courses':[{'id':101,'name':'Python Basics','price':10,'img':'https://dotnettrickscloud.blob.core.windows.net/article/5520250715143827.webp','posted':datetime.now(),'des':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo illum similique architecto illo?'},{'id':102,'name':'C++ basic to advanced','price':20,'img':'https://blog.jetbrains.com/wp-content/uploads/2023/03/Blog_Social_share_image_1280x720-8.png','posted':datetime.now(),'des':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo illum similique architecto illo?'},{'id':103,'name':'Basics of modern javascript','price':15,'img':'https://miro.medium.com/1*ChC-1PWD1vEXBwV_YRrYWw.jpeg','posted':datetime.now(),'des':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo illum similique architecto illo?'}]}
    return render(request,'templates_filters.html',user)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')