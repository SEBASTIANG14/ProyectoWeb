// Función para iniciar sesión
function iniciarSesion() {
    // Obtener los valores ingresados en los campos del formulario
    var correo = document.getElementById("correoIniciar").value;
    var contraseña = document.getElementById("contraseñaIniciar").value;
    
    // Obtener el objeto del usuario desde el localstorage
    var usuario = JSON.parse(localStorage.getItem(correo));
    
    // Verificar si el usuario existe y la contraseña es correcta
    if (usuario && usuario.contraseña === contraseña) {
      alert("Inicio de sesión exitoso");
      // Aquí puedes redirigir al usuario a la página principal
    } else {
      alert("Correo electrónico o contraseña incorrectos");
    }
  }