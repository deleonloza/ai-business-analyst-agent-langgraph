import streamlit as st
from agents.graph import graph

st.set_page_config(
    page_title="AI Business Analyst Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Business Analyst Agent")
st.write("Agentic AI System powered by LangGraph")

company = st.text_input("Introduce el nombre de una empresa", 
                        placeholder ="Ej: Tesla, Nvidia, Mercado Libre")

if st.button("Analizar empresa"):
    if not company:
        st.warning("Introduce una empresa primero.")
    else:
        with st.spinner("LangGraph workflow running"):
            final_state = graph.invoke({
                "company": company,
                "plan": "",
                "research": [],
                "analysis": "",
                "report": ""
            })
            
            plan = final_state["plan"]
            research = final_state["research"]
            analysis = final_state["analysis"]
            report = final_state["report"]
            
            st.header("Planner Agent")
            st.write(plan)
            
            st.header("Research Agent")
            for item in research:
                st.markdown(f"### Query: {item['query']}")
                
                if not item["results"]:
                    st.warning("No se encontrsron resultados para esta búsqueda.")
                
                for result in item["results"]:
                    st.markdown(f"**{result['title']}**")
                    
                    st.write(result["snippet"])
                    st.write(result["url"])
                    st.divider()
                    
            
            st.header("Analysis Agent")
            st.markdown(analysis)
            
            st.header("Executive Report")
            st.markdown(report)