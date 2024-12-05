# Base image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy Python scripts into the container
# COPY /1_interact1.py .    # ----> 1st file...
# COPY /2_interact2.py .    # ----> 2nd file...
# COPY 3_api_cat_fact.py . 
 # ----> 3rd file...
COPY localDB.py .          

# Install required Python libraries
# RUN pip install requests
# [
RUN pip install pymysql   
RUN pip install cryptography
# ]

# Command to run the desired Python script
# CMD ["python", "interact1.py"]
# CMD ["python", "interact2.py"]
# CMD ["python", "3_api_cat_fact.py"]
CMD ["python", "localDB.py"]
