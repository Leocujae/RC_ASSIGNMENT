

function Formvalidation(){

    var description = document.getElementById("description").value;
    if(description.length > 0){

        //Esto aqui es una prueba
        class suggestion {
            constructor(proyect,task,description){
                this.proyect = document.getElementById("proyect").value;
                this.task = document.getElementById("task").value;
                this.reason = document.getElementById("reason").value;
                this.description = description;
            } 
        }

        alert("TodoOk");
        return true
    }
    else {
        alert("error en el formulario")
        return false
    }

}


function GiveValues(){
    var proyects = ["Proyect1","Proyect2","Proyect3"];
    var task = ["task 1" ,"task  2", "task 3"];
    var reason = ["1","2","3"];

    for(var i = 0 ; i < proyects.length ; i++){
        var elementoOpcion = document.createElement("option");
        elementoOpcion.value = proyects[i];
        elementoOpcion.text = proyects[i];
        document.getElementById("proyect").appendChild(elementoOpcion);
    }

    for(var i = 0 ; i < task.length ; i++){
        var elementoOpcion = document.createElement("option");
        elementoOpcion.value = task[i];
        elementoOpcion.text = task[i];
        document.getElementById("task").appendChild(elementoOpcion);
    }
    for(var i = 0 ; i < reason.length ; i++){
        var elementoOpcion = document.createElement("option");
        elementoOpcion.value = reason[i];
        elementoOpcion.text = reason[i];
        document.getElementById("reason").appendChild(elementoOpcion);
    }


}
GiveValues();


function ValidatorChangeSuggestion(){

    localStorage.setItem("token","1");
    if(localStorage.token == "1"){
        window.location.href = "https://www.google.com";
    }
    else{
       class formulario {
            constructor(proyect,task,suggestion){
                this.proyect = "";
                this.task ="";
                this.suggestion ="";
            }
       }     
    }
}