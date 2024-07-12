import requests
import json

def GetAllProducts():
    url = 'https://fakestoreapi.com/products/' 
    respuesta = requests.get(url).json() 
    print("Listado de productos")
    print('--------------------')
    print(json.dumps(respuesta, indent=4,ensure_ascii=False)) 


def GetProduct():
    url_base = 'https://fakestoreapi.com/products'
    print("Búsqueda de producto")
    
    # Solicitar el ID del producto al usuario
    product_id = input("Ingrese el ID del producto que desea consultar: ")
    
    # Enviar la solicitud GET para obtener los detalles del producto
    url = f"{url_base}/{product_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        producto = response.json()
        print("Detalles del producto")
        print('--------------------')
        print(json.dumps(producto, indent=4, ensure_ascii=False))
    else:
        print("Error al obtener el producto:", response.status_code)

    
def AddProduct():
    url = 'https://fakestoreapi.com/products'
    print("Agregar producto")
    
    # Solicitar detalles del nuevo producto al usuario
    title = input("Ingrese el título del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    description = input("Ingrese la descripción del producto: ")
    image = input("Ingrese la URL de la imagen del producto: ")
    category = input("Ingrese la categoría del producto: ")
    
    # Crear un diccionario con los datos del nuevo producto
    nuevo_producto = {
        'title': title,
        'price': price,
        'description': description,
        'image': image,
        'category': category
    }
    
    # Enviar la solicitud POST con los datos del nuevo producto
    response = requests.post(url, json=nuevo_producto)
    
    if response.status_code == 200 or response.status_code == 201:
        print("Producto agregado exitosamente!")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print("Error al agregar el producto:", response.status_code)

def UpdateProduct():
    url_base = 'https://fakestoreapi.com/products'
    print("Modificar producto")
    
    # Solicitar el ID del producto a modificar
    product_id = input("Ingrese el ID del producto que desea modificar: ")
    
    # Solicitar los nuevos detalles del producto al usuario
    title = input("Ingrese el nuevo título del producto: ")
    price = float(input("Ingrese el nuevo precio del producto: "))
    description = input("Ingrese la nueva descripción del producto: ")
    image = input("Ingrese la nueva URL de la imagen del producto: ")
    category = input("Ingrese la nueva categoría del producto: ")
    
    # Crear un diccionario con los datos actualizados del producto
    producto_actualizado = {
        'title': title,
        'price': price,
        'description': description,
        'image': image,
        'category': category
    }
    
    # Enviar la solicitud PUT con los datos actualizados del producto
    url = f"{url_base}/{product_id}"
    response = requests.put(url, json=producto_actualizado)
    
    if response.status_code == 200:
        print("Producto modificado exitosamente!")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print("Error al modificar el producto:", response.status_code)  


def DeleteProduct():
    url_base = 'https://fakestoreapi.com/products'
    print("Eliminación de producto")
    
    # Solicitar el ID del producto a eliminar
    product_id = input("Ingrese el ID del producto que desea eliminar: ")
    
    # Enviar la solicitud DELETE
    url = f"{url_base}/{product_id}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        print("Producto eliminado exitosamente!")
    else:
        print("Error al eliminar el producto:", response.status_code)


def mostrar_menu():
    print("\nAdministración de Productos:")
    print("1. Consultar todos los productos")
    print("2. Consultar un producto en específico")
    print("3. Agregar un nuevo producto")
    print("4. Modificar producto en específico")
    print("5. Eliminar un producto")
    print("6. Salir")


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == '1':
        GetAllProducts()
    elif opcion == '2':
        GetProduct()
    elif opcion == '3':
        AddProduct()
    elif opcion == '4':
        UpdateProduct()    
    elif opcion == '5':
        DeleteProduct()
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")
