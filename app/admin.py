from django.contrib import admin
from .models import bd_tabla_venta , bd_table_almacen , bd_tabla_asistencias , bd_tabla_trabajador , bd_tabla_usuario , Tabla_Compras_Usuario , Tabla_Producto_Disponible , Tabla_Realizar_Pedido

admin.site.register(bd_tabla_venta)
admin.site.register(bd_table_almacen)
admin.site.register(bd_tabla_asistencias)
admin.site.register(bd_tabla_trabajador)
admin.site.register(bd_tabla_usuario)
admin.site.register(Tabla_Compras_Usuario)
admin.site.register(Tabla_Producto_Disponible)
admin.site.register(Tabla_Realizar_Pedido)