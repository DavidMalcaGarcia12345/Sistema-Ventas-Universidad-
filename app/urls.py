from django.urls import path
from . import views

urlpatterns = [
    path('' , views.login_usuario),
    path('panel_control/' , views.panel_control),

    path('enlace_registrar_ventas/' , views.enlace_registrar_ventas),
    path('enlace_tabla_registro_ventas/' , views.enlace_tabla_registro_ventas), 
    path('logica_registrar_ventas/' , views.logica_registrar_ventas),
    path('enlace_tabla_registro_ventas/logica_eliminar_ventas/<Enumearcion_Ventas>' , views.logica_eliminar_ventas),
    path('enlace_tabla_registro_ventas/enlace_actualizar_ventas/<Enumearcion_Ventas>' , views.enlace_actualizar_ventas),
    path('logica_actualizar_ventas/' , views.logica_actualizar_ventas),

    path('enlace_registrar_ingresos_productos/' , views.enlace_registrar_ingresos_productos),
    path('enlace_tabla_ingresos_productos/' , views.enlace_tabla_ingresos_productos), 
    path('logica_registrar_ingresos_productos/' , views.logica_registrar_ingresos_productos),  
    path('enlace_tabla_ingresos_productos/logica_eliminar_ingresos_prodcutos/<Enumeracion_Recepcion>' , views.logica_eliminar_ingresos_prodcutos),
    path('enlace_tabla_ingresos_productos/enlace_actualizar_ingresos_productos/<Enumeracion_Recepcion>' , views.enlace_actualizar_ingresos_productos),
    path('logica_actualizar_ingresos_productos/' , views.logica_actualizar_ingresos_productos),

    path('enlace_registrar_usuarios/' , views.enlace_registrar_usuarios), 
    path('enlace_tabla_registro_usuario/' , views.enlace_tabla_registro_usuario), 
    path('logica_registrar_usuarios/' , views.logica_registrar_usuarios),
    path('enlace_tabla_registro_usuario/logica_eliminar_usuario/<Enumacion_Usuario>' , views.logica_eliminar_usuario),
    path('enlace_tabla_registro_usuario/enlace_actualizar_usuario/<Enumacion_Usuario>' , views.enlace_actualizar_usuario),
    path('logica_actualizar_usuario/' , views.logica_actualizar_usuario),

    path('enlace_registrar_trabajador/' , views.enlace_registrar_trabajador), 
    path('enlace_tabla_registro_trabajador/' , views.enlace_tabla_registro_trabajador), 
    path('logica_registrar_trabajador/' , views.logica_registrar_trabajador),
    path('enlace_tabla_registro_trabajador/logica_eliminar_trabajador/<Enumeracion_Trabajador>' , views.logica_eliminar_trabajador),
    path('enlace_tabla_registro_trabajador/enlace_actualizar_trabajador/<Enumeracion_Trabajador>' , views.enlace_actualizar_trabajador),
    path('logico_actualizar_trabajador/' , views.logica_actualizar_trabajador),

    path('enlace_registrar_asistencias/' , views.enlace_registrar_asistencias),
    path('enlace_tabla_registro_asistencias/' , views.enlace_tabla_registro_asistencias), 
    path('logica_registrar_asistecias/' , views.logica_registrar_asistecias),
    path('enlace_tabla_registro_asistencias/logica_eliminar_asistencias/<Enumeracion_Asistencias>' , views.logica_eliminar_asistencias),
    path('enlace_tabla_registro_asistencias/enlace_actualizar_asistencias/<Enumeracion_Asistencias>' , views.enlace_actualizar_asistencias),
    path('logica_actualizar_asistencias/' , views.logica_actualizar_asistencias), 

    path('enlace_dashborad_ventas/' , views.enlace_dashborad_ventas), 
    path('enlace_dashboard_ingresos_productos/' , views.enlace_dashboard_ingresos_productos), 
    
    # --- usuario
    path('enlace_panel_usuario/' , views.enlace_panel_usuario),
    path('enlace_tabla_compras_usuario/' , views.enlace_tabla_compras_usuario),
    path('enlace_registrar_compras_usuario/' , views.enlace_registrar_compras_usuario), 
    path('logica_regitrar_compras_usuario/' , views.logica_regitrar_compras_usuario), 
    path('enlace_tabla_compras_usuario/logica_eliminar_compras_usuario/<Id_Compras_Usuario>' , views.logica_eliminar_compras_usuario),
    path('enlace_tabla_compras_usuario/enlace_actualizar_compras_usuario/<Id_Compras_Usuario>' , views.enlace_actualizar_compras_usuario), 
    path('logica_actualizar_compras_usuario/' , views.logica_actualizar_compras_usuario),

    path('enlace_tabla_producto_disponible/' , views.enlace_tabla_producto_disponible),
    path('enlace_tabla_realizar_pedido_usuario/' , views.enlace_tabla_realizar_pedido_usuario),
    path('enlace_registrar_realizar_compras/' , views.enlace_registrar_realizar_compras),
    path('logica_tabla_registrar_pedido_usuario/' , views.logica_tabla_registrar_pedido_usuario),
    path('enlace_tabla_realizar_pedido_usuario/logica_eliminar_pedido_usuario/<Id_Realizar_Pedido>' , views.logica_eliminar_pedido_usuario),
    path('enlace_tabla_realizar_pedido_usuario/enlace_actualizar_pedido_usuario/<Id_Realizar_Pedido>' , views.enlace_actualizar_pedido_usuario),
    path('logica_actualizar_pedido_usuario/' , views.logica_actualizar_pedido_usuario)
]