from django.shortcuts import render, get_object_or_404
from .form import ShopifyOrderForms
from .models import ShopifyOrder

# Create your views here.
def ShopifyOrderList(request):
    lst = ShopifyOrder.objects.order_by('-created_at')
    return render(request, "bmedia/home.html", {'lst': lst})

def ShopifyDetailsSave(request):
    id = request.POST.get('id')
    instance = get_object_or_404(ShopifyOrder, id=id)
    form = ShopifyOrderForms(instance=instance)
    context = {
        'instance': instance,
        'form': form,
        'id':id
    }
    return render(request, 'bmedia/shopify_form.html', context)

def ShopifyUpdate(request):
      id = request.POST.get('id')
      instance = get_object_or_404(ShopifyOrder, id=id)
      shopifyform = ShopifyOrderForms(request.POST or None, instance=instance)
      if shopifyform.is_valid():
          shopifyform.save()
      lst = ShopifyOrder.objects.order_by('-created_at')
      return render(request, 'bmedia/home.html', {'lst': lst})

