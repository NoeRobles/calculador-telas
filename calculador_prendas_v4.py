import streamlit as st

st.title("🧵 Calculador de Tela")

st.markdown("Seleccioná el tipo de prenda y cargá tus medidas. Te diremos cuánta tela necesitás en base al ancho disponible.")

# Selector de tipo de prenda
tipo_prenda = st.selectbox(
    "Seleccioná la prenda que vas a confeccionar:",
    [
        "Remera mangas cortas",
        "Remera mangas largas",
        "Buzo o suéter sin capucha",
        "Buzo o suéter con capucha",
        "Chaleco básico con capucha",
        "Chaleco básico sin capucha",
        "Pantalón largo",
        "Pantalón corto"
    ]
)

st.subheader("📏 Tus medidas")
hombros = st.number_input("Ancho de hombros (cm)", min_value=30, max_value=60, value=40)
cintura = st.number_input("Contorno de cintura (cm)", min_value=60, max_value=140, value=90)
cadera = st.number_input("Contorno de cadera (cm)", min_value=70, max_value=160, value=100)
pecho = st.number_input("Contorno de pecho (cm)", min_value=70, max_value=140, value=95)
largo = st.number_input("Largo deseado de la prenda (cm)", min_value=40, max_value=130, value=100)

st.markdown("---")
st.subheader("📐 Resultados para distintos anchos de tela")

anchos_tela = [140, 150, 160, 170, 180]  # en cm
margen_seguridad = 10  # cm

for ancho in anchos_tela:
    extra = 0

    if "pantalón" in tipo_prenda.lower():
        pretina = st.checkbox("¿El pantalón tiene pretina?", value=True, key=f"pretina_{ancho}")
        bolsillos = st.checkbox("¿Tiene bolsillos?", value=False, key=f"bolsillos_{ancho}")

        # nuevo cálculo: cadera/10 + 2 para cada pieza delantera y trasera
        ajuste_entrepierna = (cadera / 10) + 2
        cadera_ajustada = cadera + ajuste_entrepierna * 2  # delantero y trasero

        if cadera_ajustada <= ancho:
            largo_base = largo + margen_seguridad
        else:
            largo_base = (largo + margen_seguridad) * 2

        # Agregados por cintura
        if pretina:
            extra += 30
        else:
            extra += 15

        if bolsillos:
            extra += 20

        cantidad_cm = largo_base + extra

    elif "buzo" in tipo_prenda.lower() or "capucha" in tipo_prenda.lower():
        cantidad_cm = largo + margen_seguridad + 20  # buzos o prendas con puños y cintura

    else:
        cantidad_cm = largo + margen_seguridad  # remeras y prendas simples

    cantidad_m = cantidad_cm / 100

    st.markdown(f"### Ancho de tela: {ancho} cm")
    st.success(f"Necesitás: **{cantidad_m:.2f} metros**")
    st.markdown(f"💡 Consejo: Sumá 10 cm más si sos principiante o vas a usar estampas (usar {cantidad_m + 0.1:.2f} m)")
    st.markdown("---")
