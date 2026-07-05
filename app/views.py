from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import bd_tabla_venta , bd_table_almacen , bd_tabla_asistencias , bd_tabla_trabajador , bd_tabla_usuario , Tabla_Compras_Usuario , Tabla_Producto_Disponible , Tabla_Realizar_Pedido

def login_usuario(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        contrasena = request.POST.get("contrasena")

        # Condicional 1: Administrador
        if usuario == "administrador" and contrasena == "administrador":
            return redirect("/panel_control/")  # cambia al nombre de tu URL de admin

        # Condicional 2: Usuario normal
        elif usuario == "usuario" and contrasena == "usuario":
            return redirect("/enlace_panel_usuario/")  # cambia al nombre de tu URL de usuario

        else:
            return render(request, "login_usuario.html", {
                "error": "Usuario o contraseña incorrectos"
            })

    return render(request, "login_usuario.html")

def panel_control(request): 
    return render(request , "panel_control.html")

def enlace_registrar_ventas(request): 
    return render(request , "registrar_ventas.html")

def enlace_tabla_registro_ventas(request): 
    ventas = bd_tabla_venta.objects.all()
    return render(request , "tabla_ventas.html" , {
        'ventas' : ventas
    })

def logica_registrar_ventas(request):
    Enumearcion = request.POST['txtEnumeracion']
    Nombre = request.POST['txtNombre']
    Categoria = request.POST['txtCategoria']
    Cantidad = request.POST['txtCantidad']
    Precio = request.POST['txtPrecio']
    Fecha = request.POST['txtFecha']

    ventas = bd_tabla_venta.objects.create(
        Enumearcion_Ventas = Enumearcion,
        Nombre_Ventas = Nombre,
        Categoria_ventas = Categoria,
        Cantidad_ventas = Cantidad,
        Precio_ventas = Precio,
        Fecha_ventas = Fecha
    )

    return redirect("/enlace_tabla_registro_ventas/")

def logica_eliminar_ventas(request , Enumearcion_Ventas):
    ventas = bd_tabla_venta.objects.get(Enumearcion_Ventas=Enumearcion_Ventas)
    ventas.delete()
    return redirect("/enlace_tabla_registro_ventas/")

def enlace_actualizar_ventas(request , Enumearcion_Ventas): 
    ventas = bd_tabla_venta.objects.get(Enumearcion_Ventas=Enumearcion_Ventas)
    return render(request , "actualizar_ventas.html" , {
        'actualizar_ventas' : ventas
    })

def logica_actualizar_ventas(request):
    Enumearcion_Ventas = request.POST['txtEnumeracion']
    Nombre_Ventas = request.POST['txtNombre']
    Categoria_ventas = request.POST['txtCategoria']
    Cantidad_ventas = request.POST['txtCantidad']
    Precio_ventas = request.POST['txtPrecio']
    Fecha_ventas = request.POST['txtFecha']

    ventas = bd_tabla_venta.objects.get(Enumearcion_Ventas = Enumearcion_Ventas)
    ventas.Nombre_Ventas = Nombre_Ventas
    ventas.Categoria_ventas = Categoria_ventas
    ventas.Cantidad_ventas = Cantidad_ventas
    ventas.Precio_ventas = Precio_ventas
    ventas.Fecha_ventas = Fecha_ventas

    ventas.save()

    return redirect("/enlace_tabla_registro_ventas/")

def enlace_registrar_ingresos_productos(request): 
    return render(request , "registrar_ingresos_productos.html")

def enlace_tabla_ingresos_productos(request): 
    almacen = bd_table_almacen.objects.all()
    return render(request , "tabla_ingresos_productos.html" , {
        'almacen' : almacen
    })

def logica_registrar_ingresos_productos(request): 
    numeracion = request.POST['txtEnumeracion']
    Empresa = request.POST['txtEmpresaEmision']
    Nombre = request.POST['txtNombreProducto']
    Cantidad = request.POST['txtCantidadProducto']
    Fecha = request.POST['txtFechaIngreso'] 

    almacen = bd_table_almacen.objects.create(
        Enumeracion_Recepcion = numeracion,
        Empresa_Emision = Empresa,
        Nombre_Producto = Nombre,
        Cantidad_Producto = Cantidad,
        Fecha_Producto = Fecha
    )
    return redirect('/enlace_tabla_ingresos_productos/')

def logica_eliminar_ingresos_prodcutos(request , Enumeracion_Recepcion):
    almacen = bd_table_almacen.objects.get(Enumeracion_Recepcion = Enumeracion_Recepcion) 
    almacen.delete()
    return redirect('/enlace_tabla_ingresos_productos/')

def enlace_actualizar_ingresos_productos(request , Enumeracion_Recepcion):
    almacen = bd_table_almacen.objects.get(Enumeracion_Recepcion = Enumeracion_Recepcion)
    return render(request , "actualizar_ingresos_productos.html" , {
        'actualizar_almacen' : almacen
    })

def logica_actualizar_ingresos_productos(request):
    Enumeracion_Recepcion = request.POST['txtEnumeracion']
    Empresa_Emision = request.POST['txtNombre']
    Nombre_Producto = request.POST['txtCategoria']
    Cantidad_Producto = request.POST['txtCantidad']
    Fecha_Producto = request.POST['txtFecha']

    almacen = bd_table_almacen.objects.get(Enumeracion_Recepcion = Enumeracion_Recepcion)
    almacen.Empresa_Emision = Empresa_Emision
    almacen.Nombre_Producto = Nombre_Producto
    almacen.Cantidad_Producto = Cantidad_Producto
    almacen.Fecha_Producto = Fecha_Producto 

    almacen.save()

    return redirect('/enlace_tabla_ingresos_productos/')

def enlace_registrar_usuarios(request):
    return render(request , "registrar_usuario.html")

def enlace_tabla_registro_usuario(request): 
    usuario = bd_tabla_usuario.objects.all()
    return render(request , "tabla_usuarios.html" , {
        'usuario' : usuario
    })

def logica_registrar_usuarios(request): 
    Enumacion = request.POST['txtEnumeracion']
    Nombre = request.POST['txtNombre']
    Contrasenia = request.POST['txtContrasenia']
    Correo = request.POST['txtCorreo']
    Telefono = request.POST['txtTelefono']
    Fecha = request.POST['txtFecha']

    usuario = bd_tabla_usuario.objects.create(
        Enumacion_Usuario = Enumacion,
        Nombre_Usuario = Nombre,
        Contrasenia_Usuario = Contrasenia,
        Correo_Usuario = Correo,
        Telefono_Usuario = Telefono,
        Fecha_Usuario = Fecha,
    )

    return redirect('/enlace_tabla_registro_usuario/')

def logica_eliminar_usuario(request , Enumacion_Usuario):
    usuario = bd_tabla_usuario.objects.get(Enumacion_Usuario = Enumacion_Usuario)
    usuario.delete()
    return redirect('/enlace_tabla_registro_usuario/')

def enlace_actualizar_usuario(request , Enumacion_Usuario):
    usuario = bd_tabla_usuario.objects.get(Enumacion_Usuario = Enumacion_Usuario)
    return render(request , "actualizar_usuario.html" , {
        'actualizar_usuario' : usuario
    })

def logica_actualizar_usuario(request): 
    Enumacion_Usuario = request.POST['txtEnumeracion']
    Nombre_Usuario = request.POST['txtNombre']
    Contrasenia_Usuario = request.POST['txtContrasenia']
    Correo_Usuario = request.POST['txtCorreo']
    Telefono_Usuario = request.POST['txtTelefono']
    Fecha_Usuario = request.POST['txtFecha']

    usuario = bd_tabla_usuario.objects.get(Enumacion_Usuario = Enumacion_Usuario)
    usuario.Nombre_Usuario = Nombre_Usuario
    usuario.Contrasenia_Usuario = Contrasenia_Usuario
    usuario.Correo_Usuario = Correo_Usuario
    usuario.Telefono_Usuario = Telefono_Usuario
    usuario.Fecha_Usuario = Fecha_Usuario

    usuario.save()

    return redirect('/enlace_tabla_registro_usuario/')

def enlace_tabla_registro_trabajador(request): 
    trabajador = bd_tabla_trabajador.objects.all()
    return render(request , "tabla_trabajador.html" , {
        'trabajador' : trabajador
    })

def enlace_registrar_trabajador(request): 
    return render(request , "registrar_trabajador.html")

def logica_registrar_trabajador(request): 
    Enumeracion = request.POST['txtEnumeracion']
    Nombre = request.POST['txtNombre']
    Apellido = request.POST['txtDni']
    Cargo = request.POST['txtCargo']
    Hora = request.POST['txtHora']
    Fecha = request.POST['txtFecha']
    
    trabajador = bd_tabla_trabajador.objects.create(
        Enumeracion_Trabajador = Enumeracion,
        Nombre_Trabajador = Nombre,
        Apellido_Trabajador = Apellido,
        Cargo_Trabajador = Cargo,
        Hora_Trabajador = Hora,
        Fecha_Trabajador = Fecha
    )

    return redirect('/enlace_tabla_registro_trabajador/')

def logica_eliminar_trabajador(request , Enumeracion_Trabajador):
    trabajador = bd_tabla_trabajador.objects.get(Enumeracion_Trabajador = Enumeracion_Trabajador)
    trabajador.delete()
    return redirect('/enlace_tabla_registro_trabajador/') 

def enlace_actualizar_trabajador(request , Enumeracion_Trabajador):
    trabajador = bd_tabla_trabajador.objects.get(Enumeracion_Trabajador = Enumeracion_Trabajador)
    return render(request , "actualizar_trabajador.html" , {
        'actualizar_trabajador' : trabajador
    })

def logica_actualizar_trabajador(request): 
    Enumeracion_Trabajador = request.POST['txtEnumeracion']
    Nombre_Trabajador = request.POST['txtNombre']
    Apellido_Trabajador = request.POST['txtDni']
    Cargo_Trabajador = request.POST['txtCargo']
    Hora_Trabajador = request.POST['txtHora']
    Fecha_Trabajador = request.POST['txtFecha']

    trabajador = bd_tabla_trabajador.objects.get(Enumeracion_Trabajador = Enumeracion_Trabajador)
    trabajador.Nombre_Trabajador = Nombre_Trabajador
    trabajador.Apellido_Trabajador = Apellido_Trabajador
    trabajador.Cargo_Trabajador = Cargo_Trabajador
    trabajador.Hora_Trabajador = Hora_Trabajador
    trabajador.Fecha_Trabajador = Fecha_Trabajador
    
    trabajador.save()

    return redirect('/enlace_tabla_registro_trabajador/')

def enlace_tabla_registro_asistencias(request): 
    asistencia = bd_tabla_asistencias.objects.all()
    return render(request , "tabla_registro_asistencias.html" , {
        'asistencias' : asistencia
    })

def enlace_registrar_asistencias(request): 
    return render(request , 'registrar_asistencias.html')

def logica_registrar_asistecias(request): 
    Enumeracion = request.POST['txtEnumeracion']
    Nombre = request.POST['txtNombre']
    Hora_Inicio = request.POST['txtHoraInicio']
    Hora_Final = request.POST['txtHoraFinal']
    Fecha = request.POST['txtFecha']
    Comentario = request.POST['txtComentario']

    asistencias = bd_tabla_asistencias.objects.create(
        Enumeracion_Asistencias = Enumeracion,
        Nombre_Asistencias = Nombre,
        Hora_Inicio_Asistencias = Hora_Inicio,
        Hora_Final_Asistencias = Hora_Final,
        Fecha_Asistencias = Fecha,
        Comentario_Asistencias = Comentario
    )
    
    return redirect('/enlace_tabla_registro_asistencias/')

def logica_eliminar_asistencias(request , Enumeracion_Asistencias):
    asistencias = bd_tabla_asistencias.objects.get(Enumeracion_Asistencias = Enumeracion_Asistencias)
    asistencias.delete()
    return redirect('/enlace_tabla_registro_asistencias/')

def enlace_actualizar_asistencias(request , Enumeracion_Asistencias):
    asistencias = bd_tabla_asistencias.objects.get(Enumeracion_Asistencias = Enumeracion_Asistencias)
    return render(request , 'actualizar_asistencias.html' , {
        'actualizar_asistencias' : asistencias
    })

def logica_actualizar_asistencias(request): 
    Enumeracion_Asistencias = request.POST['txtEnumeracion']
    Nombre_Asistencias = request.POST['txtNombre']
    Hora_Inicio_Asistencias = request.POST['txtHoraInicio']
    Hora_Final_Asistencias = request.POST['txtHoraFinal']
    Fecha_Asistencias = request.POST['txtFecha']
    Comentario_Asistencias = request.POST['txtComentario']

    asistencias = bd_tabla_asistencias.objects.get(Enumeracion_Asistencias = Enumeracion_Asistencias)
    asistencias.Nombre_Asistencias = Nombre_Asistencias
    asistencias.Hora_Inicio_Asistencias = Hora_Inicio_Asistencias
    asistencias.Hora_Final_Asistencias = Hora_Final_Asistencias
    asistencias.Fecha_Asistencias = Fecha_Asistencias
    asistencias.Comentario_Asistencias = Comentario_Asistencias

    asistencias.save()

    return redirect('/enlace_tabla_registro_asistencias/')


def enlace_dashborad_ventas(request): 
    return render(request , 'dashboard_ventas.html')

def enlace_dashboard_ingresos_productos(request):
    return render(request , 'dashboard_ingresos_productos.html')

# usuario

def enlace_panel_usuario(request): 
    return render(request , 'panel_usuario.html')

def enlace_tabla_compras_usuario(request): 
    compras_usuario = Tabla_Compras_Usuario.objects.all()
    return render(request , 'tabla_compras_usuario.html' , {
        'compras_usuario' : compras_usuario
    })

def enlace_registrar_compras_usuario(request):
    return render(request , 'registrar_compras_usuario.html')

def logica_regitrar_compras_usuario(request):
    Id = request.POST['TxtId']
    Nombre = request.POST['TxtNombre']
    Cantidad = request.POST['TxtCantidad']
    Precios = request.POST['TxtPrecios']
    Fecha = request.POST['TxtFecha']
    Hora = request.POST['TxtHora']

    usuario = Tabla_Compras_Usuario.objects.create(
        Id_Compras_Usuario = Id,
        Nombre_Compras_Usuario = Nombre,
        Cantidad_Compras_Usuario = Cantidad,
        Precios_Compras_Usuario = Precios,
        Fecha_Compras_Usuario = Fecha,
        Hora_compras_Usuario = Hora,
    )
    
    return redirect('/enlace_tabla_compras_usuario/')

def logica_eliminar_compras_usuario(request , Id_Compras_Usuario):
    usuario = Tabla_Compras_Usuario.objects.get(Id_Compras_Usuario = Id_Compras_Usuario)
    usuario.delete()
    return redirect('/enlace_tabla_compras_usuario/')

def enlace_actualizar_compras_usuario(request , Id_Compras_Usuario): 
    usuario = Tabla_Compras_Usuario.objects.get(Id_Compras_Usuario = Id_Compras_Usuario)
    return render(request , 'actualizar_compras_usuario.html' , {
        'usuario' : usuario
    })

def logica_actualizar_compras_usuario(request):
    Id_Compras_Usuario = request.POST['TxtId']
    Nombre_Compras_Usuario = request.POST['TxtNombre']
    Cantidad_Compras_Usuario = request.POST['TxtCantidad']
    Precios_Compras_Usuario = request.POST['TxtPrecios']
    Fecha_Compras_Usuario = request.POST['TxtFecha']
    Hora_compras_Usuario = request.POST['TxtHora']

    usuario = Tabla_Compras_Usuario.objects.get(Id_Compras_Usuario = Id_Compras_Usuario)
    usuario.Nombre_Compras_Usuario = Nombre_Compras_Usuario
    usuario.Cantidad_Compras_Usuario = Cantidad_Compras_Usuario
    usuario.Precios_Compras_Usuario = Precios_Compras_Usuario
    usuario.Fecha_Compras_Usuario = Fecha_Compras_Usuario
    usuario.Hora_compras_Usuario = Hora_compras_Usuario

    usuario.save()

    return redirect('/enlace_tabla_compras_usuario/')

def enlace_tabla_producto_disponible(request): 
    producto_disponible = Tabla_Producto_Disponible.objects.all()
    return render(request , 'tabla_producto_disponible.html' , {
        'producto_disponible' : producto_disponible
    })

# -----------------------------------------------
def enlace_tabla_realizar_pedido_usuario(request): 
    return render(request , 'enlace_tabla_realizar_pedido_usuario.html')

# -----------------------------------------------

def enlace_tabla_realizar_pedido_usuario(request):
    realizar_pedido_usuario = Tabla_Realizar_Pedido.objects.all()
    return render(request , 'tabla_realizar_pedido_usuario.html' , {
        'realizar_pedido_usuario' : realizar_pedido_usuario
    })

def enlace_registrar_realizar_compras(request):
    return render(request , 'registrar_realizar_compras.html')

def logica_tabla_registrar_pedido_usuario(request):
    Id = request.POST['TxtId']
    Nombre = request.POST['TxtNombreDistrito']
    Dirrecion = request.POST['TxtUbicacionExacta']
    Fecha = request.POST['TxtCantidad']
    Hora = request.POST['TxtPrecios']
    Metodo_Pago = request.POST['TxtFecha']
    Observacion = request.POST['TxtHora']

    pedido_usario = Tabla_Realizar_Pedido.objects.create(
        Id_Realizar_Pedido = Id,
        Nombre_Realizar_Pedido = Nombre,
        Dirrecion_Realizar_Pedido = Dirrecion,
        Fecha_Realizar_Pedido = Fecha,
        Hora_Realizar_Pedido = Hora,
        Metodo_Pago_Realizar_Pedido = Metodo_Pago,
        Observacion_Realizar_Pedido = Observacion,
    )

    return redirect('/enlace_tabla_realizar_pedido_usuario/')

def logica_eliminar_pedido_usuario(request , Id_Realizar_Pedido): 
    realizar_pedido = Tabla_Realizar_Pedido.objects.get(Id_Realizar_Pedido = Id_Realizar_Pedido)
    realizar_pedido.delete()
    return redirect('/enlace_tabla_realizar_pedido_usuario/')

def enlace_actualizar_pedido_usuario(request , Id_Realizar_Pedido):
    realizar_pedido  = Tabla_Realizar_Pedido.objects.get(Id_Realizar_Pedido = Id_Realizar_Pedido)
    return render(request , 'actualizar_realizar_compras.html' , {
        'realizar_pedido' : realizar_pedido
    })

def logica_actualizar_pedido_usuario(request): 
    Id_Realizar_Pedido = request.POST['TxtId']
    Nombre_Realizar_Pedido = request.POST['TxtNombreDistrito']
    Dirrecion_Realizar_Pedido = request.POST['TxtUbicacionExacta']
    Fecha_Realizar_Pedido = request.POST['TxtCantidad']
    Hora_Realizar_Pedido = request.POST['TxtPrecios']
    Metodo_Pago_Realizar_Pedido = request.POST['TxtFecha']
    Observacion_Realizar_Pedido = request.POST['TxtHora']

    realizar_pedido = Tabla_Realizar_Pedido.objects.get(Id_Realizar_Pedido = Id_Realizar_Pedido)
    realizar_pedido.Nombre_Realizar_Pedido = Nombre_Realizar_Pedido
    realizar_pedido.Dirrecion_Realizar_Pedido = Dirrecion_Realizar_Pedido
    realizar_pedido.Fecha_Realizar_Pedido = Fecha_Realizar_Pedido
    realizar_pedido.Hora_Realizar_Pedido = Hora_Realizar_Pedido
    realizar_pedido.Metodo_Pago_Realizar_Pedido = Metodo_Pago_Realizar_Pedido
    realizar_pedido.Observacion_Realizar_Pedido = Observacion_Realizar_Pedido

    realizar_pedido.save()

    return redirect('/enlace_tabla_realizar_pedido_usuario/')


