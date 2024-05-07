
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

function maiores_salarios(url, target) {
    fetch(url)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.data);
            dado = data.data;
            content =  `<p><strong>Pessoa 1:</strong> ${dado.pessoa1}</p>`;
            content += `<p><strong>Pessoa 2:</strong> ${dado.pessoa2}</p>`;
            content += `<p><strong>Pessoa 3:</strong> ${dado.pessoa3}</p>`;
            document.getElementById(target).innerHTML = content;
    }).catch(function(error) {
        console.log(error);
    });
}