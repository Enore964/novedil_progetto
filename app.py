import streamlit as st

# Configurazione della pagina
st.set_page_config(layout="wide", page_title="Nuovo Layout Novedil")

# Stile CSS personalizzato per simulare il nuovo look
st.markdown("""
<style>
    .main {background-color: #f9f9f9;}
    .hero-container {
        background-color: #2c3e50;
        color: white;
        padding: 50px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 30px;
    }
    .cta-button {
        background-color: #e74c3c;
        color: white;
        padding: 15px 30px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.2em;
    }
    .service-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.image("https://www.novedilcostruzionisrl.it/wp-content/uploads/2023/10/logo-novedil.png", width=150)
st.divider()

# --- HERO SECTION (La differenza principale) ---
st.markdown("""
<div class="hero-container">
    <h1>Costruiamo il tuo futuro, ristrutturiamo il tuo presente.</h1>
    <p style="font-size: 1.2em;">40 anni di esperienza in Friuli. Soluzioni chiavi in mano con massima attenzione alla sicurezza e al risparmio energetico.</p>
    <br><br>
    <a href="#" class="cta-button">RICHIEDI UN PREVENTIVO GRATUITO</a>
</div>
""", unsafe_allow_html=True)

# --- SEZIONE SERVIZI ---
st.header("I nostri Servizi")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <h3>🏢 Nuove Costruzioni</h3>
        <p>Realizziamo la tua villa o palazzina su misura, dalla progettazione alla consegna.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <h3>🛠️ Ristrutturazioni</h3>
        <p>Rinnoviamo i tuoi spazi abitativi con materiali di alta qualità e tecnologie moderne.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <h3>⚡ Efficienza Energetica</h3>
        <p>Riqualifichiamo il tuo immobile per abbattere i consumi e aumentare il comfort.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- SEZIONE ANNUNCI (Anteprima) ---
st.header("Ultimi Immobili in Vendita")
st.warning("Qui inseriremmo le schede degli immobili con foto grandi e prezzi chiari.")
