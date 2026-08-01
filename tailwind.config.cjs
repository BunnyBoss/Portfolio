/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#030303",
        secondary: "#b3b3b3",
        tertiary: "#111111",
        "black-100": "#1a1a1a",
        "black-200": "#0a0a0a",
        "white-100": "#f3f3f3",
        accent: {
          DEFAULT: "#00e5ff",
          secondary: "#9d4edd",
        },
      },
      boxShadow: {
        card: "0px 20px 80px -10px rgba(0, 0, 0, 0.8)",
      },
      screens: {
        xs: "450px",
      },
      backgroundImage: {
        "hero-pattern": "url('/herobg.png')",
      },
    },
  },
  plugins: [],
};
