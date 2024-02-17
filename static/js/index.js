window.addEventListener("DOMContentLoaded", () => {
  function adjustTextareaHeight(textarea) {
    // Reset textarea height to auto to ensure it shrinks when content is removed
    textarea.style.height = "auto";
    // Set the height to scrollHeight if scrollHeight is greater than the current height, otherwise keep the current height
    textarea.style.height =
      textarea.scrollHeight > textarea.clientHeight
        ? textarea.scrollHeight + "px"
        : "auto";
  }
  const textareas = document.querySelectorAll("textarea");
  textareas.forEach((textarea) => {
    adjustTextareaHeight(textarea);
    textarea.rows = 0;
  });
  let liked = document.querySelectorAll(".is-liked")
  liked.forEach((like) => {
    if (like.innerHTML.trim() == "") {
        like.innerHTML = '<i class="fa-regular fa-heart"></i>'
    }
  });
  let form = document.querySelector('.user-info-form')
  if (form) {
    let file = document.querySelector('.clearablefileinput.form-control-file')
    file.style.display = 'block'
  }
});
const showTextarea = (element) => {
    if (element.textContent.trim() == 'Reply') {
        element.textContent = 'Hide';
        element.parentElement.nextElementSibling.style.display = 'block';
    }
    else{
        element.textContent = 'Reply';
        element.parentElement.nextElementSibling.style.display = 'none';
    }

};
const postFullShort = (element) => {
    let short = element.parentElement.parentElement.querySelector('.short-post')
    let full = element.parentElement.parentElement.querySelector('.full-post')
    if (element.textContent == "See More...") {
        element.textContent = "See Less"
        short.style.display = 'none';
        full.style.display = 'block';
    }else{
        element.textContent = "See More..."
        short.style.display = 'block';
        full.style.display = 'none';
    }
}

const maximizePost = (element) => {
    element.style.display = 'none';
    element.nextElementSibling.style.display = 'block';
    element.nextElementSibling.nextElementSibling.firstElementChild.textContent = 'See Less'
}
const minimizePost = (element) => {
    element.style.display = 'none';
    element.previousElementSibling.style.display = 'block';
    element.nextElementSibling.firstElementChild.textContent = 'See More...'
}


const showAnswers = (element) => {
  if (element?.textContent?.trim() == 'Answers') {
    element.textContent = 'Hide Answers';
    element.style.marginBottom = '10px';
    element.nextElementSibling.style.display = 'block';
  }else{
    element.textContent = 'Answers';
    element.nextElementSibling.style.display = 'none';
  }
}