import streamlit as st


def main():
    st.title('ThePodAI')

    # Text input field
    text_input = st.text_input(label='LabelHidden', label_visibility='hidden', placeholder='Enter prompt here Eg: The rise of use of GPUs')
    st.divider()
    host_input = st.radio('Choose voice', ['Male', 'Female'])
    st.divider()
    duration = st.slider('Duration of content (mins)', 2, 5)
    # Button to print text
    if st.button('Start'):
        print([text_input, host_input, duration])

    return [text_input, host_input, duration]

if __name__ == '__main__':
    main()
