import pandas as pd
import plotly.express as px



questions = data.columns


for question in questions:
    answer_counts = data[question].value_counts().reset_index()
    answer_counts.columns = ['answer', 'frequency']
    
    # Create a pie chart
    fig = px.pie(answer_counts, values='frequency', names='answer', title=f'{question}')
   
    #fig.show()
    print (answer_counts)
