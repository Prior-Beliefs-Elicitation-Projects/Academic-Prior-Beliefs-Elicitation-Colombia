import streamlit_survey as ss
import streamlit as st
import pandas as pd
from utils import *
from components import *
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


survey = ss.StreamlitSurvey()


# Initialize session state
initialize_session_state()

# Show introductory texts
show_titles_and_subtitles()

# Request of consent
consent_form()

if st.session_state['consent']:
    
    first_question()

    new_bins_df = first_question_grid()

    st.write(SUBTITLE_QUESTION_1_2)
    st.number_input('', min_value=0, max_value=100, key = 'input_question_1')
    # Professional Category Checkbox
    #st.selectbox('Specify your professional category:', ('Policymaker', 'Expert', 'Firm'), key="professional_category")
    
    #st.radio(EXPORT_IMPACT_DESCRIPTION, options=["Positive", "Negative", "No changes"], horizontal=False, key = 'export_impact')

    #percentage_of_expected_impact(st.session_state.export_impact)
    #probability_of_expected_impact(st.session_state.export_impact)
    #motivation()

    #if st.session_state.export_impact == "Positive":
    #    st.radio("Select one of the following options", options = ["Diversify the range of products exported", "Diversify the destinations of exportation", "All of the above"], key = 'export_outcome')

    submit = st.button("Submit", on_click = add_submission, args = (new_bins_df, ))


    if st.session_state['submit']:
        st.success("thank you for completing the Academic Prior Elicitation Survey!")

