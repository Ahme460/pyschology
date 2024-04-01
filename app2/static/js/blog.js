let inp_img =document.getElementById("image")
let inp_vid =document.getElementById("video")
let showvideo =document.getElementById("showvideo")
let showimg =document.getElementById("showimg")


inp_img.onchange=function(){
    let fr =new FileReader
    fr.readAsDataURL(inp_img.files[0])
    fr.onload=function(){
        showimg.src=fr.result
    }


    showimg.style.display="block"
    showvideo.style.display="none"


}
inp_vid.onchange=function(){
    let fr =new FileReader
    fr.readAsDataURL(inp_vid.files[0])
    fr.onload=function(){
        showvideo.src=fr.result
    }


    showvideo.style.display="block"
    showimg.style.display="none"

}

let date=document.getElementById("date")

var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];


let de = new Date()


let year =de.getFullYear()
let mon =months[de.getMonth()]
let day =de.getDate()

let full_date = `${mon} ${day},${year}`

date.innerHTML=full_date