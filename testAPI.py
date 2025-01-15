import unittest
import json
from app import app
from inventario import inventario

class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Establecer datos de prueba antes de ejecutar las pruebas"""
        # Definir el inventario inicial
        cls.inventario_inicial = {
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

    def setUp(self):
        """Restablecer el inventario al estado inicial antes de cada prueba"""
        inventario.clear()
        inventario.update(self.inventario_inicial)

    def test_consultar_producto_api(self):
        with app.test_client() as client:
            response = client.get("/producto/1")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), {"id": 1, "nombre": "Producto A", "cantidad": 100})

    def test_actualizar_stock_api(self):
        with app.test_client() as client:
            # Actualizar el stock
            response = client.put("/producto/1", json={"nueva_cantidad": 120})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), {"mensaje": "Stock actualizado correctamente."})

            # Verificar que la cantidad se actualizó correctamente
            response = client.get("/producto/1")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), {"id": 1, "nombre": "Producto A", "cantidad": 120})

    def test_actualizar_stock_producto_no_existente(self):
        with app.test_client() as client:
            # Intentar actualizar un producto que no existe
            response = client.put("/producto/999", json={"nueva_cantidad": 120})
            self.assertEqual(response.status_code, 404)
            self.assertEqual(json.loads(response.data), {"error": "Producto no encontrado."})

if __name__ == "__main__":
    unittest.main()
