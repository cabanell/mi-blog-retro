from django.contrib import admin
from .models import Post, Categoria, Etiqueta, Comentario, PerfilUsuario, ConfiguracionBlog, ImagenGaleria, MensajeContacto
from .models import Cabra
from .models import Cancion


admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Etiqueta)   
admin.site.register(Comentario)
admin.site.register(PerfilUsuario)  
admin.site.register(ConfiguracionBlog)
admin.site.register(ImagenGaleria)  
admin.site.register(MensajeContacto)
admin.site.register(Cabra)

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida')




