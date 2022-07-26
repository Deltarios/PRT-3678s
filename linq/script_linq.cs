var users = List<User>();
var roles = List<Role>();
var userRoles = List<UserRole>();
var permissions = List<Permission>();
var rolePermissions = List<RolePermission>();

var userId = "6f1ef7f45a9c420ca68ea226c099c4b5";
var rolesForUser = (for u in users
                     for ur in userRoles.Where(ur => ur.userId == u.userId && u.userId == userId)
	 for r in roles.Where(r => r.roleId == ur.roleId)
	 select r).ToList();


/** MI RESPUESTA A LA PREGUNTA 9
Se crea variable para almacenar la consulta para obtener los permisos de usuario activo.
**/
var permissionForUser = (for u in users
                     for ur in userRoles.Where(ur => ur.userId == u.userId && u.userId == userId)
	 for r in roles.Where(r => r.roleId == ur.roleId)
     for rp in rolePermissions.Where(rp => rp.roleId == r.roleId)
     for p in permissions.Where(p => p.permissionId == rp.permissionId && rp.isEnabled == true)
	 select p).ToList();


/** MI RESPUESTA A LA PREGUNTA 10
Se crea variable para almacenar los permision de usuario que contengan '/catalogs'
**/
var permissionForUser = (for u in users
                     for ur in userRoles.Where(ur => ur.userId == u.userId && u.userId == userId)
	 for r in roles.Where(r => r.roleId == ur.roleId)
     for rp in rolePermissions.Where(rp => rp.roleId == r.roleId)
     for p in permissions.Where(p => p.permissionId == rp.permissionId && rp.isEnabled == true && p.name.StartsWith('/catalogs'))
	 select p).ToList();
