
// Events
// select all the buttons with the class name "btn"
const buttons = document.getElementsByClassName("btn_api");

function exibe_dados(element) {
    console.log("Href -> ", element);
    // this.stopPropagation();
    fetch(element.href)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.data);
    }).catch(function(error) {
        console.log(error);
    });
};

// loop through each button and add a click event listener
for (i=0; i<buttons.length; i++){
    button = buttons[i];
    button.addEventListener("click", function(e) {
        console.log("Href -> ", button);
        e.stopPropagation();
        e.preventDefault();
        fetch(button.href)
            .then((resp) => resp.json())
            .then(function(data) {
                console.log("Data -> ", data.data);
                return data.map(function(

                ));
        }).catch(function(error) {
            console.log(error);
        });
    });
}