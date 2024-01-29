from django.shortcuts import render

# Create your views here.

# def vari(request):
#     value = "Bu view da qilindi"
#     return render(request=request, template_name='index.html', context={'value':value})

def vari(request):
    nested = {
        '4 gacha ==>': [1, 2, 3],
        '7 gacha ==>': [4, 5, 6],
        '10 gacha ==>': [7, 8, 9],
    }
    return render(request=request, template_name='index.html', context={'nested':nested})