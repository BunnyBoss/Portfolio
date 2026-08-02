/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#06080F",
        secondary: "#9CA3AF",
        tertiary: "#0F1318",
        "black-100": "#151A22",
        "black-200": "#0A0E14",
        "white-100": "#f3f3f3",
        accent: {
          DEFAULT: "#A8C4D4",
          secondary: "#D4A574",
        },
      },
      boxShadow: {
        card: "0 8px 32px rgba(168, 196, 212, 0.08)",
      },
      screens: {
        xs: "450px",
      },
      backgroundImage: {
        "hero-pattern": "url('/herobg.png')",
      },
      fontFamily: {
        heading: ["Outfit", "Inter", "sans-serif"],
      },
    },
  },
  plugins: [],
};
