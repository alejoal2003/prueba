# Estructura de datos para el inventario
inventario = {
    1: {"nombre": "Producto A", "cantidad": 100},
    2: {"nombre": "Producto B", "cantidad": 50},
    3: {"nombre": "Producto C", "cantidad": 75},
    4: {"nombre": "Producto D", "cantidad": 30},
    5: {"nombre": "Producto E", "cantidad": 60},
    6: {"nombre": "Producto F", "cantidad": 90},
    7: {"nombre": "Producto G", "cantidad": 20},
    8: {"nombre": "Producto H", "cantidad": 45},
    9: {"nombre": "Producto I", "cantidad": 80},
    10: {"nombre": "Producto J", "cantidad": 55}
}
# Función para consultar un producto
def consultar_producto(id_producto):
    try:
        id_producto = int(id_producto)
        if id_producto <= 0:
            return {"error": "El ID del producto debe ser un entero positivo."}
    except ValueError:
        return {"error": "El ID del producto debe ser un número entero."}
    
    producto = inventario.get(id_producto)
    if producto:
        return {"id": id_producto, "nombre": producto["nombre"], "cantidad": producto["cantidad"]}
    else:
        return {"error": "Producto no encontrado."}

# Función para agregar un producto
def agregar_producto(nombre_producto, cantidad):
    if not isinstance(nombre_producto, str) or not nombre_producto.strip():
        return {"error": "El nombre del producto debe ser una cadena no vacía."}
    
    if not isinstance(cantidad, int) or cantidad <= 0:
        return {"error": "La cantidad debe ser un número entero positivo."}

    # Buscar si el producto ya existe por nombre
    for id_producto, producto in inventario.items():
        if producto["nombre"].lower() == nombre_producto.lower():
            # Mostrar el valor actual de la cantidad
            print(f"Producto existente {producto['nombre']} con cantidad {producto['cantidad']}")
            inventario[id_producto]["cantidad"] += cantidad
            print(f"Producto actualizado {producto['nombre']} con nueva cantidad {inventario[id_producto]['cantidad']}")
            return {"mensaje": "Producto actualizado exitosamente."}
    
    # Si el producto no existe, agregar uno nuevo
    id_producto = len(inventario) + 1  # Generar un nuevo ID para el producto
    inventario[id_producto] = {"nombre": nombre_producto, "cantidad": cantidad}
    
    return {"mensaje": "Producto agregado exitosamente."}


def actualizar_stock(id_producto, nueva_cantidad):
    assert isinstance(id_producto, int) and id_producto > 0, "El ID del producto debe ser un entero positivo."
    assert isinstance(nueva_cantidad, int) and nueva_cantidad >= 0, "La nueva cantidad debe ser un entero no negativo."
    
    if id_producto in inventario:
        inventario[id_producto]["cantidad"] = nueva_cantidad
        return {"mensaje": "Stock actualizado correctamente."}
    else:
        return {"error": "Producto no encontrado."}
