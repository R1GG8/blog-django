document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.querySelector('.nav-logo span');
    const themeIcon = document.querySelector('.nav-logo i');
    
    // Проверяем сохраненную тему в localStorage
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Устанавливаем начальную тему
    setTheme(currentTheme);
    
    // Обработчик клика по кнопке темы
    themeToggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        setTheme(newTheme);
        localStorage.setItem('theme', newTheme);
    });
    
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        
        // Меняем иконку
        if (theme === 'dark') {
            themeIcon.className = 'fa-solid fa-sun';
        } else {
            themeIcon.className = 'fa-solid fa-moon';
        }
    }
});