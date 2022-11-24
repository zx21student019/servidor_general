pagina = """
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <title>Inicio de Sesion</title>

        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;0,800;1,700;1,800&display=swap"
            rel="stylesheet">

        <link rel="stylesheet" href="./../style/style.css">
    </head>

    <body>
        <header class="cabecera">
            <h3 class="titulo">Zoo de Madrid</h3>
        </header>
        <div class="contenido">
            <div class="contenedor-titulo">
                <h1 class="titulo">Bienvenido - {}<br>Pagina {}</h1>
            </div>
            <a href="{}" class="enlace-volver">Acceder a la Pagina {}</a>
            <a href="./../app/logout.py" class="enlace-volver">Logout</a>
        </div>


    </body>

    </html>
"""