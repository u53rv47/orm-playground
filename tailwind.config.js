/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      screens: {
        'sm': '640px',  
        'md': '768px',  
        'lg': '1024px',  
        'xl': '1280px',  
        '2xl': '1536px',
      },
      borderWidth: {
        DEFAULT: '1px',
        '0': '0',
        '2': '2px',
        '3': '3px',
        '4': '4px',
        '5': '5px',
        '8': '8px',
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}