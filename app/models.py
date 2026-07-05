from django.db import models

class bd_tabla_venta(models.Model): 
    Enumearcion_Ventas = models.CharField(max_length=250)
    Nombre_Ventas = models.CharField(max_length=50)
    Categoria_ventas = models.CharField(max_length=50)
    Cantidad_ventas = models.IntegerField()
    Precio_ventas = models.CharField(max_length=50)
    Fecha_ventas = models.DateField()

    def __str__(self):
        return f"ID : {self.Enumearcion_Ventas} - Nombre : {self.Nombre_Ventas}"
    
class bd_table_almacen(models.Model):
    Enumeracion_Recepcion = models.CharField(max_length=250)
    Empresa_Emision = models.CharField(max_length=250)
    Nombre_Producto = models.CharField(max_length=250)
    Cantidad_Producto = models.IntegerField()
    Fecha_Producto = models.DateField()

    def __str__(self):
        return f"ID : {self.Enumeracion_Recepcion} - Nombre : {self.Empresa_Emision}"

class bd_tabla_usuario(models.Model):
    Enumacion_Usuario = models.CharField(max_length=250)
    Nombre_Usuario = models.CharField(max_length=250)
    Contrasenia_Usuario = models.CharField(max_length=250)
    Correo_Usuario = models.CharField(max_length=250)
    Telefono_Usuario = models.CharField(max_length=250)
    Fecha_Usuario = models.DateField()

    def __str__(self):
        return f"ID : {self.Enumacion_Usuario} - Nombre : {self.Nombre_Usuario}"
    
class bd_tabla_trabajador(models.Model): 
    Enumeracion_Trabajador = models.CharField(max_length=250)
    Nombre_Trabajador = models.CharField(max_length=250)
    Apellido_Trabajador = models.CharField(max_length=250)
    Cargo_Trabajador = models.CharField(max_length=250)
    Hora_Trabajador = models.IntegerField()
    Fecha_Trabajador = models.DateField()

    def __str__(self):
        return f"ID : {self.Enumeracion_Trabajador} - Nombre : {self.Nombre_Trabajador}"
    
class bd_tabla_asistencias(models.Model): 
    Enumeracion_Asistencias = models.CharField(max_length=250)
    Nombre_Asistencias = models.CharField(max_length=250)
    Hora_Inicio_Asistencias = models.TimeField()
    Hora_Final_Asistencias = models.TimeField()
    Fecha_Asistencias = models.DateField()
    Comentario_Asistencias = models.CharField()

    def __str__(self):
        return f"ID : {self.Enumeracion_Asistencias} - Nombre : {self.Nombre_Asistencias}"

# ------------------------------------------------------------------------------------------

class Tabla_Compras_Usuario(models.Model):
    Id_Compras_Usuario = models.CharField(max_length=250)
    Nombre_Compras_Usuario = models.CharField(max_length=250)
    Cantidad_Compras_Usuario = models.IntegerField()
    Precios_Compras_Usuario = models.CharField()
    Fecha_Compras_Usuario = models.DateField()
    Hora_compras_Usuario = models.TimeField()

    def __str__(self):
        return f"ID : {self.Id_Compras_Usuario} - Nombre : {self.Nombre_Compras_Usuario}"
    
class Tabla_Producto_Disponible(models.Model): 
    Id_Producto_Disponible = models.CharField(max_length=250)
    Nombre_Producto_Disponible = models.CharField(max_length=250)
    Categoria_Producto_Disponible = models.CharField(max_length=250)
    Precio_Producto_Disponible = models.CharField(max_length=250)
    Stock_Producto_Disponible = models.CharField(max_length=250)
    Estado_Producto_Disponible = models.CharField(max_length=250)

    def __str__(self):
        return f"ID : {self.Id_Producto_Disponible} - Nombre : {self.Nombre_Producto_Disponible}"
    
class Tabla_Realizar_Pedido(models.Model):
    Id_Realizar_Pedido = models.CharField(max_length=250)
    Nombre_Realizar_Pedido = models.CharField(max_length=250)
    Dirrecion_Realizar_Pedido = models.CharField(max_length=250)
    Fecha_Realizar_Pedido = models.DateField()
    Hora_Realizar_Pedido = models.TimeField()
    Metodo_Pago_Realizar_Pedido = models.CharField(max_length=250)
    Observacion_Realizar_Pedido = models.CharField(max_length=250)

    def __str__(self):
        return f"ID : {self.Id_Realizar_Pedido} - Nombre : {self.Nombre_Realizar_Pedido}"