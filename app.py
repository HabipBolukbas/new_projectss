# app.py
import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Duygu Analizi Uygulaması",
    page_icon="😊"
)

st.title("Duygu Analizi Uygulaması")
st.write("Metin girin ve duygu analizi yapın!")

# API endpoint
API_URL = "http://backend:8000/analyze/"

# Kullanıcı girişi
text_input = st.text_area("Analiz etmek istediğiniz metni girin:", height=150)

if st.button("Analiz Et"):
    if text_input:
        try:
            response = requests.post(
                API_URL,
                json={"text": text_input}
            )
            result = response.json()
            
            # Sonuçları göster
            st.subheader("Sonuç:")
            st.write(f"Metin: {result['text']}")
            
            # Duyguya göre renkli gösterim
            if result['sentiment'] == 'positive':
                st.success(f"📈 Pozitif Duygu (%{result['score']*100:.2f})")
            else:
                st.error(f"📉 Negatif Duygu (%{result['score']*100:.2f})")
                
        except Exception as e:
            st.error(f"Hata oluştu: {str(e)}")
    else:
        st.warning("Lütfen analiz etmek için bir metin girin.")