from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Propietario, Departamento

# Agregar la clase Estudiante para administrar desde
# interfaz de administración
# admin.site.register(Estudiante)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class PropietarioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'apellido', 'edad', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')

# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin
admin.site.register(Propietario, PropietarioAdmin)

# Agregar la clase NumeroTelefonico para administrar desde
# interfaz de administración
# admin.site.register(NumeroTelefonico)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# NumeroTelefonico
class DepartamentoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('costo_depa', 'num_cuartos', 'num_banios', 'valor', 'propietario')
    # se agrega el atributo 
    # raw_id_fields que permite acceder a una interfaz 
    # para buscar los estudiantes y seleccionar el que 
    # se desee
    raw_id_fields = ('propietario',)

admin.site.register(Departamento, DepartamentoAdmin)
