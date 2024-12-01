## Requisitos

- Python 3
- pip

## Instalación

1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

1. Ejecuta el proyecto:
    ```bash
      uvicorn app.main:app --reload
    ```

## Pruebas

Para ejecutar las pruebas, usa el siguiente comando:
```bash
python -m pytest
```