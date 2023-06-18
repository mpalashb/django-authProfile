document.addEventListener("DOMContentLoaded", () => {
  const getRegisterF = document.getElementById("registerA");
  if (getRegisterF) {
    const getInputOnlyByReg = getRegisterF.querySelectorAll("input");

    for (let index = 0; index < getInputOnlyByReg.length; index++) {
      const Ielement = getInputOnlyByReg[index];

      if (Ielement.type === "hidden") {
        ("");
      } else {
        Ielement.classList.add("form-control");
      }
    }
  }

  const getLoginOAuth = document.getElementById("logOauth");

  if (getLoginOAuth) {
    const getInputOnlyByLogin = getLoginOAuth.querySelectorAll("input");

    for (let index = 0; index < getInputOnlyByLogin.length; index++) {
      const Lelement = getInputOnlyByLogin[index];

      switch (Lelement.type) {
        case "hidden":
          break;
        case "checkbox":
          break;

        default:
          Lelement.classList.add("form-control");
      }

      //   if (Lelement.type === "hidden") {
      //     ("");
      //   } else {
      //     Lelement.classList.add("form-control");
      //   }
    }
  }
});
