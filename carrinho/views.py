from django.shortcuts import render, redirect
from carrinho.models import Cart
from core.models import Produto
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	
	return render(request, 'cart.html', {"cart": cart_obj})
 

def cart_update(request):
    
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Produto.objects.get(id = product_id)
            
        except Produto.DoesNotExist:
            print("Mostrar mensagem ao usuário, esse produto acabou!")
            return redirect("cart:carrinho")
        cart_obj, new_obj = Cart.objects.new_or_get(request) 
        if product_obj in cart_obj.produtos.all(): 
            cart_obj.produtos.remove(product_obj) 
        else: 
            cart_obj.produtos.add(product_obj)
        request.session['cart_items'] = cart_obj.produtos.count()
    return redirect("cart:carrinho")

    

