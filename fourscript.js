function loadDoc(url,func){
    let xhttp=new XMLHttpRequest();
    xhttp.onload=function(){
        if (xhttp.status !=200){
            console.log("error");
        }else{
            func(xhttp.response);
        }
    }
    xhttp.open("GET", url);
    xhttp.send();
}

function upload_picture_public(){
    let xhttp=new XMLHttpRequest();
    xhttp.onload= function(){
        if (xhttp.status != 200){
            console.log("Error");
        }else{
            upload_file_response_public(xhttp.response);
        }
    }
    xhttp.open("POST", "/uploadpicturepublic", true);

    var formData=new FormData();
    formData.append("file", document.getElementById("file").files[0]);
    formData.append("caption", document.getElementById("caption").value);
    xhttp.send(formData);
}
function upload_file_response_public(response){
    location.reload();
}
//////////////////
function listpicturespublic(){
    loadDoc("/listpicturespublic", listpictures_response_public);
}
function listpictures_response_public(response){
    let data= JSON.parse(response);
    let items=data["results"];
    let divResults= document.getElementById("divResults");
    let temp ="";
    for (let i =0; i<items.length; i++){
        temp+="<div class=\"pic_container\">";
        temp+="<div class=\"picture\">"
        temp+="<img src=\""+items[i]["ImageName"]+"\" width=\"250\">"
        temp+="<p><strong>Caption: </strong>"+items[i]["Caption"]+"</p>";
        temp+="</div>";
        temp+="</div>";
    }
    divResults.innerHTML = temp;
}
console.log("Script loaded");
