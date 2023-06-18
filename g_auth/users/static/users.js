const addInput = document.getElementById("inputGroup");
const profileDash = document.getElementById("dash-url");
// console.log(profileDashUrl.getAttribute("data-url"));
const profileDashUrl = profileDash.dataset.url;
const csrftoken = getCookie("csrftoken");

function penClick(e, clss) {
  //   const crrText = e.target.parentElement.previousElementSibling.outerText;

  const previosSiblingTXT = e.target.parentElement.previousElementSibling;

  const d_name = e.target.parentElement.getAttribute("d_name");
  if (previosSiblingTXT !== null) {
    const crrText = previosSiblingTXT.outerText;

    const addInputClone = addInput.cloneNode(true);
    addInputClone.classList.remove("d-none");
    addInputClone.setAttribute("d_name", d_name);
    addInputClone.firstElementChild.value = crrText;
    clss.parentElement.parentElement.replaceWith(addInputClone);

    const checkClick = document.getElementsByClassName("check-click");

    for (let index = 0; index < checkClick.length; index++) {
      const checkClickelement = checkClick[index];
      checkClickelement.addEventListener("click", (ev) => {
        const sec_d_name = ev.target.parentElement.getAttribute("d_name");
        if (ev.target.parentElement.firstElementChild.value !== undefined) {
          const value_ = ev.target.parentElement.firstElementChild.value;
          CheckClickFn(ev, sec_d_name, value_);
        }
      });
    }
  }
}

const CheckClickFn = (e, name_, value_) => {
  //   e.preventDefault();

  const bData = JSON.stringify({ name: name_, value: value_ });
  console.log(bData);

  // e.target.firstElementChild.style.width = 25;
  // e.target.firstElementChild.style.height = 25;
  // e.target.firstElementChild.style.color = "#38ffee";
  //   e.target.firstElementChild.style.color = "red";

  fetch(profileDashUrl, {
    method: "POST",
    body: bData,
    headers: {
      "X-CSRFToken": csrftoken,
      "content-type": "application/json",
    },
  })
    .then((load) => load.json())
    .then((res) => {
      const status = res["status"];
      const msg = res["msg"];

      if (status === "ok") {
        e.target.firstElementChild.style.width = 25;
        e.target.firstElementChild.style.height = 25;
        e.target.firstElementChild.style.color = "#38ffee";
        checkAlert(msg, "alert-dark");
      }
      if (status === "bad") {
        e.target.firstElementChild.style.color = "red";
        checkAlert(msg, "alert-warning");
      }
    })
    .catch((err) => {
      return err.message;
    });
};

const checkAlert = (msg, cls, sec = 5) => {
  let seconds = 1000 * sec;
  const aletArea = document.getElementById("aletArea");
  const alertElement = document.createElement("div");
  alertElement.classList.add("alert", cls);
  alertElement.setAttribute("role", "alert");
  alertElement.innerHTML = msg;
  aletArea.insertAdjacentElement("afterbegin", alertElement);
  setTimeout(() => {
    alertElement.remove();
    // aletArea.remove();
  }, seconds);
};

document.addEventListener("DOMContentLoaded", () => {
  const penBtn = document.getElementsByClassName("pen-btn");
  const penBtnSvg = document.getElementsByClassName("pen-btn-svg");

  for (let index = 0; index < penBtnSvg.length; index++) {
    const penCrr = penBtnSvg[index];
    penCrr.addEventListener("click", (e) => penClick(e, penCrr));
  }
});

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
