from django.shortcuts import render, get_object_or_404, redirect
from productos.models import Producto
from .carrito import Carro

"""
def agregar_carrito(request, id_producto):
    
    #buscamos el producto que le enviamos por url
    producto = get_object_or_404(Producto, pk = id_producto)
    carrito = Carro(request)
    #agregamos ese producto al carrito
    carrito.agregar_producto(producto)
    return redirect('productos:productos')

def ver_carrito(request):
    
    carrito = Carro(request)
    total = carrito.obtener_total()
    #print(total)
    if request.method == 'GET':
        
        return render(request, 'ver_carrito.html',{
            'carrito':carrito,
            'total':total
        })
"""
    
    
