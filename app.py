import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine Surprise 💖", layout="wide")

her_name = "Poojiiii"
your_name = "Your King"

# Random beautiful flower images from Unsplash
background_image = "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1470&q=80"

photos = [
    "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1470&q=80",
    "https://images.unsplash.com/photo-1471357674240-e1a485acb3e1?auto=format&fit=crop&w=1470&q=80",
    "https://images.unsplash.com/photo-1493244040629-496f6d136cc3?auto=format&fit=crop&w=1470&q=80"
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
    overflow:hidden;
    font-family: 'Roboto', sans-serif;
}}
body {{
    background: url('{background_image}') center/cover no-repeat;
    max-width:100vw;
    max-height:100vh;
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
    width:90vw; height:90vh;
    top:50%; left:50%;
    transform:translate(-50%, -50%);
    display:none;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    z-index:2;
    text-align:center;
    color:black;
}}
.screen h1, .screen p {{
    font-family: 'Dancing Script', cursive;
    font-size:2em;
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
    padding:12px 25px;
    font-size:20px;
    font-family: 'Roboto', sans-serif;
}}
#yesBtn {{ background-color:#ff69b4; color:white; }}
#noBtn {{ background-color:#c71585; color:white; position:absolute; top:50%; left:55%; }}
.heart {{ position:absolute; font-size:30px; cursor:pointer; }}
#countdown {{ position:absolute; top:20px; left:50%; transform:translateX(-50%); font-size:28px; background:rgba(0,0,0,0.3); padding:8px 15px; border-radius:20px; color:white; font-weight:bold; z-index:3; }}
</style>
</head>
<body>

<div class="glass"></div>
<div id="slideshow"></div>
<div id="countdown"></div>

<!-- Screens -->
<div id="gameScreen" class="screen">
    <h1>Collect Hearts to Unlock Quiz 💌</h1>
    <div id="heartsContainer" style="width:100%; height:60%; position:relative;"></div>
</div>
<div id="quizScreen" class="screen">
    <h1>Quick Quiz 🌸</h1>
    <p>Do you love me more than chocolate? 🍫</p>
    <button onclick="showProposal()">Yes! 💖</button>
</div>
<div id="proposalScreen" class="screen">
    💖 Poojjiii, Will You Be My Valentine? 💍<br>
    <button id="yesBtn" onclick="sayYes()">YESSS 💖</button>
    <button id="noBtn">NO 😭</button>
</div>

<script>
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

function showGame(){{
    const screen = document.getElementById('gameScreen');
    screen.style.display='flex';
    const container = document.getElementById('heartsContainer');
    let hearts=[];
    for(let i=0;i<10;i++){{
        let heart = document.createElement('div');
        heart.className='heart';
        heart.innerHTML='❤️';
        heart.style.left=Math.random()*70+'vw';
        heart.style.top=Math.random()*50+'vh';
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

function showProposal(){{
    document.getElementById('quizScreen').style.display='none';
    const screen = document.getElementById('proposalScreen');
    screen.style.display='flex';
    const noBtn = document.getElementById('noBtn');
    noBtn.addEventListener('mouseover',()=>{{
        noBtn.style.left=Math.random()*60+'vw';
        noBtn.style.top=Math.random()*50+'vh';
    }});
}}
function sayYes(){{
    const screen = document.getElementById('proposalScreen');
    screen.innerHTML=`<h1 style="font-size:50px;">💖 YOU SAID YES! 💖<br>I Love You Forever {her_name} 💍</h1>`;
    for(let i=0;i<50;i++){{
        let heart = document.createElement('div');
        heart.className='heart';
        heart.innerHTML='❤️';
        heart.style.left=Math.random()*100+'vw';
        heart.style.top=Math.random()*100+'vh';
        heart.style.fontSize=(Math.random()*30+15)+'px';
        document.body.appendChild(heart);
    }}
}}

window.onload = function(){{ startSlideshow(); startCountdown(); showGame(); }};
</script>

</body>
</html>
"""

components.html(html_code, height=700)
