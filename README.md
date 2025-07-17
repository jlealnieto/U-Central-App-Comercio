# Sistema de Gestión de Ventas e Inventario                                                                                                       

Sistema integral de gestión de ventas e inventario desarrollado para empresas que requieren un control eficiente de sus productos, clientes,
ventas y proveedores. Implementado con PostgreSQL como base de datos principal.

## Características Principales

### 🏪 Gestión de Productos
- Registro completo de productos con información detallada
- Control de stock en tiempo real
- Categorización por marcas y subcategorías
- Gestión de precios y disponibilidad
- Soporte para imágenes de referencia

### 💰 Sistema de Ventas
- Interfaz intuitiva para registro de ventas
- Selección de cantidades con botones + y -
- Integración automática con inventario
- Soporte para ventas de múltiples productos
- Actualización de stock en tiempo real

### 👥 Gestión de Clientes
- Registro completo de información del cliente
- Soporte para NIT y Cédula de Ciudadanía
- Información empresarial y de contacto
- Historial completo de compras por cliente

### 📊 Reportes y Análisis
- Reportes consolidados de ventas
- Historial detallado de compras por cliente
- Consulta de stock en tiempo real
- Análisis de productos más vendidos

### 🚚 Gestión de Proveedores
- Registro de compras a proveedores
- Control de costos de adquisición
- Filtrado por proveedores
- Gestión de inventario entrante

## Tecnologías Utilizadas



## Requisitos del Sistema

### Requisitos Mínimos


### Navegadores Compatibles


## Instalación y Configuración


## Estructura de la Base de Datos

### Tablas Principales

#### productos
- `id_producto` (SERIAL PRIMARY KEY)
- `nombre_producto` (VARCHAR(255) NOT NULL)
- `marca` (VARCHAR(100) NOT NULL)
- `subcategoria` (VARCHAR(100) NOT NULL)
- `stock_disponible` (INTEGER NOT NULL)
- `descripcion` (TEXT)
- `imagen_referencia` (VARCHAR(500))
- `precio` (DECIMAL(10,2) NOT NULL)
- `fecha_creacion` (TIMESTAMP DEFAULT NOW())
- `fecha_actualizacion` (TIMESTAMP DEFAULT NOW())

#### clientes
- `id_cliente` (SERIAL PRIMARY KEY)
- `nombre_cliente` (VARCHAR(255) NOT NULL)
- `nit_cedula` (VARCHAR(20) UNIQUE NOT NULL)
- `nombre_empresa` (VARCHAR(255))
- `direccion_empresa` (TEXT)
- `telefono` (VARCHAR(20))
- `correo_electronico` (VARCHAR(255))
- `fecha_registro` (TIMESTAMP DEFAULT NOW())

#### ventas
- `id_venta` (SERIAL PRIMARY KEY)
- `id_cliente` (INTEGER REFERENCES clientes(id_cliente))
- `id_usuario` (INTEGER REFERENCES usuarios(id_usuario))
- `fecha_venta` (TIMESTAMP DEFAULT NOW())
- `total_venta` (DECIMAL(10,2) NOT NULL)

#### detalle_ventas
- `id_detalle` (SERIAL PRIMARY KEY)
- `id_venta` (INTEGER REFERENCES ventas(id_venta))
- `id_producto` (INTEGER REFERENCES productos(id_producto))
- `cantidad` (INTEGER NOT NULL)
- `precio_unitario` (DECIMAL(10,2) NOT NULL)
- `precio_total` (DECIMAL(10,2) NOT NULL)

#### proveedores
- `id_proveedor` (SERIAL PRIMARY KEY)
- `nombre_proveedor` (VARCHAR(255) NOT NULL)
- `contacto` (VARCHAR(255))
- `telefono` (VARCHAR(20))
- `correo_electronico` (VARCHAR(255))

