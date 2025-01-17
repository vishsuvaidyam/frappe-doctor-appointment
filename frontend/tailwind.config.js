/** @type {import('tailwindcss').Config} */
export default {
  presets: [require("frappe-ui/src/utils/tailwind.config")],
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
        "./node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}",
        "../node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}",
    ],
  content: ["./src/**/*.{html,jsx,tsx,vue,js,ts}"],
  theme: {
    extend: {},
  },
  plugins: [],
}

