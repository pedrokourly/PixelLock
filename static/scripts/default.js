// Função para obter o tema salvo
function getStoredTheme() {
    return localStorage.getItem('theme');
}

// Função para salvar o tema
function setStoredTheme(theme) {
    localStorage.setItem('theme', theme);
}

// Função para aplicar o tema usando Bootstrap (data-bs-theme)
function setTheme(theme) {
    document.documentElement.setAttribute('data-bs-theme', theme);
}

// Detecta preferência do sistema
function getPreferredTheme() {
    const storedTheme = getStoredTheme();
    if (storedTheme) {
        return storedTheme;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

// Aplica o tema ao carregar a página
const themeToggleButton = document.getElementById('theme-checkbox');
const currentTheme = getPreferredTheme();
setTheme(currentTheme);
if (currentTheme === 'dark') {
    themeToggleButton.checked = true;
} else {
    themeToggleButton.checked = false;
}

// Atualiza o tema ao mudar o switch
if (themeToggleButton) {
    themeToggleButton.addEventListener('change', () => {
        const newTheme = themeToggleButton.checked ? 'dark' : 'light';
        setStoredTheme(newTheme);
        setTheme(newTheme);
    });
}

// Atualiza o tema se a preferência do sistema mudar (caso não tenha tema salvo)
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    if (!getStoredTheme()) {
        setTheme(getPreferredTheme());
        themeToggleButton.checked = getPreferredTheme() === 'dark';
    }
});