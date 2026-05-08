import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("Expense Tracking System")

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    # 1. Seleção da Data
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    
    # 2. Busca de dados na API baseada na data selecionada
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    # 3. O formulário usa uma chave dinâmica baseada na data para resetar ao mudar o dia
    with st.form(key=f"expense_form_{selected_date}"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Amount**")
        with col2:
            st.markdown("**Category**")
        with col3:
            st.markdown("**Notes**")

        expenses_input_data = []
        
        # Geramos 5 linhas de inputs
        for i in range(5):
            if i < len(existing_expenses):
                # Se existem dados, preenchemos com os valores da API
                amount = float(existing_expenses[i].get('amount', 0.0))
                category = existing_expenses[i].get('category', "Shopping")
                notes = existing_expenses[i].get('notes', "")
            else:
                # Caso contrário, valores padrão
                amount = 0.0
                category = "Shopping"
                notes = ""

            # Garante que a categoria vinda do banco existe na lista, senão usa a primeira
            cat_index = categories.index(category) if category in categories else 0

            col1, col2, col3 = st.columns(3)
            with col1:
                # A KEY do widget deve conter a DATA para forçar o reset visual
                amount_val = st.number_input(
                    label="Amount", 
                    min_value=0.0, 
                    step=1.0, 
                    value=amount, 
                    key=f"amount_{selected_date}_{i}",
                    label_visibility="collapsed"
                )
            with col2:
                category_val = st.selectbox(
                    label="Category", 
                    options=categories, 
                    index=cat_index,
                    key=f"category_{selected_date}_{i}", 
                    label_visibility="collapsed"
                )
            with col3:
                notes_val = st.text_input(
                    label="Notes", 
                    value=notes, 
                    key=f"notes_{selected_date}_{i}", 
                    label_visibility="collapsed"
                )

            expenses_input_data.append({
                'amount': amount_val,
                'category': category_val,
                'notes': notes_val
            })

        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            # Filtra apenas linhas onde o valor é maior que zero
            filtered_expenses = [e for e in expenses_input_data if e['amount'] > 0]

            # Envia o POST para a API
            post_response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            
            if post_response.status_code == 200:
                st.success(f"Expenses for {selected_date} updated successfully!")
                # Opcional: st.rerun() se quiser recarregar a página após salvar
            else:
                st.error(f"Failed to update expenses. Error: {post_response.status_code}")

with tab2:
    st.info("Analytics dashboard coming soon...")