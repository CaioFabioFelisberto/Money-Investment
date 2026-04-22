import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests

def get_last_ipca():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"

    try:
        response = requests.get(url)
        data = response.json()

        last_value = data[-1]
        ipca_rate = float(last_value['valor'])

        return ipca_rate
    except Exception as e:
        print(f"Error : {e}")
        return None

def get_last_selic():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json"

    try:
        response = requests.get(url)
        data = response.json()

        last_value = data[0]
        selic_rate = float(last_value['valor'])

        return selic_rate / 12
    except Exception as e:
        print(f"Error : {e}")
        return None

def get_last_savings_rate():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.196/dados/ultimos/1?formato=json"

    try:
        response = requests.get(url)
        data = response.json()

        last_value = data[0]
        savings_rate = float(last_value['valor'])

        return savings_rate / 12
    except Exception as e:
        print(f"Error : {e}")
        return None

def selic_plot(amount, months):
    monthly_contribution = float(amount)
    time = np.arange(1, int(months) + 1)
    selic = get_last_selic() / 100
    inflation = get_last_ipca() / 100

    selic_balance = monthly_contribution * (((1 + selic) ** time) - 1) / selic
    inflation_balance = monthly_contribution * (((1 + inflation) ** time) - 1) / inflation
    real_balance = selic_balance - inflation_balance

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=selic_balance, mode='lines', name='SELIC Balance'))
    fig.add_trace(go.Scatter(x=time, y=inflation_balance, mode='lines', name='Inflation Balance'))
    fig.add_trace(go.Scatter(x=time, y=real_balance, mode='lines', name='Real Balance'))
    fig.update_layout(title='SELIC vs Inflation Balance Over Time',
                      xaxis_title='Months',
                      yaxis_title='Balance (R$)',
                      legend_title='Legend')
    
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def plot_heritage_composition(amount, months):

    total_contributions = float(amount) * int(months)
    selic = get_last_selic() / 100

    final_balance = float(amount) * (((1 + selic) ** int(months)) - 1) / selic

    total_fees = final_balance - total_contributions

    labels_slices = ['Total Contributions', 'Interest Earned']
    values_slices = [total_contributions, total_fees]

    fig = go.Figure(data=[go.Pie(labels=labels_slices, values=values_slices, hole=.3, marker_colors=['#2ca02c', '#1f77b4'])])
    
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def plot_savings_composition(amount, months):

    savings_rate = get_last_savings_rate() / 100
    selic = get_last_selic() / 100
    months_vector = np.arange(1, int(months) + 1)

    final_balance = float(amount) * (((1 + savings_rate) ** months_vector) - 1) / savings_rate
    selic_balance = float(amount) * (((1 + selic) ** months_vector) - 1) / selic

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months_vector, y=final_balance, mode='lines', name='Savings Balance'))
    fig.add_trace(go.Scatter(x=months_vector, y=selic_balance, mode='lines', name='SELIC Balance'))
    fig.update_layout(title='Savings vs SELIC Balance Over Time',
                      xaxis_title='Months',
                      yaxis_title='Balance (R$)',
                      legend_title='Legend')
    
    return fig.to_html(full_html=False, include_plotlyjs='cdn')
