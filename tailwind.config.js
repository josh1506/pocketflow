/** @type {import('tailwindcss').Config} */
const colors = require("tailwindcss/colors")

module.exports = {
    content: [
        "./templates/**/*.{html,js}",
        './app/**/templates/**/*.html'
    ],
    theme: {
        colors: {
            ...colors,
            primary: "#EB8317",
            primaryHover: "#F29B44",
            secondary: "#F4F6FF",
            secondaryHover: "#FFFFFF",
        },
        extend: {},
    },
    plugins: [],
}

