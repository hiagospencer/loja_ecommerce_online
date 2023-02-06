from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Produto
from django.urls import reverse_lazy
from carrinho.models import Cart


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# ================ FUNCÕE DE LOGIN E REGISTER ====================
def login_user(request):
    if request.method == 'GET':
        return render(request, 'autenticacao/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return render(request, 'autenticacao/login.html')

    


def cadastro_user(request):
    if request.method == 'GET':
        return render(request, 'autenticacao/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf-password')

        # Verificando se a senha e confirmação de senha são iguais
        if password != conf_password:
            messages.error(request, 'Senha e confirmação de  senha diferentes')
            return render(request, 'autenticacao/register.html')

        # Verificando se o tamanho da senha é maior que 8
        elif len(password) < 8:
            messages.error(request, 'A senha contém menos de 8 caracteres')
            return render(request, 'autenticacao/register.html')

        # Verificando se existe usuario com o mesmo nome no banco de dados
        user = User.objects.filter(username=username).first()
        if user:            
            messages.error(request, f'Já existe usuário com o nome "{username}" cadastrado')
            return render(request, 'autenticacao/register.html')

        email_user = User.objects.filter(email=email)
        if email_user:
            messages.error(request,f'Já existe um email cadastrado com {email}')
            return render(request, 'autenticacao/register.html')

        # Salvando usuário no banco de dados 
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            

    return render(request, 'autenticacao/register.html')



def logout_user(request):
    logout(request)
    return redirect('/login/')
   

# ================= Class BaseView =========================

class HomeListView(ListView):
    template_name = 'index.html'
    model = Produto
    paginate_by = 12
    
  

class ProdutoDetail(DetailView):
    template_name = 'detail.html'
    model = Produto
    success_url = reverse_lazy('ecommerce:detail')

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoDetail,  self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


class ShopListView(ListView):
    template_name = 'shop.html'
    model = Produto
    paginate_by = 9

    # barra de pesquisar do template shop
    def get_queryset(self):
        nome_pesquisa = self.request.GET.get('nome')
        if nome_pesquisa:
            produto = Produto.objects.filter(produto__icontains=nome_pesquisa)
        else:
            produto = Produto.objects.all()

        return produto



#  ================= Funções para mostrar somente os templates =======================


def contato(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')


# ========================== TEMPLATES DAS CATEGORIAS ==========================

class ReceptorListView(ListView):
    template_name = 'categorias/receptor.html'
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_receptor = Produto.objects.filter(categoria='receptor').order_by('-data_produto')
        context['categoria_receptor'] = categoria_receptor
        return context



class Fones_OuvidoListView(ListView):
    template_name = 'categorias/fones.html'
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_fones = Produto.objects.filter(categoria='fones').order_by('-data_produto')
        context['categoria_fones'] = categoria_fones
        return context




class ControleListView(ListView):
    template_name = 'categorias/controles.html'
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_controles = Produto.objects.filter(categoria='controles').order_by('-data_produto')
        context['categoria_controles'] = categoria_controles
        return context



class AcessoriosListView(ListView):
    template_name = 'categorias/acessorios.html'
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_acessorios = Produto.objects.filter(categoria='acessorios').order_by('-data_produto')
        context['categoria_acessorios'] = categoria_acessorios
        return context




class ConsoleListView(ListView):
    template_name = 'categorias/consoles.html'
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_consoles = Produto.objects.filter(categoria='video games').order_by('-data_produto')
        context['categoria_consoles'] = categoria_consoles
        return context

