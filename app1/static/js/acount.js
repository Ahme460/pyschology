let but =document.getElementById("but")
let image =document.getElementById("image")
let namer =document.getElementById("name")
let Experience =document.getElementById("Experience")
let Certificates =document.getElementById("Certificates")


but.addEventListener("click",(e)=>{
    let overlay =document.createElement("div")
    document.body.append(overlay)
    overlay.classList.add("overlay")
    let edit =document .createElement("div")
    document.body.append(edit)
    edit.classList.add("editor")
    let img =document.createElement("img")
    img.src=image.src
    edit.append(img)
    let file =document.createElement("input")
    file.setAttribute("type","file")
    file.id="file"
    edit.append(file)
    let label =document.createElement("label")
    label.setAttribute("for","file")
    edit.append(label)
    label.innerHTML="Change"
file.addEventListener("change",()=>{
    let fr =new FileReader
    fr.readAsDataURL(file.files[0])
    fr.onload=function(){
        img.src=fr.result
    }
})

let form1 =document.createElement("form")
edit.append(form1)  

    let div =document.createElement("div")
    form1.append(div)
    div.classList.add("div")

    let div1 =document.createElement("div")
    div.append(div1)
    div1.classList.add("div1")
    let p1 =document.createElement("p")
    p1.classList.add("p")
    div1.append(p1)
    p1.innerHTML=namer.innerHTML
    let change1 =document.createElement("p")
    change1.innerHTML="Change name"
    change1.classList.add("change")
    div1.append(change1)
    let input1 =document.createElement("input")
    div1.append(input1)
    change1.addEventListener("click",()=>{
        p1.style.display="none"
        input1.style.display="block"
        input1.focus()
        change1.style.display="none"
        let x =document.createElement("p")
        div1.append(x)
        x.innerHTML="X"
        x.classList.add("x")
        x.addEventListener("click",()=>{
            x.remove()
        change1.style.display="block"
        p1.style.display="flex"
            input1.style.display="none"
            input1.value=""
        })
    })


    let div2 =document.createElement("div")
    div.append(div2)
    div2.classList.add("div1")
    let p2 =document.createElement("p")
    p2.classList.add("p")
    div2.append(p2)
    p2.innerHTML=Experience.innerHTML
    let change2 =document.createElement("p")
    change2.innerHTML="Change Experience"
    change2.classList.add("change")
    div2.append(change2)
    let input2 =document.createElement("input")
    div2.append(input2)
    change2.addEventListener("click",()=>{
    p2.style.display="none"
    input2.style.display="block"   
    input2.focus()    
    change2.style.display="none"
    let x =document.createElement("p")
    div2.append(x)
    x.innerHTML="X"
    x.classList.add("x")
    x.addEventListener("click",()=>{
        x.remove()
    change2.style.display="block"
    p2.style.display="flex"
        input2.style.display="none"
        input2.value=""
    })
    })


    let div3 =document.createElement("div")
    div.append(div3)
    div3.classList.add("div1")
    let p3 =document.createElement("p")
    p3.classList.add("p")
    div3.append(p3)
    p3.innerHTML=Certificates.innerHTML
    let change3 =document.createElement("p")
    change3.innerHTML="Change Certificates"
    change3.classList.add("change")
    div3.append(change3)
    let input3 =document.createElement("input")
    div3.append(input3)
    change3.addEventListener("click",()=>{
        p3.style.display="none"
        input3.style.display="block"
        input3.focus()
        change3.style.display="none"
        let x =document.createElement("p")
        div3.append(x)
        x.innerHTML="X"
        x.classList.add("x")
        x.addEventListener("click",()=>{
            x.remove()
        change3.style.display="block"
        p3.style.display="flex"
            input3.style.display="none"
            input3.value=""
        })
    })


    let save =document.createElement("button")
    save.classList.add("save")
    form1.append(save)
    save.innerHTML="Save"
    save.addEventListener("click",()=>{
        image.src=img.src
         if(input1.value != ""){
            namer.innerHTML= input1.value
         }
         if (input2.value != "") {
            Experience.innerHTML = input2.value
         }
         if (input3.value != "") {
            Certificates.innerHTML = input3.value
         }
    })

    let span =document.createElement("span")
    edit.append(span)
    span.innerHTML="x"
    span.onclick=function(){
        overlay.remove()
        edit.remove()
    }
})



