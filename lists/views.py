from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item
def home_page(request):
    ##if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html')

    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    items = Item.objects.all()
    #else:
    #    new_item_text = ''
    return render(request, 'home.html',{'items': items})