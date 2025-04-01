from django.contrib import admin
from .models import Post, Categoria, Etiqueta, Comentario, PerfilUsuario, ConfiguracionBlog, ImagenGaleria, MensajeContacto

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Etiqueta)   
admin.site.register(Comentario)
#admin.site.register(PerfilUsuario)  
admin.site.register(ConfiguracionBlog)
admin.site.register(ImagenGaleria)  
admin.site.register(MensajeContacto)

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre')
    fields = ('usuario', 'nombre', 'biografia', 'foto')