import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine Surprise 💖", layout="wide")

her_name = "My Princess"
your_name = "Your King"

# Background and slideshow images
# Replace this URL with your own photo URL to change the background
background_image = "https://images.unsplash.com/photo-1520362958006-c863d5e1d2ed?auto=format&fit=crop&w=1470&q=80"
photos = [
    # Replace these URLs with your own photos
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e",
    "https://images.unsplash.com/photo-1507874457470-272b3c8d8ee2",
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e"
]

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Valentine Surprise 💖</title>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
<style>
html, body {{
    margin:0; padding:0;
    width:100%; height:100%;
    overflow:hidden;  /* Makes it non-scrollable */
    font-family: 'Roboto', sans-serif;
}}
body {{
    background: url('{background_image}') center/cover no-repeat;
}}
.glass {{
    position:absolute;
    width:100%; height:100%;
    backdrop-filter: blur(15px) brightness(1.2);
    background: rgba(255,255,255,0.2);
    z-index:0;
}}
.screen {{
    position:absolute;
    width:100%; height:100%;
    top:0; left:0;
    display:none;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    z-index:2;
    text-align:center;
}}
.screen h1, .screen p {{
    font-family: 'Dancing Script', cursive;
    font-size:3em;
    color:#ff1493;
    margin:0.5em 0;
}}
#slideshow {{
    position:absolute;
    width:100%; height:100%;
    z-index:1;
    overflow:hidden;
}}
.slide {{
    position:absolute;
    width:100%; height:100%;
    background-size:cover;
    background-position:center;
    opacity:0;
    transition: opacity 1.5s;
}}
button {{
    cursor:pointer;
    border:none;
    border-radius:15px;
    padding:15px 30px;
    font-size:25px;
    font-family: 'Roboto', sans-serif;
}}
#yesBtn {{ background-color:#ff69b4; color:white; }}
#noBtn {{ background-color:#c71585; color:white; position:absolute; top:50%; left:55%; }}
.heart {{ position:absolute; font-size:40px; cursor:pointer; }}
#countdown {{ position:absolute; top:20px; left:50%; transform:translateX(-50%); font-size:35px; background:rgba(255,255,255,0.3); padding:10px 20px; border-radius:20px; color:#800000; font-weight:bold; z-index:3; }}
</style>
</head>
<body>

<div class="glass"></div>
<div id="slideshow"></div>
<div id="countdown"></div>

<!-- Screens -->
<div id="gameScreen" class="screen">
    <h1>Collect Hearts to Unlock Quiz 💌</h1>
    <div id="heartsContainer" style="width:100%; height:70%; position:relative;"></div>
</div>
<div id="quizScreen" class="screen">
    <h1>Quick Quiz 🌸</h1>
    <p>Do you love me more than chocolate? 🍫</p>
    <button onclick="showProposal()">Yes! 💖</button>
</div>
<div id="proposalScreen" class="screen">
    💖 {her_name}, Will You Be My Valentine? 💍<br>
    <button id="yesBtn" onclick="sayYes()">YESSS 💖</button>
    <button id="noBtn">NO 😭</button>
</div>

<script>
// Slideshow
const photos = {photos};
function startSlideshow(){{
    const container = document.getElementById('slideshow');
    photos.forEach(url => {{
        let div = document.createElement('div');
        div.className='slide';
        div.style.backgroundImage='url('+url+')';
        container.appendChild(div);
    }});
    let current=0;
    container.children[current].style.opacity=1;
    setInterval(()=>{{
        container.children[current].style.opacity=0;
        current=(current+1)%container.children.length;
        container.children[current].style.opacity=1;
    }},4000);
}}

// Countdown
function startCountdown(){{
    const countdown = document.getElementById('countdown');
    const target = new Date(new Date().getFullYear(),1,14);
    setInterval(()=>{{
        let now = new Date();
        let diff = target - now;
        let d=Math.floor(diff/1000/60/60/24);
        let h=Math.floor(diff/1000/60/60)%24;
        let m=Math.floor(diff/1000/60)%60;
        let s=Math.floor(diff/1000)%60;
        countdown.innerHTML=`Valentine's in ${{d}}d ${{h}}h ${{m}}m ${{s}}s`;
    }},1000);
}}

// Heart Game
function showGame(){{
    const screen = document.getElementById('gameScreen');
    screen.style.display='flex';
    const container = document.getElementById('heartsContainer');
    let hearts=[];
    for(let i=0;i<10;i++){{
        let heart = document.createElement('div');
        heart.className='heart';
        heart.innerHTML='❤️';
        heart.style.left=Math.random()*85+'vw';
        heart.style.top=Math.random()*60+'vh';
        heart.onclick = function(){{
            heart.style.display='none';
            hearts[i]=true;
            if(hearts.every(Boolean)){{
                screen.style.display='none';
                document.getElementById('quizScreen').style.display='flex';
            }}
        }};
        container.appendChild(heart);
        hearts.push(false);
    }}
}}

// Proposal
function showProposal(){{
    document.getElementById('quizScreen').style.display='none';
    const screen = document.getElementById('proposalScreen');
    screen.style.display='flex';
    const noBtn = document.getElementById('noBtn');
    noBtn.addEventListener('mouseover',()=>{{
        noBtn.style.left=Math.random()*70+'vw';
        noBtn.style.top=Math.random()*70+'vh';
    }});
}}
function sayYes(){{
    const screen = document.getElementById('proposalScreen');
    screen.innerHTML=`<h1 style="font-size:60px;">💖 SHE SAID YES! 💖<br>I Love You Forever {her_name} 💍</h1>`;
    for(let i=0;i<50;i++){{
        let heart = document.createElement('div');
        heart.className='heart';
        heart.innerHTML='❤️';
        heart.style.left=Math.random()*100+'vw';
        heart.style.top=Math.random()*100+'vh';
        heart.style.fontSize=(Math.random()*40+20)+'px';
        document.body.appendChild(heart);
    }}
}}

// Initialize
window.onload = function(){{ startSlideshow(); startCountdown(); showGame(); }};
</script>

</body>
</html>
"""

components.html(html_code, height=1000)
