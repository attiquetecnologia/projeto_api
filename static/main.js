
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