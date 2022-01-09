"""

"""
###############################################################################

import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

###############################################################################

mesh = gf.Mesh("regular simplices", range(5), range(5))
pts = mesh.pts()
x = mesh.pts()[0, :]
y = mesh.pts()[1, :]
pts[0, :] = x * 44.0 / 4
pts[1, :] = 44.0 / 4 * x + (44.0 - (44.0 - 16.0) / 4 * x) / 4 * y
mesh.set_pts(pts)
mesh.export_to_vtk("mesh.vtk", "ascii")

grid = pv.read("mesh.vtk")
points = grid.points
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(grid, show_edges=True)
plotter.add_point_labels(
    points, points.tolist(), point_size=10, font_size=10, always_visible=True
)
plotter.show(cpos="xy", screenshot="mesh.png")
