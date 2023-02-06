from django.contrib import admin

from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'preco', 'stoque', 'categoria',)
    list_editable = ('preco', 'stoque', 'categoria',)
    list_filter = ('categoria',)
