const persona1 = {
    nombre: "Ana",
    apellidos: "Lopez",
    edad: 29,
    nombrecompleto: function () {
        return this.nombre + " " + this.apellidos;
    },
    fecNac:new Date("1998-11-25")
    
}

const persona2 = {
    nombre: "Juan",
    apellidos: "Garcia",
    edad: 4,
    nombrecompleto: function () {
        return this.nombre + " " + this.apellidos;
    },
    fecNac:new Date("2019-07-13")
}

const persona3 = {
    nombre: "Antonio",
    apellidos: "Fernandez",
    edad: 45,
    nombrecompleto: function () {
        return this.nombre + " " + this.apellidos;
    },
    fecNac:new Date("1970-08-01")
}

const persona0 = {
    nombre: "Federico",
    apellidos: "Zapico",
    edad: 54,
    nombrecompleto: function () {
        return this.nombre + " " + this.apellidos;
    },
    fecNac:new Date("1968-05-20")
}

const listaPersonas = [persona1, persona2,persona3,persona0];

function mostrarObjetos() {
    console.log(persona1.nombre);
    console.log(persona1.apellidos);
    console.log(persona1.edad);
    console.log(persona0.fecNac)

    persona1.direccion ="calle principal...";
    console.log(persona1.nombrecompleto())

    console.log(persona2["nombre"]);
    console.log(persona2["apellidos"]);
    console.log(persona2["edad"]);
    console.log(persona2.nombrecompleto());

    console.log(listaPersonas);
}

function ordenarListaPersonas() {
   /*
    console.log(listaPersonas);*/
    listaPersonas.sort(ordenAlfabeticoPorApellidos);
    console.log(listaPersonas)
    
}

function ordenAlfabeticoPorApellidos (a,b){
    if (a.apellidos < b.apellidos) {return 1;}
    if (a.apellidos > b.apellidos) {return -1;}
    return 0;
}

function ordenarListaPersonasPorEdades(){
    listaPersonas.sort(ordenPorFecNac);
    console.log(listaPersonas);
}

function ordenPorFecNac (a,b) {
    if (a.fecNac < b.fecNac) {return -1;}
    if (a.fecNac > b.fecNac) {return 1;}
    return 0;
}

function personaMayor(){
    listaPersonas.sort(ordenPorEdad);
    document.getElementById("salida").innerHTML=listaPersonas[0].nombre+" "+listaPersonas[0].apellidos
}

function personaMenor(){
    listaPersonas.sort(ordenPorEdad);
    document.getElementById("salida").innerHTML=listaPersonas[listaPersonas.length-1].nombre+" "+listaPersonas[listaPersonas.length-1].apellidos
}

function ordenPorEdad (a,b) {
    if (a.edad < b.edad) {return 1;}
    if (a.edad > b.edad) {return -1;}
    return 0;
}