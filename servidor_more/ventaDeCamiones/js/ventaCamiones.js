onload=principal;

let listaCamiones;

function principal() {
    document.getElementById("listaCamiones");
    cargarServidorCamiones();
}

function cargarServidorCamiones() {
    //una peticion al resvidor de la lista de camiones
    //creacion de elementos en el DOM dentro del div listacamiones

    let camion1 = '\
    <div class="card m-3">\
        <div class="row g-0">\
        <div class="col-md-5">\
            <img src="img/scaniaSCANIAR450NTG.png" class="img-fluid rounded-start" alt="SCANIA R450 NTG">\
        </div>\
        <div class="col-md-7">\
            <div class="card-body">\
            <h5 class="card-title">Modelo: R450 NTG</h5>\
            <p class="card-text">Marca: SCANIA</p>\
            <p class="card-text">Precio: 58.000 &euro;</p>\
            <p class="card-text">Descripci&oacute;n: siempre en garage</p>\
            </div>\
        </div>\
        </div>\
    </div>';
 
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

    listaCamiones.innerHtml = 
}