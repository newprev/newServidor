// Funções em Js para manipular o front
function iniciaCampos(){
    const cepInput = document.querySelector('#cep');

    cepInput.onchange = async function (event) {
        const strCep = String(cepInput.value);

        if (strCep.length == 8) {
            await httpGet(`https://viacep.com.br/ws/${strCep}/json`, avaliaCep);
        }
        else {
            console.log("Não é cep");
        }
    };
}

function avaliaCep(jsonEndereco) {

    if (jsonEndereco.length != 0) {
        limpaCampos();
        
        if (jsonEndereco.localidade){
            document.getElementById('cidade').value = (jsonEndereco.localidade);
            document.getElementById('bairro').value = (jsonEndereco.bairro);
            document.getElementById('endereco').value = (jsonEndereco.logradouro);
            document.getElementById('estados').value = jsonEndereco.uf;

            document.getElementById('numero').focus();
        }
    }
}

function limpaCampos() {
    const listaForm = [
        document.getElementById('cidade'),
        document.getElementById('bairro'),
        document.getElementById('endereco'),
        document.getElementById('numero'),
        document.getElementById('complemento'),
    ];
    
    for (campo of listaForm) {
        campo.value=("");
    }
}

async function httpGet(url, callback) {
    try {
        let response = await fetch(url);
        const jsonResponse = await response.json();

        callback(jsonResponse);
    }
    catch (err) {
        console.log(`Request error: ${err}`);
        callback('');
    }
}

iniciaCampos();
