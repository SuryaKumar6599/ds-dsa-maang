#1. Data Layer Exceptions
from unittest import case
import pandas as pd
import logging as logger

try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    logger.error("Dataset not found")
except pd.errors.EmptyDataError:
    logger.warning("Empty dataset")
except UnicodeDecodeError:
    logger.error("Encoding issue in dataset")
    
#2. Model Layer Exceptions
class ValidationError(Exception):
    pass

def validate_ic_sr(case):
    if "patient_age" not in case:
        raise ValidationError("Missing patient_age")
    
try:
    validate_ic_sr(case)
except ValidationError as e:
    logger.warning(f"Validation failed: {e}")
    
#3. Controller Layer Exceptions
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    logger.error("Model file missing")
except Exception as e:
    logger.critical(f"Model loading failed: {e}")
    
#4. API Layer Exceptions
import requests

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.Timeout:
    logger.error("API timeout")
except requests.exceptions.HTTPError as e:
    logger.error(f"HTTP error: {e}")
except requests.exceptions.RequestException:
    logger.error("General API failure")
    
#5. Deployment Layer Exceptions
try:
    doc = nlp(text)
except ValueError:
    logger.error("Invalid text input")
except RuntimeError:
    logger.error("spaCy pipeline crashed")
    
#6. Logging and Monitoring Exceptions
from sqlalchemy.exc import SQLAlchemyError

try:
    session.commit()
except SQLAlchemyError as e:
    session.rollback()
    logger.error(f"DB error: {e}")