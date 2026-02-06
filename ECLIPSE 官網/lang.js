let currentLang = localStorage.getItem("lang") || "zh";

const toggleBtn = document.getElementById("langToggle");
const elements = document.querySelectorAll("[data-zh]");

function applyLang() {
  elements.forEach(el => {
    el.textContent = el.dataset[currentLang];
  });
  toggleBtn.textContent = currentLang === "zh" ? "EN" : "中文";
}

toggleBtn.addEventListener("click", () => {
  currentLang = currentLang === "zh" ? "en" : "zh";
  localStorage.setItem("lang", currentLang);
  applyLang();
});

applyLang();
