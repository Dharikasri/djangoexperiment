from django.shortcuts import render

def first_page(request):
    return render(request,'page/firstpage.html')

def second_page(request):
    return render(request,'page/secondpage.html')
