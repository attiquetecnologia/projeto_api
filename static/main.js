
// Events

function load_data(url, target) {
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.data);
            document.getElementById(target).innerHTML = `<p>${data.data}</p>`;
    }).catch(function(error) {
        console.log(error);
    });
}

function salarios(url, target) {
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.data);
            dado = data.data;
            content = `<p><strong>Registros:</strong> ${dado.registros}</p>`;
            content += `<p><strong>Registros:</strong> ${dado.porcentagem}%</p>`;
            content += `<p><strong>Total:</strong> ${dado.total}</p>`;
            document.getElementById(target).innerHTML = content;
    }).catch(function(error) {
        console.log(error);
    });
}