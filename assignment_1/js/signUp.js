
function goBack() {
    window.location.href = "../html/mainPage.html";
}
function check(e) {
    tecla = (document.all) ? e.keyCode : e.which;

    // Tecla de retroceso para borrar, siempre la permite
    if (tecla == 8) {
        return true;
    }

    // Obtener el valor actual del campo de entrada
    var valor = e.target.value;

    // Patrón de entrada, en este caso solo acepta letras y números, y no permite que se inicie con un número
    patron = /^[A-Za-z][A-Za-z0-9]*$/;

    // Verificar que el nuevo carácter cumpla con el patrón
    tecla_final = String.fromCharCode(tecla);
    nuevo_valor = valor + tecla_final;
    return patron.test(nuevo_valor);
}
function checkPhone(e){
    tecla = (document.all) ? e.keyCode : e.which;

    // Tecla de retroceso para borrar, siempre la permite
    if (tecla == 8) {
        return true;
    }

    // Obtener el valor actual del campo de entrada
    var valor = e.target.value;

    // Patrón de entrada, en este caso solo acepta letras y números, y no permite que se inicie con un número
    patron = /^[0-9]*$/;

    // Verificar que el nuevo carácter cumpla con el patrón
    tecla_final = String.fromCharCode(tecla);
    nuevo_valor = valor + tecla_final;
    return patron.test(nuevo_valor);
}
function checkDate(e){
    tecla = (document.all) ? e.keyCode : e.which;

    // Tecla de retroceso para borrar, siempre la permite
    if (tecla == 8) {
        return true;
    }

    // Obtener el valor actual del campo de entrada
    var valor = e.target.value;

    // Patrón de entrada, en este caso solo acepta letras y números, y no permite que se inicie con un número
    patron = /^[0-9]*$/;

    // Verificar que el nuevo carácter cumpla con el patrón
    tecla_final = String.fromCharCode(tecla);
    nuevo_valor = valor + tecla_final;
    return patron.test(nuevo_valor);
}
