import requests
import json

def GetAllProducts():
    url = 'https://fakestoreapi.com/products/' 
    respuesta = requests.get(url).json() 
    print('--------------------')
    print("Listado de productos")
    print('--------------------')
    print(json.dumps(respuesta, indent=4,ensure_ascii=False)) 
    print('--------------------')

def GetProduct():
    url_base = 'https://fakestoreapi.com/products'
    print("Búsqueda de producto")
    print('--------------------')


    try:
        # Solicitar el ID del producto al usuario
        product_id = input("Ingrese el ID del producto que desea consultar: ")
        
        # Enviar la solicitud GET para obtener los detalles del producto
        url = f"{url_base}/{product_id}"
        response = requests.get(url)
        
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            producto = response.json()
            print('--------------------')
            print("Detalles del producto")
            print('--------------------')
            print(json.dumps(producto, indent=4, ensure_ascii=False))
            print("-----------------------")
        else:
            print("Producto no encontrado")
    
    except requests.exceptions.JSONDecodeError as e:
        print("-----------------------")
        print(f"Producto no encontrado")
        print("-----------------------")
    
def AddProduct():
    url = 'https://fakestoreapi.com/products'
    print("Agregar producto")
    print('----------------')

    
    # Solicitar detalles del nuevo producto al usuario
    print('--------------------')
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
        print('-------------------------------')
        print("Producto agregado exitosamente!")
        print('-------------------------------')
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print('--------------------')
        print("Error al agregar el producto:", response.status_code)
        print('--------------------')

def UpdateProduct():
    url_base = 'https://fakestoreapi.com/products'
    print("Modificar producto")
    print('------------------')

        # Solicitar el ID del producto a modificar
    product_id = input("Ingrese el ID del producto que desea modificar: ")
        
        # Verificar si el producto existe
    url = f"{url_base}/{product_id}"
    check_response = requests.get(url)
    
    try:
        # Verificar si la respuesta no está vacía
        if check_response.status_code == 404 or not check_response.text:
            print('----------------------')
            print("El producto no existe.")
            print('----------------------')

            return
    except json.JSONDecodeError:
        return
    
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
    response = requests.put(url, json=producto_actualizado)
        
    if response.status_code == 200:
            print('--------------------')
            print("Producto modificado exitosamente!")
            print('--------------------')
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            print('--------------------')
    else:
            print('--------------------')
            print("Error al modificar el producto:", response.status_code)
            print('--------------------')


def DeleteProduct():
    url_base = 'https://fakestoreapi.com/products'
    print("Eliminación de producto")  
    print('-----------------------')
  
    
    # Solicitar el ID del producto a eliminar
    product_id = input("Ingrese el ID del producto que desea eliminar: ")
    url = f"{url_base}/{product_id}"
        
    try:
        # Verificar si el producto existe
        check_response = requests.get(url)
        if check_response.status_code == 404:
            print("El producto no existe, no se puede eliminar.")
            return
        
        # Enviar la solicitud DELETE
        if check_response.text:
            response = requests.delete(url)
        
        # Verificar el código de estado de la respuesta
        if response.status_code == 200 or response.status_code == 204:
            print('--------------------------------')
            print("Producto eliminado exitosamente!")
            print('--------------------------------')
        else:
            print('--------------------')
            print("Error al eliminar el producto:", check_response.status_code)
            print('--------------------')
    
    except requests.exceptions.RequestException as e:
        print('--------------------')
        print(f"Error de conexión: {e}")
        print('--------------------')
    except ValueError:
        print('--------------------')
        print("Error al procesar la respuesta del servidor.")
        print('--------------------')
    except Exception:
        print('----------------------')
        print(f"El producto no existe")
        print('----------------------')


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


