-- MI RESPUESTA A LA PREGUNTA 7 --
-- CONSULTA PARA LA OBTENCION DE PERMISO DE USUARIO.

-- DECLARAMOS NUESTRA VARIABLE DE USUARIO DE CONSULTA
DECLARE @userId NCHAR(32)
SET @userId = '6f1ef7f45a9c420ca68ea226c099c4b5'

-- REALIZAMOS NUESTA PETICION A LA BASE DE DATOS OBTENIENDO SOLO PERMISOS Y USUARIO COMO TABLA FINAL
SELECT
    dbo.Permission.*,
    dbo.User.*
From
    (
        (
            dbo.Permission
            INNER JOIN dbo.RolePermission ON dbo.Permission.id = dbo.RolePermission.permissionId
        )
        INNER JOIN dbo.UserRol ON dbo.UserRol.roleId = dbo.RolePermission.roleId
    )
WHERE
    -- REALIZAMOS UN FILTRO FINAL PARA SOLO OBTENER LOS PERMISOS DEL USUARIO.
    dbo.User.userId = @userId

-- MI RESPUESTA A LA PREGUNTA 8 --
--CONSULTA PARA OBTENER LOS USUARIOS CUYO PERMISO TENGA EL NOMBRE DE '/catalogs'.


-- DECLARAMOS NUESTRA VARIABLE DE USUARIO DE CONSULTA
DECLARE @userId NCHAR(32)
SET @userId = '6f1ef7f45a9c420ca68ea226c099c4b5'

-- REALIZAMOS NUESTA PETICION A LA BASE DE DATOS OBTENIENDO SOLO PERMISOS Y USUARIO COMO TABLA FINAL
SELECT
    dbo.Permission.*,
    dbo.User.*
From
    (
        (
            dbo.Permission
            INNER JOIN dbo.RolePermission ON dbo.Permission.id = dbo.RolePermission.permissionId
        )
        INNER JOIN dbo.UserRol ON dbo.UserRol.roleId = dbo.RolePermission.roleId
    )
WHERE
    -- FILTRAMOS POR USUARIO Y UTILIZAMOS EL OPERADOR LIKE PARA BUSCAR EN LOS PERMISOS QUE INICIEN CON '/catalogs'.
    dbo.User.userId = @userId AND dbo.Permission.name LIKE '/catalogs%'


