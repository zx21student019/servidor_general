cabeceraHTML="""
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
   
    <!-- javascript de la aplicacion web -->
    
    <script type="text/javascript" src="js/vdc.js"></script>
 
    <title>VENTA DE CAMIONES</title>
 
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-2"></div>
            <div class="col-8 ">
                <h3 class="display-3 text-center">Venta de camiones</h3>
                
"""
 
cuerpHTML='<div id="listaCamiones"></div>'

finalHTML="""
            </div>
            <div class="col-2"></div>
        </div>
    </div>
</body>
</html>
"""

tarjetaCamion="""
<div class="card m-3">
  <div class="row g-0">
    <div class="col-md-5">
      <img src="{}" class="img-fluid rounded-start" alt="{}">
    </div>
    <div class="col-md-7">
      <div class="card-body">
        <h5 class="card-title">Modelo: {}</h5>
        <p class="card-text">Marca: {}</p>
        <p class="card-text">Precio: {}</p>
        <p class="card-text">Descripci&oacute;n: {}</p>
      </div>
    </div>
  </div>
</div>
"""