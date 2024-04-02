let inp_img = document.getElementById("image");
let showimg = document.getElementById("showimg");
let but = document.getElementById("save");

but.onclick = function() {
  let fr = new FileReader();
  fr.readAsDataURL(inp_img.files[0]);
  fr.onload = function() {
    showimg.src = fr.result;
  };

  showimg.style.display = "block";
  showvideo.style.display = "none";
};

let date = document.getElementById("date");

var months = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
];

let de = new Date();
let year = de.getFullYear();
let mon = months[de.getMonth()];
let day = de.getDate();

let full_date = `${mon} ${day} ${year}`;

date.innerHTML = full_date;