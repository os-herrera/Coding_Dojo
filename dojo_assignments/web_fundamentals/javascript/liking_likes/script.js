function increment(){
  var neilLikes = document.querySelector('#neil-likes')
  console.log(neilLikes.innerText) 
  var likeCount = parseInt(neilLikes.innerText)
  likeCount ++ 
  neilLikes.innerText=likeCount
  
}

function increment2(){
  var nicholeLikes = document.querySelector('#nichole-likes')
  console.log(nicholeLikes.innerText) 
  var likeCount = parseInt(nicholeLikes.innerText)
  likeCount ++ 
  nicholeLikes.innerText=likeCount
  
}

function increment3(){
  var jimLikes = document.querySelector('#jim-likes')
  console.log(jimLikes.innerText) 
  var likeCount = parseInt(jimLikes.innerText)
  likeCount ++ 
  jimLikes.innerText=likeCount
  
}