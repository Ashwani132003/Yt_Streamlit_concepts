import streamlit as st

st.title('Streamlit Fragments')

st.session_state.count = 0
st.write(f'Count: {st.session_state.count}')

# It will rerun the whole app (default streamlit behaviour)
if st.button('Run whole'):
    st.write('Rerun whole app')


# It will run this fragment only not the whole app
@st.fragment
def run_specific():
    if st.button('Run specific fragment'):

        st.session_state.count += 1
        st.write('Run specific fragment only')
        st.write(f'Count: {st.session_state.count}')


run_specific()

# It will run this fragment only not the whole app
@st.fragment
def print_specific():
    if st.button('Print fragment'):
        st.write('I hope you learnt something!')
print_specific()