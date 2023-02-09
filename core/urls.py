from django.urls import path
from .views import ( cadastro_user, login_user, logout_user, contato,
                    HomeListView, ProdutoDetail, ShopListView, ReceptorListView, Fones_OuvidoListView,
                    ControleListView,AcessoriosListView, ConsoleListView, 
                    
                    )

app_name = 'ecommerce'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('contato/', contato, name='contato'),
    path('detail/<int:pk>', ProdutoDetail.as_view(), name='detail'),

    #path('contato/', contato, name='contato'),

    # Urls de Login e Register
    path('login/', login_user, name="login"),
    path('login/cadastro/', cadastro_user, name="cadastro"),
    path('sair/', logout_user, name="sair"),


    # Urls da Categoria
    path('categoria/receptores/', ReceptorListView.as_view(), name='receptor'),
    path('categoria/headset/', Fones_OuvidoListView.as_view(), name='fones'),
    path('categoria/controles/', ControleListView.as_view(), name='controles'),
    path('categoria/acessorios/', AcessoriosListView.as_view(), name='acessorios'),
    path('categoria/consoles/', ConsoleListView.as_view(), name='consoles'),
]