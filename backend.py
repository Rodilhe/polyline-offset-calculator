import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x_curve = None
y_curve = None
total_size = 0.0

def loadData(file_path):
    global x_curve, y_curve, total_size
    data = pd.read_csv(file_path)
    print("DataFrame Columns:", data.columns)
    print("First Lines DataFrame:\n", data.head())
    x_curve = data.iloc[:, 0].values  
    y_curve = data.iloc[:, 1].values  
    total_size = 0.0
    for i in range(len(x_curve) - 1):
        x1, y1 = x_curve[i], y_curve[i]
        x2, y2 = x_curve[i + 1], y_curve[i + 1]
        total_size += distanceCalculate(x1, y1, x2, y2)

def distanceCalculate(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def closestPointCalculation(x1, y1, x2, y2, x_user, y_user):
    dx = x2 - x1
    dy = y2 - y1
    l2 = dx * dx + dy * dy
    
    if l2 == 0:
        return x1, y1, distanceCalculate(x_user, y_user, x1, y1)
    
    t = max(0, min(1, ((x_user - x1) * dx + (y_user - y1) * dy) / l2))
    x_proj = x1 + t * dx
    y_proj = y1 + t * dy
    distance = distanceCalculate(x_user, y_user, x_proj, y_proj)
    return x_proj, y_proj, distance

def calculateStation(x_coords, y_coords, closest_x, closest_y):
    if len(x_coords) < 2 or closest_x is None or closest_y is None:
        return 0.0
    station = 0.0
    closest_segment_idx = -1
    min_distance = float('inf')

    for i in range(len(x_coords) - 1):
        x1, y1 = x_coords[i], y_coords[i]
        x2, y2 = x_coords[i + 1], y_coords[i + 1]
        x_proj, y_proj, distance = closestPointCalculation(x1, y1, x2, y2, closest_x, closest_y)
        if distance < min_distance:
            min_distance = distance
            closest_segment_idx = i

    for i in range(closest_segment_idx):
        x1, y1 = x_coords[i], y_coords[i]
        x2, y2 = x_coords[i + 1], y_coords[i + 1]
        station += distanceCalculate(x1, y1, x2, y2)

    if closest_segment_idx >= 0:
        x1, y1 = x_coords[closest_segment_idx], y_coords[closest_segment_idx]
        x2, y2 = x_coords[closest_segment_idx + 1], y_coords[closest_segment_idx + 1]
        dx = x2 - x1
        dy = y2 - y1
        l2 = dx * dx + dy * dy
        if l2 != 0:
            t = max(0, min(1, ((closest_x - x1) * dx + (closest_y - y1) * dy) / l2))
            segment_distance = t * distanceCalculate(x1, y1, x2, y2)
            station += segment_distance
    
    return station

def generateGraph():
    global x_curve, y_curve, total_size
    if x_curve is None or y_curve is None:
        print("Please, load the csv file first!")
        return

    fig, ax = plt.subplots()
    ax.plot(x_curve, y_curve, '-o', label=f'Polyline Size: {total_size:.2f} units')
    ax.set_title('Polyline Offset Calculator')
    ax.legend()

    pointUser = None
    pointClosest = None

    def onclick(event):
        global pointUser, pointClosest
        x_user, y_user = event.xdata, event.ydata
        if x_user is None or y_user is None:
            return

        offset = float('inf')
        xClosest, yClosest = None, None
        closest_segment_idx = -1
        
        for i in range(len(x_curve) - 1):
            x1, y1 = x_curve[i], y_curve[i]
            x2, y2 = x_curve[i + 1], y_curve[i + 1]
            x_proj, y_proj, distance = closestPointCalculation(x1, y1, x2, y2, x_user, y_user)
            
            if distance < offset:
                offset = distance
                xClosest, yClosest = x_proj, y_proj
                closest_segment_idx = i

        station = calculateStation(x_curve, y_curve, xClosest, yClosest)

        pointClosest = (xClosest, yClosest)
        pointUser = (x_user, y_user)

        ax.cla()
        ax.plot(x_curve, y_curve, '--k', label=f'Offset: {offset:.2f} units')
        ax.plot(x_curve, y_curve, '-o', label=f'Polyline Size: {total_size:.2f} units')

        if closest_segment_idx >= 0:
            x_station = x_curve[:closest_segment_idx + 1].tolist()
            y_station = y_curve[:closest_segment_idx + 1].tolist()
            x_station.append(xClosest)
            y_station.append(yClosest)
            ax.plot(x_station, y_station, '-o', linewidth=2, alpha=0.5, label=f'Station: {station:.2f} units')
        
        ax.plot(x_user, y_user, 'ro', label=f'User Point (x, y): {x_user:.1f}, {y_user:.1f}')
        ax.plot(xClosest, yClosest, 'go', label=f'Closest Point in Polyline (x, y): {xClosest:.1f}, {yClosest:.1f}')
        ax.plot([x_user, xClosest], [y_user, yClosest], 'k--')
        #ax.set_title(f'Polyline Size: {total_size:.2f} units\nOffset: {offset:.2f} units')
        ax.set_title('Polyline Offset Calculator')
        ax.legend()
        plt.draw()

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()