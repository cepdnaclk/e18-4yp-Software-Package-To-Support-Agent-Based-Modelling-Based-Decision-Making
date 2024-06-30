import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from mesa import Agent, Model
from mesa.time import RandomActivation
from scipy.spatial import Delaunay
import base64
import io

# MeshSpace from space.py
class MeshSpace:
    def __init__(self, vertices):
        self.vertices = vertices
        self.tri = Delaunay(self.vertices[:, :2])
        self.triangles = self.tri.simplices
        self.neighbors = self.find_neighbors(self.tri)

    def find_neighbors(self, tri):
        # Initialize an empty list of neighbors for each triangle
        neighbors = [[] for _ in range(len(tri.simplices))]
        total_simplices = len(tri.simplices)

        # Iterate over each simplex (triangle) and its neighbors
        for i, simplex in enumerate(tri.simplices):
            # The neighbors of each simplex are stored in tri.neighbors
            for neighbor in tri.neighbors[i]:
                if neighbor != -1:
                    neighbors[i].append(int(neighbor))
            # Print progress
            if i % (total_simplices // 10) == 0:
                progress = (i / total_simplices) * 100
                print(f"\rProcessed {i} / {total_simplices} triangles ({progress:.2f}%)", end='', flush=True)

        return neighbors

    @staticmethod
    def plot_agent_movement(vertices, triangles, agent_history):
        mesh = plot_triangular_mesh(vertices, triangles)
        frames = []
        steps = []

        for step, agents in enumerate(agent_history):
            agent_positions = vertices[triangles[agents].flatten()].reshape(-1, 3) + [0, 0, 0.01]
            scatter = go.Scatter3d(
                x=agent_positions[:, 0],
                y=agent_positions[:, 1],
                z=agent_positions[:, 2],
                mode='markers',
                marker=dict(size=5, color='black'),
                name='Agents'
            )
            frames.append(go.Frame(data=[mesh, scatter], name=str(step)))
            steps.append({
                'args': [[str(step)], {'frame': {'duration': 500, 'redraw': True}, 'mode': 'immediate'}],
                'label': str(step),
                'method': 'animate'
            })

        fig = go.Figure(data=[mesh, frames[0].data[1]], frames=frames)
        fig.update_layout(
            updatemenus=[{
                'buttons': [
                    {'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}], 'label': 'Play', 'method': 'animate'},
                    {'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}], 'label': 'Pause', 'method': 'animate'}
                ],
                'showactive': False,
                'type': 'buttons'
            }],
            sliders=[{
                'steps': steps,
                'currentvalue': {'prefix': 'Step: '}
            }],
            height=800,
            width=1200
        )
        return fig

# Visualization Functions
def plot_triangular_mesh(vertices, triangles):
    mesh = go.Mesh3d(
        x=vertices[:, 0],
        y=vertices[:, 1],
        z=vertices[:, 2],
        i=triangles[:, 0],
        j=triangles[:, 1],
        k=triangles[:, 2],
        color='lightblue',
        opacity=0.50,
        flatshading=True,
        name='Mesh'
    )
    return mesh

# Define the Agent Class
class MeshAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.position = None
        self.data = {
            'elevation': [],
            'composition': [],
            'temperature': []
        }

    def step(self):
        # Simulate agent movement
        current_triangle = self.model.space.triangles[self.position]
        current_height = self.model.space.vertices[current_triangle].mean(axis=0)[2]
        neighbor_heights = [self.model.space.vertices[self.model.space.triangles[n]].mean(axis=0)[2] for n in self.model.space.neighbors[self.position]]

        # Find neighbor with lowest height
        min_neighbor_idx = np.argmin(neighbor_heights)
        min_neighbor = self.model.space.neighbors[self.position][min_neighbor_idx]

        # Move agent to neighbor with lowest height
        if neighbor_heights[min_neighbor_idx] < current_height:
            self.position = min_neighbor % len(self.model.space.triangles)  # Ensure agent index stays within bounds

        # Collect data at the current position
        self.collect_data(current_triangle)

    def collect_data(self, current_triangle):
        vertices = self.model.space.vertices[current_triangle]
        self.data['elevation'].append(vertices[:, 2].mean())
        self.data['composition'].append(self.model.space.vertices[current_triangle, 2].mean())  # Placeholder for composition
        self.data['temperature'].append(self.model.space.vertices[current_triangle, 2].mean())  # Placeholder for temperature

# Define the Model Class
class MeshModel(Model):
    def __init__(self, num_agents, vertices):
        super().__init__()
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)
        
        # Set vertex data
        self.vertices = vertices
        self.space = MeshSpace(self.vertices)

        # Create agents
        for i in range(self.num_agents):
            agent = MeshAgent(i, self)
            self.schedule.add(agent)
            # Randomly place agents on triangles
            agent.position = np.random.randint(0, len(self.space.triangles))

    def step(self):
        self.schedule.step()

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Label('Upload File:', style={'margin-left': '20px'}),
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ], style={'display': 'flex', 'alignItems': 'center', 'margin-left': '10px'}),
                    style={
                        'width': '100%',  # Adjusted to take full width of the column
                        'height': '30px',
                        'lineHeight': '30px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    multiple=False
                )
            ], style={'display': 'flex', 'alignItems': 'center'}),
        ], width=4),
        dbc.Col([
            html.Div([
                html.Label('Number of Agents: ', style={'margin-right': '10px'}),
                dcc.Input(id='num_agents', type='number', value=20, min=1, step=1, style={'width': '100px'}),
            ], style={'display': 'flex', 'alignItems': 'center', 'margin': '10px'}),
        ], width=3),
        dbc.Col([
            html.Div([
                html.Label('Number of Steps: ', style={'margin-right': '10px'}),
                dcc.Input(id='num_steps', type='number', value=10, min=1, step=1, style={'width': '100px'}),
            ], style={'display': 'flex', 'alignItems': 'center', 'margin': '10px'}),
        ], width=3),
        dbc.Col([
            dbc.Button('Run Simulation', id='run_simulation', n_clicks=0, color='primary', className='ms-3', style={'margin': '10px'}),
        ], width=2),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Loading(
                id='loading',
                type='default',
                children=html.Div(dcc.Graph(id='simulation_graph', style={'height': '800px'}))
            )
        ], width=12)
    ])
])

def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        vertices = np.loadtxt(io.StringIO(decoded.decode('utf-8')))
        return vertices
    except Exception as e:
        print(e)
        return None

@app.callback(
    Output('upload-data', 'children'),
    Input('upload-data', 'filename')
)
def update_filename(filename):
    if filename is None:
        return html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ])
    return html.Div(filename)

@app.callback(
    Output('simulation_graph', 'figure'),
    Input('run_simulation', 'n_clicks'),
    State('num_agents', 'value'),
    State('num_steps', 'value'),
    State('upload-data', 'contents')
)
def update_simulation(n_clicks, num_agents, num_steps, contents):
    if n_clicks > 0:
        if contents is None:
            raise PreventUpdate

        vertices = parse_contents(contents)
        if vertices is None:
            return go.Figure()

        # Create the model and run the simulation
        model = MeshModel(num_agents, vertices)

        agent_history = []
        for i in range(num_steps):
            model.step()
            agent_positions = [agent.position for agent in model.schedule.agents]
            agent_history.append(agent_positions)

        # Plot the agent movement
        fig = MeshSpace.plot_agent_movement(model.vertices, model.space.triangles, agent_history)
        return fig
    else:
        return go.Figure()

if __name__ == '__main__':
    app.run_server(debug=True)