#### compras_proveedores
- `id_compra` (SERIAL PRIMARY KEY)
- `id_proveedor` (INTEGER REFERENCES proveedores(id_proveedor))
- `id_producto` (INTEGER REFERENCES productos(id_producto))
- `fecha_compra` (TIMESTAMP DEFAULT NOW())
- `cantidad_comprada` (INTEGER NOT NULL)
- `costo_unitario` (DECIMAL(10,2) NOT NULL)
- `costo_total` (DECIMAL(10,2) NOT NULL)

#### usuarios
- `id_usuario` (SERIAL PRIMARY KEY)
- `nombre_usuario` (VARCHAR(100) UNIQUE NOT NULL)
- `correo_electronico` (VARCHAR(255) UNIQUE NOT NULL)
- `password_hash` (VARCHAR(255) NOT NULL)
- `rol` (ENUM('administrador', 'vendedor') NOT NULL)
- `fecha_creacion` (TIMESTAMP DEFAULT NOW())

## Guía de Uso por Roles

### 👑 Administrador

#### Gestión de Productos
1. Acceder al módulo "Productos"
2. Hacer clic en "Nuevo Producto"
3. Completar todos los campos requeridos
4. Subir imagen de referencia (opcional)
5. Guardar producto

#### Gestión de Clientes
1. Ir a "Clientes" → "Nuevo Cliente"
2. Ingresar información completa del cliente
3. Validar NIT o Cédula de Ciudadanía
4. Guardar registro

#### Reportes de Ventas
1. Acceder a "Reportes" → "Ventas"
2. Seleccionar rango de fechas
3. Aplicar filtros según necesidad
4. Exportar reporte en PDF/Excel

#### Gestión de Proveedores
1. Ir a "Proveedores" → "Nueva Compra"
2. Seleccionar proveedor del filtro
3. Elegir productos y cantidades
4. Registrar costos de adquisición

### 🛒 Vendedor

#### Registro de Ventas
1. Acceder al módulo "Ventas"
2. Seleccionar cliente existente
3. Agregar productos usando botones + y -
4. Verificar stock disponible
5. Procesar venta

#### Consulta de Stock
1. Ir a "Inventario" → "Consultar Stock"
2. Ver tabla en tiempo real
3. Filtrar por producto o categoría
4. Verificar disponibilidad

## API Endpoints

### Autenticación
```
POST /api/auth/login
POST /api/auth/logout
POST /api/auth/refresh-token
```

### Productos
```
GET    /api/productos
POST   /api/productos
PUT    /api/productos/:id
DELETE /api/productos/:id
GET    /api/productos/stock
```

### Clientes
```
GET    /api/clientes
POST   /api/clientes
PUT    /api/clientes/:id
GET    /api/clientes/:id/historial
```

### Ventas
```
GET    /api/ventas
POST   /api/ventas
GET    /api/ventas/reportes
GET    /api/ventas/:id
```

### Proveedores
```
GET    /api/proveedores
POST   /api/proveedores
GET    /api/compras-proveedores
POST   /api/compras-proveedores
```

## Contribución al Proyecto

### Configuración del Entorno de Desarrollo

1. Fork del repositorio
2. Crear rama de feature: `git checkout -b feature/nueva-funcionalidad`
3. Realizar cambios y commits descriptivos
4. Ejecutar pruebas: `npm test`
5. Push a la rama: `git push origin feature/nueva-funcionalidad`
6. Crear Pull Request

### Estándares de Código

- **Idioma:** Todo el código, comentarios y documentación en español
- **Convención de nombres:** camelCase para variables, PascalCase para componentes
- **Commits:** Usar conventional commits en español

### Estructura de Commits
```
feat: agregar módulo de reportes avanzados
fix: corregir cálculo de inventario en tiempo real
docs: actualizar documentación de API
style: mejorar estilos de formulario de productos
```

## Licencia

Este proyecto está licenciado bajo la Licencia GNU3. Ver archivo [LICENSE](LICENSE) para más detalles.

## Soporte y Contacto

- **Documentación:** [Wiki del Proyecto](../../wiki)
- **Issues:** [Reportar Problemas](../../issues)
- **Discusiones:** [Foro de la Comunidad](../../discussions)

