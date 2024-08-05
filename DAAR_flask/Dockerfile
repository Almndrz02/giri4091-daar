# imagen base de Python
FROM python:3.9-slim

# directorio de trabajo en /app
WORKDIR /app

# copia el archivo app.py al contenedor de trabajo
COPY app.py app.py

# instalcion de dependencias
RUN pip install flask requests

# exponer el puerto 5001
EXPOSE 5001

# comando para ejecutar la aplicación
CMD ["python", "app.py"]
