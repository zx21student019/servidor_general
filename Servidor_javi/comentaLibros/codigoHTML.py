cabeceraHTML= """
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{}</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;0,800;1,700;1,800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/miEstilo.css">
  
  {}
</head>

<body>
  <header class="cabecera">
    <h3 class="titulo">Tu Biblioteca Online</h3>
    {}
  </header>
  <div class="contenido">
    <div class="contenedor-titulo">
      <h1 class="titulo">{}</h1>
    </div>
    <p class="texto-contenido">{}</p>
"""

contenedorComentarios = """
<div class="contenedor-comentarios">
  {}
</div>
"""

comentario = """
<div class="comentario">
  <div class="contenedor-portada">
    <img class="portada-libro" src="img/{}" alt="portada">
  </div>
  <h3 class="titulo-libro">{}</h3>
  <h4 class="autor-libro">{}</h4>
  <p class="descripcion-comentario">
    {}
  </p>
  {}
</div>
"""

botonBorrarComentario = """
<form class="formulario-borrar-boton" action="borrarComentario.py" method="post" enctype="multipart/form-data">
  <input type="text" name="id-libro" value="{}" class="input-invisible">
  <button class="boton-borrar" type="submit">Borrar Comentario</button>
</form>
"""

formularioComentario = """
<div class="contenedor-formulario-comentario">
  <form class="formulario-comentario" action="insertarComentarioBBDD.py" method="post" enctype="multipart/form-data">
    <div class="campo-insertar-comentario">
      <label class="etiqueta-datos-comentario" for="titulo-libro">Titulo:</label>
      <input class="datos-formulario-comentario" type="text" name="titulo" id="">
    </div>
    <div class="campo-insertar-comentario">
      <label class="etiqueta-datos-comentario" for="autor">Autor:</label>
      <input class="datos-formulario-comentario" type="text" name="autor" id="">
    </div>
    <div class="campo-insertar-comentario">
      <label class="etiqueta-datos-comentario" for="comentario-libro">Comentario:</label>
      <textarea class="datos-formulario-comentario datos-formulario-comentario-grande" name="comentario"></textarea>
    </div>
    <div class="campo-insertar-comentario">
      <label class="etiqueta-datos-comentario" for="comentario-libro">Subir Portada:</label>
      <label class="datos-formulario-comentario-subir">
        <input type="file" name="fichero" class="subir-fichero-oculto"/>
        Subir Fichero
      </label>
    </div>
    <div class="botonera"><button class="boton-publicar-comentario" type="submit">Publicar</button></div>
  </form>
  <div class="contenedor-texto-insertar-comentario">
    <p class="texto-insertar-comentario">
      Por favor, asegurese de rellenar todos los campos, y de introducir datos validos en el formulario.
      Los comentarios podran ser vistos por el resto de usuarios, y usted podra borrar sus propios comentarios.
      La subida de la imagen de la portada del libro es opcional.
    </p>
  </div>
</div>
"""

tablaUsuarios = """
  <div class="contenedor-tabla">
    <table class="tabla-usuarios">
      <tr>
        <td class="titulo-celda">ID</td>
        <td class="titulo-celda">Nombre</td>
        <td class="titulo-celda">Correo</td>
        <td class="titulo-celda">Borrar</td>
      </tr>
        {}    
    </table>
  </div>
"""

filaUsuario = """
<tr>
  <td class="contenido-celda">{}</td>
  <td class="contenido-celda">{}</td>
  <td class="contenido-celda">{}</td>
  <td class="contenido-celda">
    <form class="formulario-borrar-usuario" action="borrarUsuario.py" method="post" enctype="multipart/form-data">
      <input type="text" name="id-usuario" value="{}" class="input-invisible">
      <button class="boton-borrar boton-tabla" type="submit">Borrar Usuario</button>
    </form>
  </td>
</tr>
"""

finalHTML= """
  </div>
</body>
</html>
"""