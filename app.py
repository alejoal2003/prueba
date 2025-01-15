from flask import Flask, request, jsonify
from inventario import consultar_producto, agregar_producto, actualizar_stock
app = Flask(__name__)

# Endpoint para consultar un producto
@app.route("/producto/<id_producto>", methods=["GET"])
def api_consultar_producto(id_producto):
    # Verificar si el parámetro es un número entero positivo (antes de convertirlo)
    if not id_producto.isdigit() or int(id_producto) <= 0:
        return jsonify({"error": "El ID del producto debe ser un número entero positivo."}), 400
    
    # Convertir a entero después de pasar la validación
    id_producto = int(id_producto)
    resultado = consultar_producto(id_producto)
    
    if "error" in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado), 200


# Endpoint para agregar un producto
@app.route("/producto", methods=["POST"])
def api_agregar_producto():
    data = request.get_json()
    nombre_producto = data.get('nombre')
    cantidad = data.get('cantidad')
    
    # Validaciones
    if not isinstance(nombre_producto, str) or not nombre_producto.strip():
        return jsonify({"error": "El nombre del producto debe ser una cadena no vacía."}), 400
    
    if not isinstance(cantidad, int) or cantidad <= 0:
        return jsonify({"error": "La cantidad debe ser un número entero positivo."}), 400
    
    resultado = agregar_producto(nombre_producto, cantidad)
    if "error" in resultado:
        return jsonify(resultado), 404
    return jsonify(resultado), 200

# Endpoint para actualizar el stock
@app.route("/producto/<int:id_producto>", methods=["PUT"])
def api_actualizar_stock(id_producto):
    try:
        datos = request.get_json()
        nueva_cantidad = datos.get("nueva_cantidad")
        
        # Validaciones
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            return jsonify({"error": "La nueva cantidad debe ser un número entero no negativo."}), 400
        
        # Llamar a la función de actualización del stock
        resultado = actualizar_stock(id_producto, nueva_cantidad)
        
        # Verificar si hubo un error en la actualización
        if "error" in resultado:
            return jsonify(resultado), 404  # Si el producto no existe, devolver 404

        return jsonify(resultado), 200  # Si la actualización es exitosa, devolver 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    
if __name__ == "__main__":
    app.run(debug=True)
