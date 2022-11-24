cabeceraHTML= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv ="X-UA-Compatible" content = "IE=edge" >
    <meta name = "viewport" content="width=device-width,initial-scale=1.0">
    <!-- Latest compiled and minified CSS -->
    <link href ="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel = " stylesheet ">
    
    <!-- Latest compiled JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js "></script>
    
    <!-- Se ha de poner brackets para cambiarlo en el otro codigo -->
    <title>{}</title>
    {}
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-3"></div>
            <div class="col-6 ">
                <h3 class="display-3 text-center">{}</h3>
                <div class="text-center">{}</div>
                <br>
                <div class="text-center">{}</div>
"""

tarjetaComentario="""
<div class="card m-3">
  <div class="row g-0">
    <div class="col-md-4">
      <img src="{}" class="img-fluid rounded-start" alt="{}">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">{}</h5>
        <p class="card-text">{}</p>
        <p class="card-text"><small class="text-muted">{}</small></p>
      </div>
    </div>
  </div>
</div>
"""
tarjetaComentarioBotonBorrar="""
<div class="card m-3">
  <div class="row g-0">
    <div class="col-md-4">
      <img src="{}" class="img-fluid rounded-start" alt="{}">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">{}</h5>
        <p class="card-text">{}</p>
        <p class="card-text"><small class="text-muted">{}</small></p>
        <p class="card-text"><small class="text-muted"><a class="btn btn-primary" href="borrarComent.py?id={}">Borrar</a></small></p>
      </div>
    </div>
  </div>
</div>
"""

formulario = """
<form enctype = "multipart/form-data" action="insertaComentario.py" method="post">
  <div class="mb-3">
    <label for="titulo" class="form-label">T&iacute;tulo</label>
    <input type="text" class="form-control" id="titulo" aria-describedby="tituloAyuda" name="titulo">
    <div id="tituloAyuda" class="form-text">Escribe el t&iacute;tulo del comentario.</div>
  </div>
  <div class="mb-3">
    <label for="comentario" class="form-label">Comentario</label>
    <input type="textArea" class="form-control" id="comentario" aria-describedby="comentarioAyuda" name="comentario">
    <div id="comentarioAyuda" class="form-text">Escribe el comentario.</div>
  </div>
  <div class="mb-3">
    <label for="formFile" class="form-label">Portada del libro </label>
    <input class="form-control" type="file" id="formFile" name="imagen">
  </div>
  <button type="submit" class="btn btn-primary">Enviar comentario</button>
</form>
"""

finalHTML= """
            </div>
            <div class="col-3"></div>
        </div>
    </div>
</body>
</html>
"""

inicioTabla="""
                 <table class="m-3 table table-striped"><tr><th></th><th>Usuario</th><th>Correo</th></tr>
"""
tablausuarios="""
                    <tr>
                    <td>
                      <form action="borrar.py" metho="get">
                      <input type="hidden" name="id" value="{}">
                      <input type="hidden" name="usuario" value="{}">
                      <button class="btn btn-primary" type="submit">Borrar</button>
                      </form>
                    </td>
                    <td>{}</td>
                    <td>{}</td>
                    </tr>
"""

finalTabla="""
                  </table>
"""

usuarioBorrado="""
Usuario {} borrado
"""

usuarioNoBorrado="""
  No se borro el usuario {}
"""