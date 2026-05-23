````md
# FixYa Backend

Backend del proyecto **FixYa** desarrollado con **FastAPI** y **PostgreSQL**.

---

# Tecnologías utilizadas

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Docker
- Docker Compose
- ReportLab

---

# Instalación del proyecto

## 1. Clonar repositorio

```bash
git clone https://github.com/vanneglezn/FixYa.git
```

---

## 2. Entrar al proyecto

```bash
cd FixYa/backend
```

---

## 3. Crear entorno virtual

```bash
python -m venv venv
```

---

## 4. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Configuración de variables de entorno

Crear archivo `.env`

Ejemplo:

```env
DATABASE_URL=postgresql://postgres:1234@localhost/fixya
SECRET_KEY=clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Ejecutar proyecto localmente

```bash
uvicorn app.main:app --reload
```

---

# Ejecutar proyecto con Docker

## Levantar contenedores

```bash
docker compose up --build
```

---

## Detener contenedores

```bash
docker compose down
```

---

# Contenedores utilizados

- `fixya_backend`
  - API FastAPI

- `fixya_postgres`
  - Base de datos PostgreSQL

---

# Documentación Swagger

Disponible en:

```txt
http://127.0.0.1:8000/docs
```

o

```txt
http://localhost:8000/docs
```

---

# Funcionalidades implementadas

- Gestión de usuarios
- Autenticación JWT
- Roles de usuario
  - ADMIN
  - CLIENTE
  - TECNICO
- Gestión de técnicos
- Marketplace de técnicos
- Solicitudes de servicios
- Asignación de técnicos
- Gestión de estados de solicitudes
- Dashboard administrador
- Dashboard técnico
- Dashboard cliente
- Cotizaciones
- Reseñas y ratings
- Notificaciones
- Generación de PDF
- Subida de archivos

---

# Estado actual del proyecto

Backend funcional y conectado a PostgreSQL.

Frontend responsive en desarrollo con React.
````
