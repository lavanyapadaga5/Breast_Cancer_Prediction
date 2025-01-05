# Breast_Cancer_Prediction

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved model
breast_cancer_model = pickle.load(open('breast_cancer_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Breast Cancer Prediction'],
                           icons=['person'],
                           default_index=0)

# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        radius_mean = st.text_input('Mean Radius')
        
    with col2:
        texture_mean = st.text_input('Mean Texture')
        
    with col3:
        perimeter_mean = st.text_input('Mean Perimeter')
        
    with col1:
        area_mean = st.text_input('Mean Area')
        
    with col2:
        smoothness_mean = st.text_input('Mean Smoothness')
        
    with col3:
        compactness_mean = st.text_input('Mean Compactness')
        
    with col1:
        symmetry_mean = st.text_input('Mean Symmetry')
        
    with col2:
        fractal_dimension_mean = st.text_input('Mean Fractal Dimension')
    
    # code for Prediction
    cancer_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        try:
            cancer_prediction = breast_cancer_model.predict(
                [[float(radius_mean), float(texture_mean), float(perimeter_mean), 
                  float(area_mean), float(smoothness_mean), float(compactness_mean), 
                  float(symmetry_mean), float(fractal_dimension_mean)]]
            )
            
            if cancer_prediction[0] == 1:
                cancer_diagnosis = 'The person is likely to have breast cancer (Malignant)'
            else:
                cancer_diagnosis = 'The person is unlikely to have breast cancer (Benign)'
        
        except ValueError:
            cancer_diagnosis = 'Please provide valid numeric inputs for all fields.'
        
    st.success(cancer_diagnosis)
