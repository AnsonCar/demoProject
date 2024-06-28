/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui'),],
  daisyui: {
    themes: [
      {
        "carhyme-light" : {
          ...require("./theme.config")["carhyme-light"]
        }
      },
      {
        "carhyme-dark" : {
          ...require("./theme.config")["carhyme-dark"]
        }
      },
      "light", "dark"
    ],
  },
}