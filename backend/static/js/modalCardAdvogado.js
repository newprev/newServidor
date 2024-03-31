// $("#foo").change(function() { 
//     $.ajax({
//       type: 'POST',
//       url: '/some_url/',
//       data: {
//           'some_data_from_page': $("#some_data_from_page").val()
//       },
//       success: function(data) {
//           alert("Got response from server ...", data);
//       }
//     });
// });


function pegaInfoAdvogado(advogadoId){
    const botaoEscondido = document.getElementById(`botaoEscondido${advogadoId}`);

    botaoEscondido.click();    
}