
let labels =document.querySelectorAll(".chose label")

labels.forEach(element => {
    element.addEventListener("click",(e)=>{
        labels.forEach(el => {
            el.classList.remove("active")
        });
        e.target.classList.add("active")
    })
});


let inp =document.getElementById("password")
let inpuser =document.getElementById("username")
let inpemail =document.getElementById("email")
let inpage =document.getElementById("age")
let eror =document.getElementById("eror")
let but =document.querySelector("button")
let lenghtvalue=inp.value.lenght

but.onclick=function(event){
    let hasnumbers =/[0-9]/.test(inp.value)
    let hasletters=/[a-zA-Z]/.test(inp.value)
    let has8letters =String(inp.value).length>=8
if(inp.value!="" && inpuser.value!="" && inpemail.value!="" && inpage.value!=""){
    if(hasletters===false||hasnumbers===false||has8letters===false){
        event.preventDefault()
    eror.innerHTML=`Must contain at least one letter <br> It should contain numbers <br> Must be at least 8`
    }
}else{
    event.preventDefault()

}
}
