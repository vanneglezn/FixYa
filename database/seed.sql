-- REGIONES

INSERT INTO region (id_region, nombre_region)
VALUES
(1, 'Biobío');


-- COMUNAS

INSERT INTO comuna (id_comuna, nombre_comuna, region_id_region)
VALUES
(11, 'Concepción', 1),
(12, 'Talcahuano', 1),
(13, 'San Pedro de la Paz', 1);


-- SERVICIOS

INSERT INTO servicio (
    id_servicio,
    nombre_servicio,
    descripcion_servicio,
    servicio_activo
)
VALUES
(1, 'Electricidad', 'Servicios eléctricos', true),
(2, 'Gasfitería', 'Reparaciones de agua y gas', true),
(3, 'Carpintería', 'Trabajos de madera', true),
(4, 'Cerrajería', 'Servicios de cerraduras', true);


-- USUARIO ADMIN

INSERT INTO usuario (
    rut,
    nombre_completo,
    fecha_nacimiento,
    genero,
    correo,
    telefono,
    contrasena,
    estado_usuario,
    comuna_id_comuna,
    tipo_usuario
)
VALUES (
    '11111111-1',
    'Administrador FixYa',
    '1990-01-01',
    'Masculino',
    'admin@fixya.cl',
    '999999999',
    '$2b$12$abcdefghijklmnopqrstuv',
    true,
    11,
    'ADMIN'
);


-- USUARIO CLIENTE

INSERT INTO usuario (
    rut,
    nombre_completo,
    fecha_nacimiento,
    genero,
    correo,
    telefono,
    contrasena,
    estado_usuario,
    comuna_id_comuna,
    tipo_usuario
)
VALUES (
    '22222222-2',
    'Cliente Demo',
    '1998-05-10',
    'Femenino',
    'cliente@fixya.cl',
    '988888888',
    '$2b$12$abcdefghijklmnopqrstuv',
    true,
    11,
    'CLIENTE'
);


-- USUARIO TÉCNICO

INSERT INTO usuario (
    rut,
    nombre_completo,
    fecha_nacimiento,
    genero,
    correo,
    telefono,
    contrasena,
    estado_usuario,
    comuna_id_comuna,
    tipo_usuario
)
VALUES (
    '12311111-1',
    'Técnico Demo',
    '1995-02-15',
    'Masculino',
    'tecnico@fixya.cl',
    '977777777',
    '$2b$12$abcdefghijklmnopqrstuv',
    true,
    11,
    'TECNICO'
);


-- TÉCNICO

INSERT INTO tecnico (
    usuario_rut,
    descripcion_perfil,
    experiencia_anios,
    nivel_tecnico,
    tecnico_verificado
)
VALUES (
    '12311111-1',
    'Especialista en instalaciones eléctricas',
    5,
    'Senior',
    true
);


-- TÉCNICO SERVICIO

INSERT INTO tecnico_servicio (
    tecnico_usuario_rut,
    servicio_id_servicio
)
VALUES (
    '12311111-1',
    1
);


-- TÉCNICO COMUNA

INSERT INTO tecnico_comuna (
    tecnico_usuario_rut,
    comuna_id_comuna
)
VALUES (
    '12311111-1',
    11
);