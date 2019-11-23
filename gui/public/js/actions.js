let actions = ["move", "sounds", "cozmo-lights", "animations"]
$( document ).ready(function() {
    console.log("document on")
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
    // put li in stack with its attributes
    setTimeout(() => {
        $(".push-to-stack").click(function(event){
            $("#cozmo-stack").append('<li class="list-group-item" code='+event.target.getAttribute("code")+'>'+event.target.name+'<button class="remove btn-danger float-right" code='+event.target.getAttribute("code")+'> x </button></li>');
            let newItem = event.target.getAttribute("code")
            $.post('/task-added', {name:newItem}); 
        });
    }, 0);
});

// remove li in stack
$(document).on('click', "button.remove", function(event) {
    let elementtoRemove = event.target.getAttribute("code")
    let parentToRemove = this.parentNode
    $(parentToRemove).remove()
    $.post('/delete', {name:elementtoRemove}); 
});