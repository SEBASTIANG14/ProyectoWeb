  // Función para agregar un producto al carrito
  function agregarProducto() {
    // Obtener el nombre y precio del producto desde los campos de entrada
    var nombre = document.getElementById("nombre").value;
    var precio = document.getElementById("precio").value;

    // Crear un objeto con la información del producto
    var producto = {
      nombre: nombre,
      precio: precio
    };

    // Obtener los productos existentes en el carrito del local storage
    var carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    // Agregar el nuevo producto al carrito
    carrito.push(producto);

    // Guardar el carrito actualizado en el local storage
    localStorage.setItem("carrito", JSON.stringify(carrito));

    // Limpiar los campos de entrada
    document.getElementById("nombre").value = "";
    document.getElementById("precio").value = "";

    // Actualizar la lista de productos en el carrito
    mostrarProductos();
  }

  // Función para eliminar un producto del carrito
  function eliminarProducto(index) {
    // Obtener los productos existentes en el carrito del local storage
    var carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    // Eliminar el producto en el índice especificado
    carrito.splice(index, 1);

    // Guardar el carrito actualizado en el local storage
    localStorage.setItem("carrito", JSON.stringify(carrito));

    // Actualizar la lista de productos en el carrito
    mostrarProductos();
  }

  // Función para mostrar los productos en el carrito
  function mostrarProductos() {
    // Obtener el contenedor del carrito
    var carritoContainer = document.getElementById("carrito-container");

    // Obtener los productos existentes en el carrito del local storage
    var carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    // Limpiar el contenido del contenedor
    carritoContainer.innerHTML = "";

    // Recorrer los productos y agregarlos al contenedor
    carrito.forEach(function (producto, index) {
      var productoElement = document.createElement("div");
      productoElement.innerHTML =
        "<span>" +
        producto.nombre +
        " - $" +
        producto.precio +
        "</span>" +
        "<button onclick='eliminarProducto(" +
        index +
        ")'>Eliminar</button>";
      carritoContainer.appendChild(productoElement);
    });
  }

   // Función para agregar productos al carrito
   function agregarAlCarrito(nombre, precio) {
    // Recupera el carrito almacenado en el local storage o crea uno vacío
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    // Agrega el nuevo producto al carrito
    carrito.push({ nombre, precio, cantidad: 1 });

    // Actualiza el local storage con el nuevo carrito
    localStorage.setItem('carrito', JSON.stringify(carrito));

    // Actualiza la visualización del carrito
    mostrarCarrito();
  }

  // Función para mostrar el carrito
  function mostrarCarrito() {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    let listaCarrito = document.getElementById('lista-carrito');
    let totalElement = document.getElementById('total');
    let total = 0;

    // Limpia la lista de productos en el carrito
    listaCarrito.innerHTML = '';

    // Recorre el carrito y muestra cada producto en la lista
    carrito.forEach(producto => {
      let item = document.createElement('li');
      item.textContent = `${producto.nombre} - Cantidad: ${producto.cantidad} - Precio: $${producto.precio}`;
      listaCarrito.appendChild(item);
      total += producto.precio * producto.cantidad;
    });

    // Muestra el total
    totalElement.textContent = total;
  }

  // Función para realizar la compra
  function realizarCompra() {
    // Puedes implementar aquí la lógica para guardar la compra en el historial del usuario
    // Por ahora, simplemente vaciamos el carrito
    vaciarCarrito();
    alert('Compra realizada con éxito. ¡Gracias por tu compra!');
  }

  // Función para vaciar el carrito
  function vaciarCarrito() {
    // Vacía el carrito en el local storage
    localStorage.removeItem('carrito');

    // Actualiza la visualización del carrito
    mostrarCarrito();
  }
