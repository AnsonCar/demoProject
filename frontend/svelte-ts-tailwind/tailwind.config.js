import { dark } from 'daisyui/src/theming/themes';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {}
  },
  plugins: [require('daisyui'),],
  daisyui: {
    themes: [
      {
        ...require("daisyui/src/theming/themes"),
        ...require("./theme.config")
      }
    ],
  },
};