import streamlit as st
import pandas as pd
import numpy as np
import random


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
	st.title('Naughty or Nice?')
	st.text('Click the button to check if you are on the naughty or nice list!')


nn_list = ["https://imgaz2.staticbg.com/thumb/view/oaupload/banggood/images/1B/EC/40dab768-5728-4640-9029-014a38081db9.jpg",
		   "https://cdn10.bigcommerce.com/s-npe4l/products/1154/images/1319/B-HOL-NICE---HIGH__27383.1477602932.1280.1280.jpg?c=2"]



if st.button('check'):	
	result = random.randint(1, 2)
	if result == 1:
		st.image(
           	"https://imgaz2.staticbg.com/thumb/view/oaupload/banggood/images/1B/EC/40dab768-5728-4640-9029-014a38081db9.jpg",
            width=400, # Manually Adjust the width of the image as per requirement
        )
	elif result == 2:
		st.image(
           	"https://cdn10.bigcommerce.com/s-npe4l/products/1154/images/1319/B-HOL-NICE---HIGH__27383.1477602932.1280.1280.jpg?c=2",
            width=400, # Manually Adjust the width of the image as per requirement
        )





