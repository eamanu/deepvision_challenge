# Challenge Deep Vission - Ejecución


## Ejecución local

Primero creamos el venv e instalamos los modulos necesarios

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

```

Para ejecutar localmente el servicio se debe levantar flask de la siguiente manera:

```bash

$ export FLASK_APP=main.py
$ export FLASK_ENV=development
$ flask run
```


## Docker

Buildear:

```bash
docker build -t deep .
```

Luego ejecutar:

```bash
docker run -p 8080:80 deep
```

## Docekr compose

Para ejcutar con docker-compose ir a la carpeta `docker/compose/deepvision` y ejecutar:

```bash
docker-compose up --build app

```

## Uso del servicio

Pra obtener efemerides de un día determinado ejecutar:

```bash 
$ curl http://127.0.0.1:<PORT>/api/v1/efemerides?day=2019-7-9

{
  "2019-07-09": "D\u00eda de la Independencia [Independence Day]"
}
```


Para obtener efemerides de un mes determinado ejecutar:

```bash 
$ curl http://127.0.0.1:<PORT>/api/v1/efemerides?month=2019-7

{
  "Mes": 5, 
  "Dia: 1": "D\u00eda del Trabajo [Labour Day]", 
  "Dia: 25": "D\u00eda de la Revolucion de Mayo [May Revolution Day]"
}
```

**Nota:** Cambiar <PORT> por 5000 si se ejcuta localmente o 8080 si se ejecuta con Docker
