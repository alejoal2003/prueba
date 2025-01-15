import unittest
from inventario import consultar_producto, agregar_producto, actualizar_stock, inventario

class TestInventario(unittest.TestCase):
    
    def setUp(self):
        # Reiniciar el inventario antes de cada prueba
        inventario.clear()
        inventario.update({
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
        })


    def test_consultar_producto_existente(self):
        resultado = consultar_producto(1)
        self.assertEqual(resultado, {"id": 1, "nombre": "Producto A", "cantidad": 100})

    def test_consultar_producto_no_existente(self):
        resultado = consultar_producto(999)
        self.assertEqual(resultado, {"error": "Producto no encontrado."})

    def test_consultar_producto_id_no_valido(self):
        resultado = consultar_producto("abc")
        self.assertEqual(resultado, {"error": "El ID del producto debe ser un número entero."})

    def test_agregar_producto(self):
        resultado = agregar_producto("Producto Z", 40)
        self.assertEqual(resultado, {"mensaje": "Producto agregado exitosamente."})
        producto = consultar_producto(11)  # Producto recién agregado
        self.assertEqual(producto, {"id": 11, "nombre": "Producto Z", "cantidad": 40})

    def test_agregar_producto_existente(self):
        resultado = agregar_producto("Producto A", 20)
        self.assertEqual(resultado, {"mensaje": "Producto actualizado exitosamente."})
        producto = consultar_producto(1)  # Producto A actualizado
        self.assertEqual(producto, {"id": 1, "nombre": "Producto A", "cantidad": 120})

    def test_actualizar_stock(self):
        resultado = actualizar_stock(1, 50)
        self.assertEqual(resultado, {"mensaje": "Stock actualizado correctamente."})
        producto = consultar_producto(1)
        self.assertEqual(producto, {"id": 1, "nombre": "Producto A", "cantidad": 50})

    def test_actualizar_stock_producto_no_existente(self):
        resultado = actualizar_stock(999, 50)
        self.assertEqual(resultado, {"error": "Producto no encontrado."})

    def test_actualizar_stock_cantidad_invalida(self):
        with self.assertRaises(AssertionError):
            actualizar_stock(1, -10)

if __name__ == "__main__":
    unittest.main()
