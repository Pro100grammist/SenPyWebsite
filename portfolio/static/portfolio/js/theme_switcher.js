import { THEME, PREFERS_COLOR_SHCEME_DARK, DARK, LIGHT } from "./constants.js";

export class ThemeToggle {

    #toggleButton

    constructor() {
        this.#toggleButton = document.querySelector('.btn-theme-swithcer');
        const initThemeValue = this.#getInitThemeValue();
        document.body.dataset.theme = initThemeValue;
        
        this.#updateThemeSwitchButton(initThemeValue);

        this.#toggleButton.addEventListener('click', this.#toggleTheme);

    }
    
    #getInitThemeValue = () => {
        const preSetteledThemeValue = localStorage.getItem(THEME);
        const prefersDarkSchema = window.matchMedia(PREFERS_COLOR_SHCEME_DARK);

        if (preSetteledThemeValue) {
            return preSetteledThemeValue;
        }

        if (prefersDarkSchema.matches) {
            return DARK;
        }

        return LIGHT;
    }

    #updateThemeSwitchButton = (theme) => {
        const buttonText = theme === DARK ? LIGHT : DARK;
        this.#toggleButton.setAttribute('aria-label', buttonText);
        this.#toggleButton.innerText = buttonText;
    }

    #toggleTheme = () => {
        const newTheme = document.body.dataset.theme === DARK ? LIGHT : DARK;

        this.#updateThemeSwitchButton(newTheme);

        document.body.dataset.theme = newTheme;

        localStorage.setItem(THEME, newTheme);
    }
    


}