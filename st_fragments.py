import streamlit as st

st.title('Streamlit Fragments')


count = 0
st.write(f'Count: {count}')

with st.spinner('Wait for it...'):
    import time
    time.sleep(5)

# It will rerun the whole app (default streamlit behaviour)
if st.button('Run whole'):
    st.write('Rerun whole app')

# It will rerun the whole app (default streamlit behaviour)
st.checkbox('Check me')

# It will run this fragment only not the whole app
@st.fragment
def print_specific():
    if st.button('Print fragment'):
        st.write('I hope you learnt something!')
print_specific()

# It will run this fragment only not the whole app
@st.fragment
def run_specific():
    if st.button('Run specific fragment'):
        global count
        count += 1
        st.write('Run specific fragment only')
        st.write(f'Count: {count}')
run_specific()

# It will rerun the whole app (default streamlit behaviour)
st.selectbox('Check',['a','b'])
