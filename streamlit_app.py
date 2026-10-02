from __future__ import annotations

from pathlib import Path
import json
import pandas as pd
import streamlit as st

APP_NAME = "EUROMIQ"
BASE_DIR = Path(__file__).resolve().parent
LOGO_WHITE = BASE_DIR / "brand" / "euromiq_logo_white.png"
LOGO_BLUE = BASE_DIR / "brand" / "euromiq_logo_blue.png"

st.set_page_config(
    page_title="EUROMIQ · Demo pública",
    page_icon="✓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
:root{
  --navy:#062B56;--navy2:#073C76;--blue:#0B5DE9;--blue2:#064CC6;
  --blue-soft:#EEF5FF;--gold:#F3B61F;--ink:#102544;--muted:#6D7D95;
  --line:#D9E4F1;--bg:#F7FAFE;--card:#FFFFFF;--ok:#16754A;--ok-bg:#EAF7EF;
  --warn:#946B00;--warn-bg:#FFF6DE;--bad:#B4232D;--bad-bg:#FDECEE;
}
html,body,[class*="css"]{font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;}
.stApp{background:var(--bg);color:var(--ink);}
[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],#MainMenu{display:none!important;}
[data-testid="stAppViewContainer"]>.main,[data-testid="stMain"]{padding-top:0!important;margin-top:0!important;}
[data-testid="stMainBlockContainer"]{padding-top:1.45rem!important;}
.block-container{max-width:1380px;padding:1.45rem 1.65rem 3rem!important;margin-top:0!important;}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#052A54 0%,#06386E 62%,#06305E 100%);border-right:1px solid rgba(255,255,255,.06);box-shadow:12px 0 30px rgba(7,29,57,.13);}
[data-testid="stSidebar"] .block-container{padding:1rem .72rem 1rem!important;}
[data-testid="stSidebar"] *{color:#F5F8FC;}
[data-testid="stSidebarHeader"],[data-testid="stSidebarCollapseButton"],[data-testid="stSidebarCollapsedControl"]{display:none!important;}
[data-testid="stSidebar"] [data-testid="stImage"]{margin:.05rem .4rem .8rem!important;}
[data-testid="stSidebar"] [data-testid="stImage"] img{max-width:220px!important;width:100%!important;height:auto!important;margin:0 auto!important;display:block!important;}
[data-testid="stSidebar"] button{background:transparent!important;border:1px solid rgba(255,255,255,.18)!important;color:#E9F1FB!important;border-radius:10px!important;text-align:left!important;justify-content:flex-start!important;box-shadow:none!important;padding:.62rem .72rem!important;font-weight:650!important;margin-bottom:.15rem!important;}
[data-testid="stSidebar"] button:hover{background:rgba(255,255,255,.08)!important;color:#fff!important;}
[data-testid="stSidebar"] button[kind="primary"]{background:linear-gradient(90deg,#0A58DC,#0F66F2)!important;color:#fff!important;border-color:transparent!important;box-shadow:0 8px 18px rgba(8,77,194,.25)!important;}
.sidebar-kicker{color:#9FB8D7!important;font-size:.66rem;text-transform:uppercase;letter-spacing:.12em;font-weight:800;margin:1rem .45rem .4rem;}
.sidebar-account{background:rgba(3,28,57,.48);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:.78rem .82rem;margin:.75rem 0 .55rem;}
.sidebar-account strong{display:block;font-size:.9rem;color:#fff!important}.sidebar-account span{font-size:.76rem;color:#C8D7E9!important;}
.demo-pill{display:inline-flex;align-items:center;gap:.35rem;background:rgba(243,182,31,.14);border:1px solid rgba(243,182,31,.42);color:#FFD34A!important;border-radius:999px;padding:.33rem .58rem;font-size:.68rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase;margin:.1rem .35rem .8rem;}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:1rem;background:#fff;border:1px solid #E8EEF6;border-radius:16px;padding:.82rem 1rem;margin-bottom:1.15rem;box-shadow:0 5px 18px rgba(18,45,79,.035);}
.topbar-title{font-size:1.03rem;font-weight:800;color:var(--ink);}.topbar-sub{font-size:.77rem;color:var(--muted);margin-top:.12rem;}
.topbar-demo{display:inline-flex;align-items:center;background:#FFF6DE;color:#946B00;border:1px solid #F7DE99;border-radius:999px;padding:.36rem .62rem;font-size:.7rem;font-weight:800;white-space:nowrap;}
.eyebrow{font-size:.71rem;text-transform:uppercase;letter-spacing:.11em;font-weight:850;color:var(--blue);margin-bottom:.35rem;}
.hero-title2{font-size:2.05rem;font-weight:850;letter-spacing:-.025em;line-height:1.08;color:var(--ink);margin:.1rem 0 .4rem;}
.hero-copy2{font-size:.98rem;color:#60738E;line-height:1.55;max-width:780px;margin-bottom:.9rem;}
.panel-card{background:#fff;border:1px solid var(--line);border-radius:17px;padding:1.05rem 1.1rem;box-shadow:0 10px 28px rgba(18,44,79,.045);}
.panel-head{display:flex;align-items:center;gap:.7rem;margin-bottom:.7rem}.panel-icon{width:38px;height:38px;border-radius:12px;background:#EEF5FF;color:var(--blue);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:1.15rem;}
.panel-title{font-size:1.02rem;font-weight:800;color:var(--ink);}.panel-copy{font-size:.79rem;color:var(--muted);}
.profile-row{display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.65rem 0;border-top:1px solid #EDF1F6;font-size:.82rem;}
.profile-row:first-of-type{border-top:0}.profile-label{color:#334D70;font-weight:600}.profile-value{background:#EEF2F6;color:#5D6B7C;border-radius:999px;padding:.28rem .55rem;font-size:.72rem;white-space:nowrap;}.profile-value.ok{background:var(--ok-bg);color:var(--ok);}
.step-summary{display:grid;grid-template-columns:repeat(4,1fr);gap:0;background:#fff;border:1px solid var(--line);border-radius:16px;padding:.4rem;margin:.9rem 0 1rem;box-shadow:0 7px 22px rgba(20,46,82,.035);}
.step-item{display:flex;align-items:center;gap:.65rem;padding:.7rem .75rem;border-radius:12px;min-height:64px;}
.step-item.active{background:linear-gradient(90deg,#EEF5FF,#F8FBFF);box-shadow:inset 0 0 0 1px #D8E6FA;}
.step-num{width:34px;height:34px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#EAF0F7;color:#34506F;font-weight:800;flex:0 0 auto;}
.step-item.active .step-num{background:var(--blue);color:#fff;box-shadow:0 6px 14px rgba(11,93,233,.22);}
.step-item b{display:block;font-size:.84rem;color:var(--ink);}.step-item span{font-size:.72rem;color:#7B8BA0;}
.fake-upload{border:1.5px dashed #9EBCEA;background:linear-gradient(180deg,#F8FBFF,#F3F7FD);border-radius:16px;padding:2rem;text-align:center;margin:.5rem 0 1rem;}
.fake-upload .ico{font-size:2.15rem;color:#0B5DE9}.fake-upload b{display:block;color:#173553;margin:.35rem 0}.fake-upload span{font-size:.78rem;color:#74849A;}
.readonly-note{background:#FFF8E3;border:1px solid #F3D77A;color:#7C5A00;border-radius:12px;padding:.72rem .82rem;font-size:.8rem;font-weight:650;margin:.6rem 0 1rem;}
.status{display:inline-flex;border-radius:999px;padding:.25rem .52rem;font-size:.7rem;font-weight:800;}.status.blue{background:#EEF5FF;color:#0B5DE9}.status.green{background:#EAF7EF;color:#16754A}.status.yellow{background:#FFF6DE;color:#946B00}.status.grey{background:#EEF2F6;color:#5D6B7C}.status.red{background:#FDECEE;color:#B4232D}
.kpi{background:#fff;border:1px solid var(--line);border-radius:16px;padding:1rem 1.05rem;min-height:118px;box-shadow:0 8px 22px rgba(18,44,79,.035);}.kpi-label{font-size:.73rem;color:#6D7D95;font-weight:700}.kpi-value{font-size:2rem;font-weight:850;color:#102544;line-height:1.05;margin-top:.25rem}.kpi-foot{font-size:.72rem;color:#0B5DE9;margin-top:.35rem;font-weight:700}
.intro-shell{min-height:calc(100vh - 3rem);display:grid;grid-template-columns:1.08fr .92fr;border-radius:28px;overflow:hidden;background:linear-gradient(125deg,#031C3A 0%,#07376F 48%,#0A57B8 100%);box-shadow:0 26px 70px rgba(8,36,77,.18);border:1px solid rgba(255,255,255,.16);}
.intro-left{position:relative;padding:4rem 4rem 3rem;color:white;overflow:hidden;}.intro-left:before{content:"";position:absolute;width:530px;height:530px;border-radius:50%;right:-180px;top:-110px;background:radial-gradient(circle,rgba(31,121,240,.35),rgba(31,121,240,0) 66%);}.intro-left:after{content:"★  ★  ★\\A   ★   ★\\A ★   ★   ★";white-space:pre;position:absolute;right:2.4rem;top:7rem;color:#F3B61F;font-size:2.2rem;line-height:2.3;opacity:.9;transform:rotate(-8deg);}
.intro-left h1{font-size:3.2rem;line-height:1.03;max-width:610px;letter-spacing:-.035em;margin:2rem 0 1rem;position:relative;z-index:2}.intro-left p{font-size:1.07rem;line-height:1.6;color:#DDE9F7;max-width:620px;position:relative;z-index:2}.intro-rule{width:64px;height:5px;background:#F3B61F;border-radius:999px;margin:1.2rem 0;position:relative;z-index:2}.intro-badges{display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1.8rem;position:relative;z-index:2}.intro-badge{border:1px solid rgba(255,255,255,.24);background:rgba(255,255,255,.07);border-radius:999px;padding:.5rem .75rem;font-size:.76rem;font-weight:750;color:#fff}.intro-right{display:flex;align-items:center;padding:3rem 3.2rem;background:linear-gradient(180deg,rgba(10,77,157,.20),rgba(2,35,76,.36));}.intro-card{width:100%;background:rgba(6,49,101,.64);border:1px solid rgba(255,255,255,.22);border-radius:24px;padding:2rem;color:white;box-shadow:0 18px 46px rgba(0,20,55,.16);}.intro-card h2{font-size:2.15rem;margin:.5rem 0 .55rem}.intro-card p{color:#D6E3F4;line-height:1.5}.intro-label{color:#FFD13B;font-size:.76rem;font-weight:900;letter-spacing:.12em;text-transform:uppercase}.intro-feature{display:flex;gap:.7rem;align-items:flex-start;padding:.8rem 0;border-top:1px solid rgba(255,255,255,.12)}.intro-feature:first-of-type{margin-top:1rem}.intro-feature strong{font-size:.88rem}.intro-feature span{font-size:.74rem;color:#C9D8EA;display:block;margin-top:.1rem}.intro-lock{width:34px;height:34px;border-radius:10px;background:rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center;color:#FFD13B;flex:0 0 auto}.intro-card .stButton button{background:linear-gradient(90deg,#F5B719,#FFD03C)!important;color:#062B56!important;border:0!important;font-weight:900!important;min-height:54px!important;border-radius:12px!important;}
@media(max-width:1000px){.intro-shell{grid-template-columns:1fr}.intro-left{padding:2.4rem}.intro-right{padding:1rem 2rem 2.4rem}.step-summary{grid-template-columns:1fr 1fr}.block-container{padding:1rem!important}}
</style>
""",
    unsafe_allow_html=True,
)

DEMO_USER = {
    "id": 0,
    "name": "Eva María",
    "surname": "Martínez",
    "email": "demo@euromiq.eu",
    "organization": "EUROMIQ Demo",
    "professional_role": "Técnica de proyectos",
    "country": "España",
    "is_admin": False,
}

CASES = [
    {"id": "EXP-2026-001", "project_name": "Modernización de infraestructuras digitales", "fund": "FEDER", "country": "España", "status": "En revisión", "phase": "Revisión", "updated_at": "01/10/2026", "beneficiary": "Entidad pública regional", "amount": "1.280.000 €"},
    {"id": "EXP-2026-002", "project_name": "Transición energética en entidades locales", "fund": "FEDER", "country": "España", "status": "Completado", "phase": "Informe", "updated_at": "29/09/2026", "beneficiary": "Consorcio local", "amount": "845.000 €"},
    {"id": "EXP-2026-003", "project_name": "Formación para el empleo joven", "fund": "FSE+", "country": "España", "status": "Documentación", "phase": "Documentos", "updated_at": "27/09/2026", "beneficiary": "Entidad social", "amount": "415.000 €"},
    {"id": "EXP-2026-004", "project_name": "Desarrollo rural sostenible", "fund": "FEADER", "country": "España", "status": "Pendiente", "phase": "Configurar", "updated_at": "24/09/2026", "beneficiary": "Grupo de acción local", "amount": "660.000 €"},
]

DOCUMENTS = [
    {"Documento": "Memoria técnica del proyecto.pdf", "Tipo": "Justificación", "Expediente": "EXP-2026-001", "Estado": "Revisado", "Tamaño": "2,4 MB"},
    {"Documento": "Contrato de servicios.docx", "Tipo": "Contratación", "Expediente": "EXP-2026-001", "Estado": "Revisado", "Tamaño": "1,1 MB"},
    {"Documento": "Justificación de costes.xlsx", "Tipo": "Costes reales", "Expediente": "EXP-2026-001", "Estado": "Con observaciones", "Tamaño": "856 KB"},
    {"Documento": "Informe de ejecución.pdf", "Tipo": "Evidencia", "Expediente": "EXP-2026-002", "Estado": "Revisado", "Tamaño": "3,2 MB"},
    {"Documento": "Indicadores de resultado.xlsx", "Tipo": "Indicadores", "Expediente": "EXP-2026-003", "Estado": "Pendiente", "Tamaño": "644 KB"},
]

SOURCES = [
    {"Norma": "Reglamento (UE) 2021/1060", "Ámbito": "Disposiciones comunes", "Estado": "Referencia base", "Aplicación": "RDC / fondos 2021-2027"},
    {"Norma": "Reglamento (UE) 2021/1058", "Ámbito": "FEDER y Fondo de Cohesión", "Estado": "Referencia específica", "Aplicación": "Operaciones FEDER"},
    {"Norma": "Reglamento (UE) 2021/1057", "Ámbito": "FSE+", "Estado": "Referencia específica", "Aplicación": "Operaciones FSE+"},
    {"Norma": "Normativa nacional aplicable", "Ámbito": "Elegibilidad / contratación / ayudas", "Estado": "Según expediente", "Aplicación": "Control complementario"},
]

REPORT_ROWS = [
    {"Expediente": "EXP-2026-001", "Resultado": "Con observaciones", "Cobertura documental": "86%", "Controles": 18, "Incidencias": 3},
    {"Expediente": "EXP-2026-002", "Resultado": "Correcto", "Cobertura documental": "94%", "Controles": 16, "Incidencias": 1},
    {"Expediente": "EXP-2026-003", "Resultado": "Requiere revisión", "Cobertura documental": "72%", "Controles": 14, "Incidencias": 5},
]


def set_route(route: str) -> None:
    st.session_state["screen"] = route


def enter_demo() -> None:
    st.session_state["demo_entered"] = True
    st.session_state["screen"] = "dashboard"


def exit_demo() -> None:
    st.session_state["demo_entered"] = False
    st.session_state["screen"] = "dashboard"
    st.session_state["review_step"] = 1


def set_review_step(step: int) -> None:
    st.session_state["review_step"] = max(1, min(4, int(step)))


def render_intro() -> None:
    logo = str(LOGO_WHITE) if LOGO_WHITE.exists() else None
    left, right = st.columns([1.08, .92], gap=None)
    st.markdown('<div class="intro-shell-marker"></div>', unsafe_allow_html=True)
    # Use columns inside a visual shell. The contents remain native Streamlit elements.
    with left:
        st.markdown('<div style="background:linear-gradient(135deg,#031C3A,#0750A4);border-radius:28px 0 0 28px;padding:3.2rem 3.2rem 2.8rem;min-height:700px;color:white;position:relative;overflow:hidden">', unsafe_allow_html=True)
        if logo:
            st.image(logo, width=330)
        st.markdown('<div class="intro-rule"></div>', unsafe_allow_html=True)
        st.markdown('<h1 style="color:white;font-size:3.1rem;line-height:1.03;letter-spacing:-.035em;margin:1.5rem 0 1rem">Revisión técnica<br>de justificaciones</h1>', unsafe_allow_html=True)
        st.markdown('<p style="color:#DDE9F7;font-size:1.08rem;line-height:1.6;max-width:650px">Explora una versión demostrativa de EUROMIQ: expedientes, documentación, revisión técnica, informes y base normativa con datos ficticios.</p>', unsafe_allow_html=True)
        st.markdown('<div class="intro-badges"><span class="intro-badge">Demo pública</span><span class="intro-badge">Solo lectura</span><span class="intro-badge">Sin datos reales</span></div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-top:8rem;color:#C7D9EE;font-size:.76rem;letter-spacing:.12em;text-transform:uppercase">Gestión más transparente de los fondos europeos</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div style="background:linear-gradient(180deg,#0B58B6,#06366C);border-radius:0 28px 28px 0;padding:4.2rem 3rem;min-height:700px;color:white">', unsafe_allow_html=True)
        st.markdown('<div class="intro-label">Demo pública · solo lectura</div>', unsafe_allow_html=True)
        st.markdown('<h2 style="color:white;font-size:2.2rem;margin:.6rem 0">Explora EUROMIQ</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#D6E3F4;line-height:1.55">La navegación reproduce la estructura de la aplicación real, pero no guarda cambios, no utiliza Neon y no permite subir documentos.</p>', unsafe_allow_html=True)
        st.markdown('<div class="intro-feature"><div class="intro-lock">✓</div><div><strong>Datos ficticios</strong><span>Ningún expediente o usuario real.</span></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="intro-feature"><div class="intro-lock">✓</div><div><strong>Navegación completa</strong><span>Panel, expedientes, documentos, informes y normativa.</span></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="intro-feature"><div class="intro-lock">✓</div><div><strong>Sin persistencia</strong><span>Todo se reinicia al recargar la sesión.</span></div></div>', unsafe_allow_html=True)
        st.button("Entrar en la demo  →", type="primary", use_container_width=True, on_click=enter_demo, key="enter_demo")
        st.markdown('</div>', unsafe_allow_html=True)


def render_sidebar(active: str) -> None:
    with st.sidebar:
        if LOGO_WHITE.exists():
            st.image(str(LOGO_WHITE), use_container_width=True)
        st.markdown('<div class="demo-pill">● Demo pública · solo lectura</div>', unsafe_allow_html=True)
        items = [
            ("dashboard", "⌂ Panel de inicio"),
            ("workspace", "▣ Nueva revisión"),
            ("cases", "▤ Expedientes"),
            ("documents", "▥ Documentos"),
            ("reports", "▦ Informes"),
            ("sources", "▱ Base normativa"),
            ("settings", "⚙ Configuración"),
        ]
        for route, label in items:
            st.button(
                label,
                key=f"nav_{route}",
                type="primary" if active == route else "secondary",
                use_container_width=True,
                on_click=set_route,
                args=(route,),
            )
        st.markdown('<div class="sidebar-kicker">Cuenta demo</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-account"><strong>Eva María Martínez</strong><span>EUROMIQ Demo</span></div>', unsafe_allow_html=True)
        st.caption("Entorno de demostración. No conectado a Neon.")
        st.button("↪ Salir de la demo", key="exit_demo", use_container_width=True, on_click=exit_demo)


def render_topbar(title: str, subtitle: str) -> None:
    st.markdown(
        f'<div class="topbar"><div><div class="topbar-title">{title}</div><div class="topbar-sub">{subtitle}</div></div><div class="topbar-demo">DEMO PÚBLICA · SOLO LECTURA</div></div>',
        unsafe_allow_html=True,
    )


def dashboard() -> None:
    render_sidebar("dashboard")
    render_topbar("Revisión técnica de justificaciones", "Control de fondos europeos con trazabilidad normativa y documental")
    st.markdown('<div class="eyebrow">Panel de inicio</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title2">Hola, Eva María</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-copy2">Visión general del trabajo de revisión. Todos los datos mostrados son ficticios y forman parte de esta demostración pública.</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3, gap="large")
    with a:
        st.markdown('<div class="kpi"><div class="kpi-label">Revisiones en curso</div><div class="kpi-value">3</div><div class="kpi-foot">2 con actividad reciente</div></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="kpi"><div class="kpi-label">Pendientes de revisión</div><div class="kpi-value">4</div><div class="kpi-foot">Prioridad técnica</div></div>', unsafe_allow_html=True)
    with c:
        st.markdown('<div class="kpi"><div class="kpi-label">Informes disponibles</div><div class="kpi-value">3</div><div class="kpi-foot">Muestras de resultado</div></div>', unsafe_allow_html=True)
    st.markdown("### Expedientes recientes")
    df = pd.DataFrame(CASES)[["id","project_name","fund","status","phase","updated_at"]]
    df.columns = ["Código","Expediente","Fondo","Estado","Fase actual","Actualizado"]
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown('<div class="readonly-note">Esta demo no crea, modifica ni elimina expedientes. Los botones de navegación sirven únicamente para explorar el flujo de la herramienta.</div>', unsafe_allow_html=True)


def render_stepper(step: int) -> None:
    labels = [(1,"Configurar","Perfil del expediente"),(2,"Documentos","Marco y evidencias"),(3,"Revisión","Controles y validación"),(4,"Informe","Resultados y trazabilidad")]
    html=['<div class="step-summary">']
    for num,title,sub in labels:
        cls="step-item active" if num==step else "step-item"
        html.append(f'<div class="{cls}"><div class="step-num">{num}</div><div><b>{title}</b><span>{sub}</span></div></div>')
    html.append('</div>')
    st.markdown(''.join(html), unsafe_allow_html=True)


def workspace() -> None:
    render_sidebar("workspace")
    render_topbar("Revisión técnica de justificaciones", "Flujo guiado de revisión por expediente")
    st.markdown('<div class="eyebrow">Expediente de revisión</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title2">Primera evaluación de la justificación</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-copy2">Ejemplo interactivo del flujo de trabajo. Puedes avanzar y retroceder entre fases, pero ningún cambio se guarda.</div>', unsafe_allow_html=True)
    step = int(st.session_state.get("review_step", 1))
    render_stepper(step)
    st.markdown('<div class="readonly-note">Modo demo: los controles se muestran con valores de ejemplo. No se cargan ni procesan archivos reales.</div>', unsafe_allow_html=True)

    if step == 1:
        main, side = st.columns([1.75,.85], gap="large")
        with main:
            with st.container(border=True):
                st.markdown("### Configuración del expediente")
                c1,c2 = st.columns(2)
                with c1:
                    st.selectbox("Estado miembro", ["España"], disabled=True)
                    st.selectbox("Fondo", ["FEDER"], disabled=True)
                    st.selectbox("Fase de justificación", ["Intermedia / parcial"], disabled=True)
                    st.selectbox("Vía de selección / concesión", ["Convocatoria competitiva"], disabled=True)
                with c2:
                    st.selectbox("Modalidad de costes", ["Costes reales"], disabled=True)
                    st.selectbox("Contratación / proveedores", ["Sí"], disabled=True)
                    st.selectbox("Ayuda de Estado / de minimis", ["No"], disabled=True)
                    st.selectbox("Evaluación ambiental / screening", ["Sí"], disabled=True)
                st.button("Continuar a documentos →", type="primary", use_container_width=True, on_click=set_review_step, args=(2,), key="step1_next")
        with side:
            st.markdown('<div class="panel-card"><div class="panel-head"><div class="panel-icon">≋</div><div><div class="panel-title">Perfil de la revisión</div><div class="panel-copy">Parámetros de ejemplo.</div></div></div><div class="profile-row"><span class="profile-label">Estado miembro</span><span class="profile-value">España</span></div><div class="profile-row"><span class="profile-label">Fondo</span><span class="profile-value">FEDER</span></div><div class="profile-row"><span class="profile-label">Fase</span><span class="profile-value">Intermedia</span></div><div class="profile-row"><span class="profile-label">Costes</span><span class="profile-value">Costes reales</span></div><div class="profile-row"><span class="profile-label">Contratación</span><span class="profile-value ok">Aplica</span></div><div class="profile-row"><span class="profile-label">Ayuda de Estado</span><span class="profile-value">No aplica</span></div></div>', unsafe_allow_html=True)
    elif step == 2:
        st.markdown("### Documentos del expediente")
        st.markdown('<div class="fake-upload"><div class="ico">⇧</div><b>Zona de carga desactivada en la demo pública</b><span>La aplicación real permite incorporar documentación del expediente para su revisión técnica.</span></div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame(DOCUMENTS[:4]), use_container_width=True, hide_index=True)
        a,b=st.columns([1,2])
        a.button("← Volver a configurar", use_container_width=True, on_click=set_review_step, args=(1,), key="step2_back")
        b.button("Continuar a revisión →", type="primary", use_container_width=True, on_click=set_review_step, args=(3,), key="step2_next")
    elif step == 3:
        st.markdown("### Revisión técnica guiada")
        rows = pd.DataFrame([
            {"Área":"Elegibilidad","Control":"Periodo y operación elegible","Estado":"Localizado","Evidencia":"Memoria técnica"},
            {"Área":"Contratación","Control":"Procedimiento y concurrencia","Estado":"Parcial","Evidencia":"Contrato + expediente"},
            {"Área":"Costes","Control":"Trazabilidad financiera","Estado":"Localizado","Evidencia":"Justificación de costes"},
            {"Área":"Indicadores","Control":"Resultados e indicadores","Estado":"Pendiente","Evidencia":"No localizada"},
            {"Área":"Publicidad","Control":"Comunicación y visibilidad","Estado":"Localizado","Evidencia":"Informe de ejecución"},
        ])
        st.dataframe(rows, use_container_width=True, hide_index=True)
        c1,c2,c3 = st.columns(3)
        c1.metric("Controles revisados", "18")
        c2.metric("Con evidencia", "14")
        c3.metric("A revisar", "4")
        a,b=st.columns([1,2])
        a.button("← Volver a documentos", use_container_width=True, on_click=set_review_step, args=(2,), key="step3_back")
        b.button("Generar informe de muestra →", type="primary", use_container_width=True, on_click=set_review_step, args=(4,), key="step3_next")
    else:
        st.markdown("### Informe de muestra")
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Cobertura RDC", "91%")
        c2.metric("Cobertura nacional", "84%")
        c3.metric("Cobertura documental", "86%")
        c4.metric("Controles", "18")
        st.markdown("#### Prioridades de revisión")
        st.markdown("- **Contratación** — completar la evidencia de concurrencia y motivación del procedimiento.\n- **Indicadores** — incorporar soporte de resultados e indicadores.\n- **Trazabilidad financiera** — validar correspondencia entre gasto declarado y soporte de pago.")
        sample = {"expediente":"EXP-2026-001","resultado":"Con observaciones","cobertura_documental":86,"controles":18,"modo":"demo"}
        st.download_button("Descargar JSON de muestra", json.dumps(sample, ensure_ascii=False, indent=2), file_name="euromiq_demo_informe.json", mime="application/json")
        a,b=st.columns(2)
        a.button("← Volver a revisión", use_container_width=True, on_click=set_review_step, args=(3,), key="step4_back")
        b.button("Ir a Informes →", type="primary", use_container_width=True, on_click=set_route, args=("reports",), key="step4_reports")


def cases_screen() -> None:
    render_sidebar("cases")
    render_topbar("Expedientes", "Gestión y seguimiento de expedientes de fondos europeos")
    st.markdown('<div class="eyebrow">Expedientes</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title2">Histórico de revisiones</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-copy2">Muestra de expedientes con distintas fases de trabajo. No se pueden crear ni eliminar registros desde la demo pública.</div>', unsafe_allow_html=True)
    df = pd.DataFrame(CASES)
    shown = df[["id","project_name","fund","status","phase","updated_at"]].copy()
    shown.columns=["Código","Título del expediente","Fondo","Estado","Fase actual","Última actualización"]
    st.dataframe(shown, use_container_width=True, hide_index=True)
    selected = st.selectbox("Ver detalle del expediente", [c["id"] for c in CASES], key="demo_case_select")
    case = next(c for c in CASES if c["id"] == selected)
    with st.container(border=True):
        st.markdown(f"### {case['id']} · {case['project_name']}")
        a,b,c,d=st.columns(4)
        a.metric("Fondo", case["fund"])
        b.metric("Estado", case["status"])
        c.metric("Fase", case["phase"])
        d.metric("Importe", case["amount"])
        st.caption(f"Beneficiario: {case['beneficiary']} · Última actualización: {case['updated_at']}")


def documents_screen() -> None:
    render_sidebar("documents")
    render_topbar("Documentos", "Centro documental de expedientes y evidencias")
    st.markdown('<div class="eyebrow">Documentación</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title2">Documentos y evidencias</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-copy2">Vista demostrativa del repositorio documental asociado a los expedientes.</div>', unsafe_allow_html=True)
    st.markdown('<div class="fake-upload"><div class="ico">⇧</div><b>Subida desactivada en la demo pública</b><span>En la versión operativa, los documentos se incorporan al expediente y se utilizan durante la revisión.</span></div>', unsafe_allow_html=True)
    f1,f2=st.columns(2)
    type_filter=f1.selectbox("Tipo", ["Todos"]+sorted({d["Tipo"] for d in DOCUMENTS}))
    case_filter=f2.selectbox("Expediente", ["Todos"]+sorted({d["Expediente"] for d in DOCUMENTS}))
    data=DOCUMENTS
    if type_filter!="Todos": data=[d for d in data if d["Tipo"]==type_filter]
    if case_filter!="Todos": data=[d for d in data if d["Expediente"]==case_filter]
    st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)


def reports_screen() -> None:
    render_sidebar("reports")
    render_topbar("Informes", "Resultados de la revisión técnica de justificaciones")
    st.markdown('<div class="eyebrow">Informes</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title2">Resultados y soporte a la justificación</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-copy2">Ejemplos ficticios de resultados agregados e informes por expediente.</div>', unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    c1.metric("Expedientes revisados","3")
    c2.metric("Justificaciones correctas","1")
    c3.metric("Con observaciones","2")
    st.dataframe(pd.DataFrame(REPORT_ROWS), use_container_width=True, hide_index=True)
    chart = pd.DataFrame({"Correcta":[8,11,14,18,21,26],"Con observaciones":[4,5,6,7,8,9],"Requiere revisión":[2,3,4,4,5,6]}, index=["May","Jun","Jul","Ago","Sep","Oct"])
    st.markdown("#### Evolución de revisiones (datos ficticios)")
    st.bar_chart(chart, use_container_width=True)


def sources_screen() -> None:
    render_sidebar("sources")
    render_topbar("Base normativa", "Estructura de referencia para la revisión técnica")
    st.markdown('<div class="eyebrow">Base normativa</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title2">Normativa integrada</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-copy2">La aplicación organiza las fuentes por nivel normativo y por contexto del expediente. Esta pantalla utiliza una selección ilustrativa.</div>', unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(SOURCES), use_container_width=True, hide_index=True)
    with st.container(border=True):
        st.markdown("### Jerarquía de trabajo")
        st.markdown("**RDC → Reglamento específico del fondo → Programa y criterios de selección → Convocatoria / instrumento → Condiciones de apoyo → Normativa nacional y horizontal → Evidencias del expediente**")
        st.caption("La demo ilustra la arquitectura. La evaluación técnica final depende siempre del marco aplicable al expediente concreto.")


def settings_screen() -> None:
    render_sidebar("settings")
    render_topbar("Configuración", "Parámetros de la demostración")
    st.markdown('<div class="eyebrow">Configuración</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title2">Entorno de demostración</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-copy2">Esta versión está diseñada exclusivamente para mostrar la experiencia de uso sin exponer datos, usuarios ni infraestructura de producción.</div>', unsafe_allow_html=True)
    a,b = st.columns(2, gap="large")
    with a:
        with st.container(border=True):
            st.markdown("### Seguridad de la demo")
            st.markdown("- Sin conexión a Neon\n- Sin `DATABASE_URL`\n- Sin usuarios reales\n- Sin carga de archivos\n- Sin escritura persistente\n- Sin secretos de producción")
    with b:
        with st.container(border=True):
            st.markdown("### Datos mostrados")
            st.markdown("Todos los expedientes, documentos, indicadores y resultados son ficticios. Se incluyen únicamente para demostrar el flujo de EUROMIQ.")
    st.info("Para volver a la portada pública utiliza «Salir de la demo» en el menú lateral.")


if "demo_entered" not in st.session_state:
    st.session_state["demo_entered"] = False
if "screen" not in st.session_state:
    st.session_state["screen"] = "dashboard"
if "review_step" not in st.session_state:
    st.session_state["review_step"] = 1

if not st.session_state["demo_entered"]:
    render_intro()
else:
    screen = st.session_state.get("screen", "dashboard")
    if screen == "workspace":
        workspace()
    elif screen == "cases":
        cases_screen()
    elif screen == "documents":
        documents_screen()
    elif screen == "reports":
        reports_screen()
    elif screen == "sources":
        sources_screen()
    elif screen == "settings":
        settings_screen()
    else:
        dashboard()
