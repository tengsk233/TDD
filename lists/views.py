from django.shortcuts import render
from django.test import TestCase
from django.http import HttpResponse

# # Create your views here.
# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1+1,3)
#
#
def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html',{
        'new_item_text': request.POST.get('item_text', ''),
    })
    #return HttpResponse('<html><title>To-Do lists</title></html>')
#home_page = None