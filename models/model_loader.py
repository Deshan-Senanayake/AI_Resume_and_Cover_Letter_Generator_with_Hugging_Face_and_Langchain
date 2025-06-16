from transformers import pipeline
import torch

# Set device (GPU if available, otherwise CPU)
device = 0 if torch.cuda.is_available() else -1

# Cache the model to prevent reloading on every button click
import streamlit as st

@st.cache_resource(show_spinner="Loading model...")
def load_text_generator(model_name="tiiuae/falcon-7b-instruct"):
    return pipeline(
        "text-generation",
        model=model_name,
        device=device,
        model_kwargs={
            "temperature": 0.7,
            "max_new_tokens": 512,
            "top_p": 0.9
        }
    )
