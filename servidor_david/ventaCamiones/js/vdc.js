onload = principal;

let listaCamiones;
let texto = "";

function principal() {
    listaCamiones = document.getElementById("listaCamiones")
    cargarServidorCamiones();

}

function cargarServidorCamiones() {

    //peticion a servidor de la lista de camiones
    //**********************************
    //configura datos y objetos
    //**********************************

    //parrafo para la salida de datos
    //?let parrafo = document.getElementById("salida");

    //crear el objeto XMLHttpRequest para acceder al servidor
    let jsonhttp = new XMLHttpRequest();

    //**********************************
    //registro de la funcion que trata la 
    //respuesta del servidor
    //**********************************

    jsonhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let lc = JSON.parse(this.responseText);
            for (let x = 0; x < lc.length; x++) {
                texto = texto+' \
                    <div class="card m-3">\
                        <div class="row g-0">\
                        <div class="col-md-5">\
                            <img src="img/'+lc[x][0]+'" class="img-fluid rounded-start">\
                        </div>\
                        <div class="col-md-7">\
                            <div class="card-body">\
                            <h5 class="card-title">Modelo:'+lc[x][1]+'</h5>\
                            <p class="card-text">Marca:'+lc[x][2]+'</p>\
                            <p class="card-text">Precio:'+lc[x][3]+' &euro;</p>\
                            <p class="card-text">Descripci&oacute;n: '+lc[x][4]+'</p>\
                            </div>\
                        </div>\
                        </div>\
                    </div>';
            }
            listaCamiones.innerHTML=texto
        }
    };

    //**********************************
    //codigo que realiza la petición al sevidor
    //se pueden hacer peticiones GET, POST (y otros verbos HTTP)
    //**********************************
    //construir la peticion al servidor
    jsonhttp.open("GET", "listaCamiones.py", true);
    //ejecutar la peticion al sevidor
    jsonhttp.send();

    //creación de elementos en el DOM dentro del div listaCamiones
    let camion1 = ` \
    <div class="card m-3">\
        <div class="row g-0">\
        <div class="col-md-5">\
            <img src="img/scaniaSCANIAR450NTG.png" class="img-fluid rounded-start" alt="SCANIA R 450 NTG">\
        </div>\
        <div class="col-md-7">\
            <div class="card-body">\
            <h5 class="card-title">Modelo: R450 NTG</h5>\
            <p class="card-text">Marca: SCANIA</p>\
            <p class="card-text">Precio: 78.500 &euro;</p>\
            <p class="card-text">Descripci&oacute;n: siempre en garage</p>\
            </div>\
        </div>\
        </div>\
    </div>';`

    let camion2 = '\
    <div class="card m-3">\
        <div class="row g-0">\
        <div class="col-md-5">\
            <img src="img/VolvoFH500.png" class="img-fluid rounded-start" alt="Volvo FH 500">\
        </div>\
        <div class="col-md-7">\
            <div class="card-body">\
            <h5 class="card-title">Modelo: FH 500</h5>\
            <p class="card-text">Marca: Volvo</p>\
            <p class="card-text">Precio: 78.000 &euro;</p>\
            <p class="card-text">Descripci&oacute;n: poco uso</p>\
            </div>\
        </div>\
        </div>\
    </div>';

    //listaCamiones.innerHTML = camion1 + camion2;
}
