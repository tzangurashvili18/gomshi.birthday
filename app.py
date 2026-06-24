import streamlit as st
import base64
import time
from pathlib import Path

st.set_page_config(
    page_title="Happy Birthday Gomshi!",
    page_icon="🎷",
    layout="centered"
)

# ── Commschool brand colors ──────────────────────────────────────────────────
CS_GREEN  = "#00C220"
CS_DARK   = "#1A1A1A"
CS_CARD   = "#222222"
CS_TEXT   = "#F5F5F5"
CS_MUTED  = "#888888"

st.markdown(f"""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

  html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {{
      background-color: {CS_DARK} !important;
      font-family: 'Inter', sans-serif;
  }}

  [data-testid="stAppViewContainer"] > .main {{
      background-color: {CS_DARK};
  }}

  /* hide default streamlit chrome */
  #MainMenu, footer, header {{ visibility: hidden; }}

  .cs-logo-wrap {{
      display: flex;
      justify-content: center;
      margin-bottom: 8px;
  }}
  .cs-logo-wrap img {{
      width: 100px;
      border-radius: 16px;
  }}

  .cs-tag {{
      text-align: center;
      font-size: 12px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: {CS_GREEN};
      font-weight: 700;
      margin-bottom: 24px;
  }}

  .cs-hero {{
      text-align: center;
      margin-bottom: 36px;
  }}
  .cs-hero h1 {{
      font-size: clamp(2.4rem, 8vw, 4rem);
      font-weight: 900;
      color: {CS_TEXT};
      line-height: 1.1;
      margin: 0 0 8px;
  }}
  .cs-hero h1 span {{
      color: {CS_GREEN};
  }}
  .cs-hero p {{
      font-size: 1.05rem;
      color: {CS_MUTED};
      margin: 0;
  }}

  .cs-card {{
      background: {CS_CARD};
      border-radius: 20px;
      padding: 32px 28px;
      margin-bottom: 24px;
      border: 1px solid #2e2e2e;
  }}

  .cs-card h3 {{
      color: {CS_GREEN};
      font-size: 0.75rem;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      margin: 0 0 16px;
      font-weight: 700;
  }}

  .cs-card p {{
      color: {CS_TEXT};
      font-size: 1.05rem;
      line-height: 1.7;
      margin: 0;
  }}

  .cs-quote {{
      border-left: 3px solid {CS_GREEN};
      padding-left: 16px;
      color: {CS_MUTED};
      font-style: italic;
      font-size: 0.95rem;
      margin-top: 16px;
  }}

  .cs-player-label {{
      color: {CS_GREEN};
      font-size: 0.75rem;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      font-weight: 700;
      margin-bottom: 12px;
  }}

  audio {{
      width: 100%;
      border-radius: 12px;
      accent-color: {CS_GREEN};
      background: #2a2a2a;
  }}

  .cs-footer {{
      text-align: center;
      color: {CS_MUTED};
      font-size: 0.8rem;
      margin-top: 40px;
      padding-bottom: 40px;
      letter-spacing: 1px;
  }}
  .cs-footer span {{
      color: {CS_GREEN};
  }}

  /* confetti canvas */
  #confetti-canvas {{
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      pointer-events: none;
      z-index: 9999;
  }}
</style>

<!-- Confetti -->
<canvas id="confetti-canvas"></canvas>
<script>
(function() {{
  const canvas = document.getElementById('confetti-canvas');
  const ctx    = canvas.getContext('2d');
  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;
  window.addEventListener('resize', () => {{
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
  }});

  const COLORS = ['{CS_GREEN}','#ffffff','#1A1A1A','#00b81e','#ccff99'];
  const pieces = Array.from({{length: 120}}, () => ({{
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height - canvas.height,
    r: Math.random() * 7 + 4,
    d: Math.random() * 80 + 20,
    color: COLORS[Math.floor(Math.random() * COLORS.length)],
    tilt: Math.random() * 10 - 10,
    tiltAngle: 0,
    tiltSpeed: Math.random() * 0.1 + 0.05
  }}));

  let angle = 0;
  let frame = 0;
  const MAX_FRAMES = 300;

  function draw() {{
    if (frame > MAX_FRAMES) {{ ctx.clearRect(0,0,canvas.width,canvas.height); return; }}
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    angle += 0.01;
    frame++;
    pieces.forEach(p => {{
      p.tiltAngle += p.tiltSpeed;
      p.y += (Math.cos(angle + p.d) + 2) * 1.5;
      p.x += Math.sin(angle) * 1.2;
      p.tilt = Math.sin(p.tiltAngle) * 12;
      if (p.y > canvas.height) {{ p.y = -10; p.x = Math.random() * canvas.width; }}
      ctx.beginPath();
      ctx.lineWidth = p.r;
      ctx.strokeStyle = p.color;
      ctx.moveTo(p.x + p.tilt + p.r / 2, p.y);
      ctx.lineTo(p.x + p.tilt, p.y + p.tilt + p.r / 2);
      ctx.stroke();
    }});
    requestAnimationFrame(draw);
  }}
  draw();
}})();
</script>
""", unsafe_allow_html=True)


# ── Logo ─────────────────────────────────────────────────────────────────────
logo_path = Path("Logo.jpg")
if logo_path.exists():
    with open(logo_path, "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <div class="cs-logo-wrap">
        <img src="data:image/jpeg;base64,{logo_b64}" alt="Commschool logo"/>
    </div>""", unsafe_allow_html=True)



# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cs-hero">
  <h1>Happy Birthday<br><span>Gomshi 🎷</span></h1>
  <p>From the whole Commschool crew — with love</p>
</div>
""", unsafe_allow_html=True)

# ── Audio Player ──────────────────────────────────────────────────────────────
audio_path = Path("Happy Birthday Gomshi.mp3")
if audio_path.exists():
    with open(audio_path, "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode()
    st.markdown('<div class="cs-player-label">🎵 Your Birthday Song</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <audio controls autoplay>
      <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
    </audio>
    """, unsafe_allow_html=True)
else:
    st.warning("Place Happy_Birthday_Gomshi.mp3 in the same folder as app.py")

st.markdown("<br>", unsafe_allow_html=True)

# ── Message Card ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="cs-card">
  <h3>A message from the team</h3>
  <p>Gomshi, happy birthday from Commschool team! 🎉</p>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cs-footer">
  Made with ♥ by the <span>Commschool</span> Team · 2026
</div>
""", unsafe_allow_html=True)
