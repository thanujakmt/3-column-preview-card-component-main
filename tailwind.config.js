
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./previewcardapp/**/*.{html,js}"],
  theme: {
    extend: {
      colors : {
        'Bright_orange': 'hsl(31, 77%, 52%)',
        'Dark_cyan': 'hsl(184, 100%, 22%)',
        'Very_dark_cyan': 'hsl(179, 100%, 13%)',
        'Transparent_white' : 'hsla(0, 0%, 100%, 0.75)',
        'Very_light_gray' : 'hsl(0, 0%, 95%)',
        'black':'#0000'
      },
      fontFamily : {
        'lexend' : 'Lexend Deca,sans-serif',
        'shoulders' : 'Big Shoulders Display,sans-serif'
      }
    },
  },
  plugins: [],
}
