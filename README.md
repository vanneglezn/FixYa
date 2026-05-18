# FixYa Backend

Backend del proyecto FixYa desarrollado con FastAPI y PostgreSQL.

## Tecnologías utilizadas

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT
- ReportLab

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/vanneglezn/FixYa.git
```

---

## 2. Entrar al proyecto

```bash
cd backend
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

---

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Configurar base de datos

Crear archivo `.env`

Ejemplo:

```env
DATABASE_URL=postgresql://postgres:1234@localhost/fixya
SECRET_KEY=clave_secreta
```

---

# Ejecutar proyecto

```bash
uvicorn app.main:app --reload
```

---

# Swagger

Documentación disponible en:

```txt
http://127.0.0.1:8000/docs
```

---

# Estado actual

- Usuarios
- Técnicos
- Solicitudes
- Cotizaciones
- Generación PDF

Frontend responsive en desarrollo.
