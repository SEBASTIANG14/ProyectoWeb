// Función para registrar un usuario en el localstorage
function registrarUsuario() {
    // Obtener los valores ingresados en los campos del formulario
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var correo = document.getElementById("correo").value;
    var contra = document.getElementById("contra").value;
    var contra2 = document.getElementById("contra2")
    var num = document.getElementById("num").value;
    var direccion = document.getElementById("direccion").value;
    
    // Verificar si el correo ya está registrado
    if (localStorage.getItem(correo)) {
      alert("El correo electrónico ya está registrado");
      return;
    }
    
    // Crear un objeto con la información del usuario
    var usuario = {
        nombre: nombre,
        apellido: apellido,
        correo: correo,
        Contra: contra,
        Contra2 : contra2,
        num: num,
        direccion: direccion
    };
    
    // Almacenar el objeto en el localstorage
    localStorage.setItem(correo, JSON.stringify(usuario));
    
    alert("Usuario registrado exitosamente");
}