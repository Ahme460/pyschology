let imgs =document.querySelectorAll(".section3 img")

imgs.forEach(img => {
    img.addEventListener("click",(e)=>{
        let overlay =document.createElement("div")
        overlay.classList.add("overlay")
        document.body.append(overlay)
        let postshow =document.createElement("div")
        document.body.append(postshow)
        postshow.classList.add("post")
        let img =document.createElement("img")
        img.src=e.target.src
        postshow.append(img)
        let text =document.createElement("p")
        text.innerHTML=e.target.dataset.text
        postshow.append(text)
        let exit =document.createElement("span")
        exit.innerHTML="x"
        postshow.append(exit)
        exit.addEventListener("click",()=>{
            overlay.remove()
            postshow.remove()
        })
    })


});

// _______________________________________________________________________________

// console.log(document.querySelectorAll(".home .section2 .start .text p")[1]);

window.onscroll=function(){
    if(scrollY >= 210){
        document.querySelectorAll(".home .section2 .start .text p")[0].style.right="0"
    }
    if(scrollY >= 310){
        document.querySelectorAll(".home .section2 .start .text p")[1].style.right="0"
    }
    if(scrollY >= 410){
        document.querySelectorAll(".home .section2 .start .text p")[2].style.right="0"
    }
    if(scrollY >= 510){
        document.querySelectorAll(".home .section2 .start .text p")[3].style.right="0"
    }
    if(scrollY >= 610){
        document.querySelectorAll(".home .section2 .start .text p")[4].style.right="0"
    }
    if(scrollY >= 710){
        document.querySelectorAll(".home .section2 .start .text p")[5].style.right="0"
        document.querySelector(".home .section2 .start .text").style.border="1px solid var(--main-color)"
    }



}