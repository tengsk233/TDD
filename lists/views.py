from django.shortcuts import render,redirect
from django.test import TestCase
from django.http import HttpResponse
from lists.models import Item

# # Create your views here.
# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1+1,3)
#
#
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']
    #     Item.objects.create(text=new_item_text)
    # else:
    #     new_item_text = ''
    #     #return HttpResponse(request.POST['item_text'])
    # # item = Item()
    # # item.text = request.POST.get('item_text', '')
    # # item.save()
    #
    # return render(request, 'home.html',{
    #     'new_item_text': new_item_text,
    # })
    #return HttpResponse('<html><title>To-Do lists</title></html>')
#home_page = None