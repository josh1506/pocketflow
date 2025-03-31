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
            danger: colors.red["600"],
            dangerHover: colors.red["500"],
        },
        extend: {},
    },
    plugins: [],
}

