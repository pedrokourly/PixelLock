document.addEventListener("DOMContentLoaded", function () {
  const dropzone = document.getElementById("dropzone");
  const input = document.getElementById("imageUpload");
  const preview = document.getElementById("preview");

  if (dropzone && input) {
    dropzone.addEventListener("click", () => input.click());
    dropzone.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropzone.classList.add("bg-light");
    });
    dropzone.addEventListener("dragleave", (e) => {
      e.preventDefault();
      dropzone.classList.remove("bg-light");
    });
    dropzone.addEventListener("drop", (e) => {
      e.preventDefault();
      dropzone.classList.remove("bg-light");
      if (e.dataTransfer.files.length) {
        input.files = e.dataTransfer.files;
        // Opcional: disparar evento de mudança para preview
        input.dispatchEvent(new Event("change"));
      }
    });
  }

  if (input && preview) {
    input.addEventListener("change", function () {
      preview.innerHTML = "";
      if (input.files && input.files[0]) {
        Array.from(input.files).forEach((file) => {
          if (file.type.startsWith("image/")) {
            const reader = new FileReader();
            reader.onload = function (e) {
              const img = document.createElement("img");
              img.src = e.target.result;
              img.className = "img-thumbnail m-2";
              img.style.maxWidth = "200px";
              img.style.maxHeight = "200px";
              preview.appendChild(img);
            };
            reader.readAsDataURL(file);
          }
        });
      }
    });
  }

  function getStoredTheme() {
    return localStorage.getItem("theme");
  }

  function setStoredTheme(theme) {
    localStorage.setItem("theme", theme);
  }

  function setTheme(theme) {
    document.body.setAttribute("data-bs-theme", theme);
  }

  function getPreferredTheme() {
    const storedTheme = getStoredTheme();
    if (storedTheme) {
      return storedTheme;
    }
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  // Seletores dos dois checkboxes
  const themeToggleOffcanvas = document.getElementById("theme-checkbox-offcanvas");
  const themeToggleNavbar = document.getElementById("theme-checkbox-navbar");
  const currentTheme = getPreferredTheme();
  setTheme(currentTheme);

  // Sincroniza ambos os checkboxes com o tema atual
  if (themeToggleOffcanvas) themeToggleOffcanvas.checked = currentTheme === "dark";
  if (themeToggleNavbar) themeToggleNavbar.checked = currentTheme === "dark";

  // Função para atualizar ambos os checkboxes
  function syncThemeCheckboxes(checked) {
    if (themeToggleOffcanvas) themeToggleOffcanvas.checked = checked;
    if (themeToggleNavbar) themeToggleNavbar.checked = checked;
  }

  // Handler para mudança de tema
  function handleThemeChange(checked) {
    const newTheme = checked ? "dark" : "light";
    setStoredTheme(newTheme);
    setTheme(newTheme);
    syncThemeCheckboxes(checked);
  }

  if (themeToggleOffcanvas) {
    themeToggleOffcanvas.addEventListener("change", function () {
      handleThemeChange(this.checked);
    });
  }
  if (themeToggleNavbar) {
    themeToggleNavbar.addEventListener("change", function () {
      handleThemeChange(this.checked);
    });
  }

  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => {
    if (!getStoredTheme()) {
      const prefersDark = getPreferredTheme() === "dark";
      setTheme(prefersDark ? "dark" : "light");
      syncThemeCheckboxes(prefersDark);
    }
  });
});
