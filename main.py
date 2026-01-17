import os
import smtplib
from typing import List, Optional
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import pandas as pd
from dotenv import load_dotenv
from jobspy import scrape_jobs

# LangChain Imports
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


# Load environment variables
load_dotenv()

# Configuration
RESUME = os.getenv("RESUME_TEXT", "")
SEARCH_TERM = "Software Engineer"
LOCATION = "Tokyo, Japan"
RESULT_LIMIT = 30
HOURS_OLD = 24
PROXY_URL = os.getenv("PROXY_URL", None)

# Define the output data structure from AI
class JobEvaluation(BaseModel):
    """
    Structure for job evaluation output.
    """

    score: int = Field(description="A relevance score from 0 to 100 based on the resume match and job preferences.")
    reason: str = Field(description="A concise, one-sentence reason for the score.")
