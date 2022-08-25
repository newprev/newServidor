;(function (){
    const toastSuccess = document.getElementById("toast-success");
    const toastWarning = document.getElementById("toast-warning");

    const toastMessageSuccess = document.getElementById("toast-message-success");
    const toastMessageWarning = document.getElementById("toast-message-warning");

    // Escritório tentou adicionar um advogado sem chaves disponíveis
    htmx.on('semChaves',(event) => {
        const modelToast = new bootstrap.Toast(toastWarning);

        toastMessageWarning.innerText = event.detail.value;
        modelToast.show();
    });

    // Escritório (des)ativou cadastro de um(a) advogado(a)
    htmx.on('desAtivaAdvogado',(event) => {
        const modelToast = new bootstrap.Toast(toastSuccess);

        console.log(event);
        toastMessageSuccess.innerText = event.detail.value;
        modelToast.show();
    });

    // Escritório adquiriu uma chave com sucesso
    htmx.on('chaveAdicionada',(event) => {
        const modelToast = new bootstrap.Toast(toastSuccess);
        const btnVoltaDashboard = document.getElementById('volta-dashboard');

        // if (btnVoltaDashboard) {
        //     btnVoltaDashboard.click();
        // }
        // else {
        //     console.log('***************');
        //     console.log('Era para voltar para o dashboard após adicionar uma chave');
        //     console.log('***************');
        // }

        toastMessageSuccess.innerText = event.detail.value;
        modelToast.show();
    });

    // Ecritório tenta adquirir nova chave, mas há algum problema no cadastro
    htmx.on('erroChave',(event) => {
        const modelToast = new bootstrap.Toast(toastWarning);

        console.log(event);
        toastMessageWarning.innerText = event.detail.value;
        modelToast.show();
    });

    // Escritório tentou adquirir nova chave sem estar logado
    htmx.on('naoAutorizado',(event) => {
        const modelToast = new bootstrap.Toast(toastWarning);

        console.log(event);
        toastMessageWarning.innerText = event.detail.value;
        modelToast.show();
    });

})()