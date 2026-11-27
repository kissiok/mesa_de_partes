-- =====================================================================
--  Base de datos del prototipo de mesa de partes digital
--  Expedientes de licencias de funcionamiento - Municipalidad Distrital de Chorrillos
--  Ejecutar completo en MySQL Workbench (botón del rayo)
-- =====================================================================

CREATE DATABASE IF NOT EXISTS mesa_partes_digital
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_spanish_ci;

USE mesa_partes_digital;

CREATE TABLE IF NOT EXISTS expediente (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    codigo         VARCHAR(15)  NOT NULL UNIQUE,
    documento      VARCHAR(11)  NOT NULL,
    razon_social   VARCHAR(150) NOT NULL,
    tramite        VARCHAR(30)  NOT NULL,
    giro           VARCHAR(100) NOT NULL,
    riesgo         ENUM('BAJO','MEDIO','ALTO','MUY ALTO') NOT NULL,
    fecha_ingreso  DATE         NOT NULL,
    folios         INT          NOT NULL,
    estado         ENUM('RECIBIDO','EN EVALUACION','OBSERVADO','APROBADO','DENEGADO','ARCHIVADO')
                   NOT NULL DEFAULT 'RECIBIDO',
    ubicacion      VARCHAR(40)  NOT NULL DEFAULT 'SIN ARCHIVAR',
    CONSTRAINT chk_documento CHECK (CHAR_LENGTH(documento) IN (8, 11)),
    CONSTRAINT chk_folios CHECK (folios > 0)
) ENGINE=InnoDB;

-- Consulta para revisar los expedientes registrados desde el programa
SELECT codigo, razon_social, tramite, fecha_ingreso, folios, estado, ubicacion
FROM expediente
ORDER BY codigo;
