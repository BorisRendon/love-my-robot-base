let actions = ["move", "sounds", "cozmo-things", "animations"]
$( document ).ready(function() {

    if (localStorage.reload) {
        $.post('/delete-stack', '')
    }

    // display and hide options from menu
    setTimeout(() => {
        for (let i = 0; i < actions.length; i++) {
        $(`.${actions[i]}`).click(function(){
            document.getElementsByClassName(actions[i])[1].classList.remove('hide')

            for (let j = 0; j < actions.length; j++){
                if(j != i){
                    document.getElementsByClassName(actions[j])[1].classList.add('hide')
                }
            }
        });
    }    
    }, 0);

});

window.onbeforeunload = sendTimeToServer;
function sendTimeToServer() {
    localStorage.reload = true
}

$(".modal-item").click(function(event){
    var modifier = event.target.getAttribute("modifier")            
    modal(modifier)
});

// remove li in stack
$(document).on('click', "button.remove", function(event) {
    let elementtoRemove = event.target.getAttribute("code")
    let parentToRemove = this.parentNode
    $(parentToRemove).remove()
    $.post('/delete', {name:elementtoRemove}); 
});

let modifier

function modal(mod){
    modifier = mod
    console.log(modifier)
}

$(".push-to-stack").click((event)=>{
    console.log(modifier)
    modifier = modifier || ''

    console.log("going to stack")

    // modify the code with attribute
    let theCode = event.target.getAttribute("code")
    if(modifier != ""){
        theCode += "&" + modifier
    }
    // push li in stack
    $("#cozmo-stack").append('<li class="list-group-item" code='+theCode+'>'+event.target.name+" "+modifier+'<button class="remove btn-danger float-right" code='+theCode+'> x </button></li>');
    let newItem = theCode
    $.post('/task-added', {name:newItem}); 
});