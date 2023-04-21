# import libraries
import numpy as np
import pandas as pd
import lightgbm as lgb
import streamlit as st
from PIL import Image
import os

# title
st.markdown('## Otto Recommender: Predict Next 20 Orders')

# instructions
st.markdown('Please choose userid from 13000001 to 13010000')

# userid input (13000001 to 13100000)
userid = st.number_input('User ID', min_value=13000001, max_value=13010000)    

# function to predict
def pred_data(userid):
    # load the LightGBM model from binary file
    model_path = os.path.join(os.path.dirname(__file__), 'model.txt')
    ranker = lgb.Booster(model_file=model_path)

    # import preprocessed dataset
    test = pd.read_parquet('./test_deploy.parquet')

    # preprocess test data
    feature_cols = test.columns[2:]
    test = test[test['session'] == userid]
    X_test = test[feature_cols]
    
    # make predictions
    scores = ranker.predict(X_test)

    # create new DataFrame with scores
    reranker_candidates_features = test.copy()
    reranker_candidates_features['score'] = scores

    # rank items by score within each session
    reranker_predictions = reranker_candidates_features.sort_values(['session', 'score'], ascending=[True, False])
    reranker_predictions = reranker_predictions.groupby('session').head(20)
    reranker_predictions = reranker_predictions.groupby('session')['aid'].apply(list).reset_index()

    prediction = reranker_predictions['aid']
    prediction_str = ", ".join(str(x) for x in prediction)[1:-1]
    return prediction_str


# predict button
if st.button('Predict'):
    prediction = pred_data(userid)
    st.markdown(f'**User {userid}**')
    st.markdown(f'### Empfehlungen für dich:')
    prediction_list = prediction.split(', ')
    for i, aid in enumerate(prediction_list):

        # display the aid value below the box image
        st.write(f'Product {i+1}: {aid}')

st.write('')
st.write('')
st.write('')
st.write('')

# explanation
st.markdown(f'*This app predicts the next 20 orders for the user on the Otto ecommerce platform with a recall score of 0.62. More info here: [github](https://github.com/chanhaosheng/project-submissions/blob/main/capstone)*')