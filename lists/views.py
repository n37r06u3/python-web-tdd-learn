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

    #else:
    #    new_item_text = ''
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')