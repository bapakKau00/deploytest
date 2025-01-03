import streamlit as st
import streamlit.components.v1 as components

st.title("BankingBuddy with Animated Background")

# HTML and JavaScript for Particles Animation
particles_html = """
<script src="https://cdn.jsdelivr.net/npm/particles.js"></script>
<div id="particles-js" style="position: fixed; width: 100%; height: 100%; z-index: -1;"></div>

<script>
particlesJS("particles-js", {
    "particles": {
        "number": { "value": 80, "density": { "enable": true, "value_area": 800 } },
        "color": { "value": "#ffffff" },
        "shape": {
            "type": "circle",
            "stroke": { "width": 0, "color": "#000000" },
            "polygon": { "nb_sides": 5 },
        },
        "opacity": { "value": 0.5, "random": false },
        "size": { "value": 3, "random": true },
        "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",
            "opacity": 0.4,
            "width": 1,
        },
        "move": {
            "enable": true,
            "speed": 6,
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "attract": { "enable": false },
        },
    },
    "interactivity": {
        "detect_on": "canvas",
        "events": {
            "onhover": { "enable": true, "mode": "repulse" },
            "onclick": { "enable": true, "mode": "push" },
        },
        "modes": {
            "repulse": { "distance": 100, "duration": 0.4 },
            "push": { "particles_nb": 4 },
        },
    },
    "retina_detect": true,
});
</script>
"""

# Insert the particle animation into the app
components.html(particles_html, height=0)

st.write("Enjoy the particle animation in the background!")
