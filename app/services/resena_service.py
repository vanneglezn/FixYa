from datetime import datetime


PALABRAS_OFENSIVAS = [
    "idiota",
    "estupido",
    "estúpido",
    "imbecil",
    "imbécil",
    "mierda",
    "weon",
    "weón",
    "ctm"
]


def detectar_lenguaje_ofensivo(comentario: str) -> bool:
    if not comentario:
        return False

    comentario_lower = comentario.lower()

    return any(
        palabra in comentario_lower
        for palabra in PALABRAS_OFENSIVAS
    )


def preparar_estado_resena(comentario: str):
    ofensiva = detectar_lenguaje_ofensivo(comentario)

    if ofensiva:
        return {
            "resena_activa": "N",
            "resena_reportada": "S",
            "motivo_reporte": "Lenguaje ofensivo detectado automáticamente",
            "fecha_reporte": datetime.utcnow(),
            "reporte_resuelto": "N"
        }

    return {
        "resena_activa": "S",
        "resena_reportada": "N",
        "motivo_reporte": None,
        "fecha_reporte": None,
        "reporte_resuelto": None
    }