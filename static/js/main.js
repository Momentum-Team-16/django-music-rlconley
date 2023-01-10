console.log("js loaded");
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

const form = document.querySelector("#create-form");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  console.log("submitted");

  const formData = new FormData(form);
  // grabs data from the form to be put into the request body
  console.log("formData", formData);

  fetch("cards/new", {
    method: "POST",
    credentials: "same-origin",
    headers: {
      Accept: "application/json",
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": csrftoken,
    },
    body: formData,
    // include the data from the form in the body of the request
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log(data);
      const cardList = document.querySelector("#card-list");
      let newEl = document.createElement("li");
      newEl.innerText = `${data.card_title} held by ${data.card_owner}`;
      cardList.appendChild(newEl);
    });
});
