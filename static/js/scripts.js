function deletar(id){
	cont = window.confirm("Tem certeza que deseja deletar esse cliente do banco de dados?:")
	if(cont){
		window.document.location.replace(`/deletar/${id}`);
	}
}

function save(){
    buttom = document.querySelector(".formulario")
    window.confirm("Deseja salvar as alterações? ")?buttom.submit():console.log("operação cancelada")
}

function stdin(id){
    menu = document.querySelector(".menu")
    input = document.querySelectorAll(".grid-container input");
            objeto = document.querySelector(".grid-container input")
            input.forEach((element) => {
                element.disabled = false;
            });
    window.alert("Modo de edição ativado.")
}

function menu(){
    icone = document.querySelector(".icone i")
    header = document.querySelector(".burguer-menu")


    if (icone.classList.contains("bi-list-ul")){
        icone.classList.remove("bi-list-ul")
        header.style.left = "0px"
        icone.classList.add("bi-x-lg")

    }
    else{
        icone.classList.remove("bi-x-lg")
        icone.classList.add("bi-list-ul")
        header.style.left = "-150px"
    }
}
