# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Modelo para categorías (como "reflexiones", "tecnología", etc.)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para etiquetas (pueden agregarse al momento de crear un post)
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Modelo de la publicación principal del blog
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()  # Puede contener HTML simple para estilos
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    imagen_destacada = models.ImageField(upload_to='imagenes_posts/', blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    publicado_en = models.DateTimeField(default=timezone.now)
    programado_para = models.DateTimeField(blank=True, null=True)  # Para programar publicaciones
    publicado = models.BooleanField(default=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

# Comentarios asociados a los posts, solo visibles si el usuario está autorizado
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario por {self.autor.username}"

# Extensión del modelo de usuario para agregar perfil y autorización personalizada
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    puede_publicar = models.BooleanField(default=False)  # Controla si puede escribir posts
    puede_comentar = models.BooleanField(default=True)   # Controla si puede comentar

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

# Configuración del blog, como el fondo de la página principal
class ConfiguracionBlog(models.Model):
    nombre_fondo = models.CharField(max_length=100, default="Fondo principal")
    fondo = models.ImageField(upload_to='fondos/', blank=True, null=True)

    def __str__(self):
        return self.nombre_fondo

# Modelo para la galería de imágenes
class ImagenGaleria(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='galeria/')
    descripcion = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Modelo para mensajes de contacto
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    enviado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.correo})"

