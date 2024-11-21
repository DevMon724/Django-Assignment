"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404
from django.shortcuts import render



movie_list = [
    {'title' : "파묘", 'director' : "장재현"},
    {'title' : "웡카", 'director' : "폴 킴"},
    {'title' : "듄 : 파트2", 'director' : "드니 빌뇌브"},
    {'title' : "시민덕희", 'director' : "박영주"}
]

def index(request):
    return HttpResponse("<h1>Hello!</h1>")

def books(request):
    # book_text = ""
    #
    # for i in range(0, 10) :
    #     book_text += f'book {i}'
    #
    # return HttpResponse(book_text)
    return render(request, "books.html", {'range': range(0,10)})

def book_detail(request, num):
    # book_text = f"book {num}번 페이지입니다."
    # return HttpResponse(book_text)
    return render(request, "book_detail.html", {'num': num})


def movies(request):
#     movie_titles = [
#         f'<a href="/movie/{index}/">{movie["title"]}</a><br>'
#         for index, movie in enumerate(movie_list)
#     ]
#     response_text = '<br>'.join(movie_titles)
#
#     return HttpResponse(response_text)
    return render(request, "movies.html", {'movie_list': movie_list})

def movie_detail(request, index):
    if index > len(movie_list) -1:

        raise Http404

    movie = movie_list[index]
    context = {"movie": movie}
    return render(request, "movie_detail.html", context)

def gugudan(request, num):
    context = {
        "num" : num,
        "results" : [num * i for i in range(1,10)]
    }

    return render(request, "gugudan.html", context)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('books/', books),
    path('book_detail/<int:num>', book_detail),
    path('movies/', movies),
    path('movie/<int:index>/', movie_detail),
    path('gugudan/<int:num>', gugudan),
]

