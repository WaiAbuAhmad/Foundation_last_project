function randomNumber(){
  random_value = [];
  while (random_value.length <40){
    random_number = Math.floor(Math.random()*80)+1;
    if (!random_value.includes(random_number)){
      random_value.push(random_number);
    }
 
  }
  return random_value;
}
function addAttribute(){
  attribute_id = randomNumber();
  for (i=0; i< 40; i++){
    document.getElementById(attribute_id[i]).setAttribute("disabled",true);
    document.getElementById(attribute_id[i]).setAttribute("class","fixed");
  }
}
function checkInputValue(){  
  x={};
  inputCount=document.getElementsByClassName("general");
  for (i=0;i<inputCount.length;i++){
    x[inputCount[i].id]=document.getElementById(inputCount[i].id).value;
    document.getElementById(inputCount[i].id).setAttribute("value","");

    }
  return x;  
  }
function checkCell(ID,VALUE){
  if (x[ID] == VALUE ) {
    document.getElementById(ID).setAttribute("disabled",true);
    document.getElementById(ID).setAttribute("class","fixed");
  }else{
    
    document.getElementById(ID).setAttribute("class","wrong");
  }
  
  if (inputCount.length == 0){
    location.replace("/Congratulations")
  }
}
  
  
