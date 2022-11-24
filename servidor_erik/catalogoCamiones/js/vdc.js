onload = principal

let listaCamiones;

function principal(){
    listaCamiones = document.getElementById("listaCamiones");
    cargarServidorCamiones();
}

function cargarServidorCamiones(){
    //una peticion al servidor de la lista de camiones - AJAX
    //crear el objeto XMLHttpRequest para acceder al servidor
	let jsonhttp = new XMLHttpRequest();

    //*********************************
	// codigo para tratar la respuesta
	jsonhttp.onreadystatechange  = function(){
		//evaluar la respuesta del servidor
        if(this.readyState == 4 && this.status == 200){
            let listaC = JSON.parse(this.responseText);   

            for (c of listaC){
                listaCamiones.appendChild(crearCamion(c))
            }
		}
	}

    //construir la petición al servidor
	jsonhttp.open("GET","http://www.servidor.es/catalogoCamiones/listarCamiones.py",true);
	//ejecutar la petición al servidor
	jsonhttp.send();
}

function crearCamion(c){

    let img = c[4];
    let marca = c[0];
    let modelo = c[1];
    let desc = c[2];
    let precio = c[3];

    let divTarjCam = document.createElement("div");
    divTarjCam.setAttribute("class","card m-3");

    let divRow = document.createElement("div");
    divRow.setAttribute("class","row g-0");

    let subDivImg = document.createElement("div");
    subDivImg.setAttribute("class","col-md-5");

    let imagen = document.createElement("img");
    imagen.setAttribute("src","img/"+img);
    imagen.setAttribute("class","img-fluid rounded-start");
    imagen.setAttribute("alt",marca+" "+modelo);

    subDivImg.appendChild(imagen);

    let subDivInfo = document.createElement("div");
    subDivInfo.setAttribute("class","col-md-7");

    let subDivCard = document.createElement("div");
    subDivCard.setAttribute("class","card-body");

    let infoMod = document.createElement("h5");
    infoMod.setAttribute("class","card-title");
    infoMod.innerHTML = "Modelo: "+modelo;

    let infoMarca = document.createElement("p");
    infoMarca.setAttribute("class","card-text");
    infoMarca.innerHTML = "Marca: "+marca;

    let infoPrecio = document.createElement("p");
    infoPrecio.setAttribute("class","card-text");
    infoPrecio.innerHTML = "Precio: "+precio;

    let infoDesc = document.createElement("p");
    infoDesc.setAttribute("class","card-text");
    infoDesc.innerHTML = "Descripci&oacute;n: "+desc;

    subDivCard.appendChild(infoMod);
    subDivCard.appendChild(infoMarca);
    subDivCard.appendChild(infoPrecio);
    subDivCard.appendChild(infoDesc);

    subDivInfo.appendChild(subDivCard);

    divRow.appendChild(subDivImg);
    divRow.appendChild(subDivInfo);

    divTarjCam.appendChild(divRow);

    return divTarjCam;
}

function enviarCamion(){
    //crear el objeto XMLHttpRequest para acceder al servidor
    let jsonhttp = new XMLHttpRequest();

    //datos para enviar al servidor
    let marca = document.getElementById("marca").value;
    let modelo = document.getElementById("modelo").value;
    let precio = document.getElementById("precio").value;
    let desc = document.getElementById("desc").value;

    //*********************************
    // codigo para tratar la respuesta
    jsonhttp.onreadystatechange  = function(){
        //evaluar la respuesta del servidor
        if(this.readyState == 4 && this.status == 200){
            let resultado = JSON.parse(this.responseText);
            if(resultado){
                c=[marca,modelo,desc,precio,"camionDeffault.png"]
                listaCamiones.insertBefore(crearCamion(c), listaCamiones.firstChild);                
            }
        }
    }

    //construir la petición al servidor
	jsonhttp.open("POST","http://www.servidor.es/catalogoCamiones/guardarCamion.py",true);
    jsonhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	//ejecutar la petición al servidor
	jsonhttp.send("marca="+marca+"&modelo="+modelo+"&precio="+precio+"&desc="+desc);
}