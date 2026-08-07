from sklearn.ensemble import RandomForestClassifier
import numpy as np
import streamlit as st
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
model = RandomForestClassifier()
model.fit(X, y)

st.title("Iris Species Prediction ")

sepal_length = st.number_input("Sepal Length (cm)")
sepal_width = st.number_input("Sepal Width (cm)")
petal_length = st.number_input("Petal Length (cm)")
petal_width = st.number_input("Petal Width (cm)")
predict=st.button("Predict Species")

if predict:
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    species = iris.target_names[prediction][0]
    st.write(f"The predicted species is: {species}")

st.markdown("---")
st.write("Adjust the input values and click the 'Predict Species' button to see the predicted species of the Iris flower based on the provided measurements.")
