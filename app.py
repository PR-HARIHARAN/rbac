import streamlit as st

# Simulated token-role map
USER_ROLES = {
    "Admin": "admin",
    "Analyst": "analyst",
    "Viewer": "viewer"
}

# Simulated data access functions
def access_postgres():
    """Logic for Postgres"""
    return "✅ Query result from **PostgreSQL**."

def access_vector_db():
    """Logic for vectordb"""
    return "🔍 Vector search result from **Vector DB**."

def access_website_data():
    """Logic for website data"""
    return "🌐 Scraped result from **Website Data**."

# Role-based access logic
def query_llm(source: str, role: str):
    if source == "SQL":
        if role in ("admin", "analyst"):
            return access_postgres()
        else:
            return "❌ Access denied to **SQL data**."

    elif source == "Vector DB":
        if role in ("admin", "analyst"):
            return access_vector_db()
        else:
            return "❌ Access denied to **Vector DB**."

    elif source == "Website":
        if role in ("admin", "viewer"):
            return access_website_data()
        else:
            return "❌ Access denied to **Website data**."

    return "⚠️ Unknown data source."

# --- Streamlit App UI ---
st.set_page_config(page_title="RBAC Data Access", layout="centered")
st.title("🔐 Role-Based LLM Data Access Demo")

st.markdown("Choose a **role** and a **data source** to simulate access control.")

role_choice = st.selectbox("Select your role", list(USER_ROLES.keys()))
source_choice = st.radio("Choose data source", ["SQL", "Vector DB", "Website"], horizontal=True)

if st.button("🔍 Query"):
    user_role = USER_ROLES[role_choice]
    result = query_llm(source_choice, user_role)
    
    if result.startswith("✅") or result.startswith("🔍") or result.startswith("🌐"):
        st.success(result)
    else:
        st.error(result)
