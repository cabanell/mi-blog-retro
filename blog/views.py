from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import PerfilUsuario
from .models import Cabra
from django.http import HttpResponse

from .models import (
    Post, Categoria, Etiqueta, Comentario,
    ConfiguracionBlog, ImagenGaleria
)

from .forms import ComentarioForm, ContactoForm


def feed(request):
    posts = Post.objects.filter(publicado=True, publicado_en__lte=timezone.now()).order_by('-publicado_en')
    fondo = ConfiguracionBlog.objects.first()
    comentario_form = ComentarioForm()

    if request.method == 'POST' and 'post_id' in request.POST:
        form = ComentarioForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)

            perfil = getattr(request.user, 'perfilusuario', None)
            if perfil and perfil.puede_comentar:
                comentario = form.save(commit=False)
                comentario.autor = request.user
                comentario.post = post
                comentario.save()
                return redirect('feed')

    return render(request, 'blog/feed.html', {
        'posts': posts,
        'fondo': fondo,
        'comentario_form': comentario_form
    })


@require_POST
def dar_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('feed')


@require_POST
def dar_dislike(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.dislikes += 1
    post.save()
    return redirect('feed')


def sobre_mi(request):
    perfil = PerfilUsuario.objects.filter(usuario__is_superuser=True).first()
    return render(request, 'blog/sobre_mi.html', {'perfil': perfil})


def galeria(request):
    imagenes = ImagenGaleria.objects.all().order_by('-creado_en')
    return render(request, 'blog/galeria.html', {'imagenes': imagenes})


def contacto(request):
    enviado = False

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            enviado = True
    else:
        form = ContactoForm()

    return render(request, 'blog/contacto.html', {
        'form': form,
        'enviado': enviado
    })


def sobre_mi(request):
    perfil = PerfilUsuario.objects.first()
    return render(request, 'blog/sobre_mi.html', {'perfil': perfil})



def vista_cabra(request):
    cabra = Cabra.objects.first()
    if not cabra:
        return render(request, 'blog/cabra.html', {'cabra': cabra})
    return render(request, 'cabra.html', {'cabra': cabra})

