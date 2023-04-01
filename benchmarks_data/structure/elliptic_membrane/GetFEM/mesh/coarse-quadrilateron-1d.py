import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

mesh = gf.Mesh("empty", 2)
gt = gf.GeoTrans("GT_QK(2,1)")
x = [
    2.12968779,
    1.78302097,
    2.0,
    2.41700006,
    1.16499996,
    1.36939037,
    0.0,
    0.0,
    2.83276558,
    3.25,
    1.78299999,
    0.0,
]
y = [
    0.748563945,
    0.453000009,
    0.0,
    0.0,
    0.812830687,
    1.30441773,
    1.58299994,
    1.0,
    1.34800005,
    0.0,
    2.29920578,
    2.75,
]
mesh.add_convex(gt, [[x[0], x[1], x[3], x[2]], [y[0], y[1], y[3], y[2]]])
mesh.add_convex(gt, [[x[4], x[5], x[7], x[6]], [y[4], y[5], y[7], y[6]]])
mesh.add_convex(gt, [[x[8], x[0], x[9], x[3]], [y[8], y[0], y[9], y[3]]])
mesh.add_convex(gt, [[x[10], x[5], x[8], x[0]], [y[10], y[5], y[8], y[0]]])
mesh.add_convex(gt, [[x[5], x[10], x[6], x[11]], [y[5], y[10], y[6], y[11]]])
mesh.add_convex(gt, [[x[5], x[4], x[0], x[1]], [y[5], y[4], y[0], y[1]]])
mesh.save("coarse-quadrilateron-1d.msh")
mesh.export_to_vtk("coarse-quadrilateron-1d.vtk", "ascii")

mesh = pv.read("coarse-quadrilateron-1d.vtk")

plotter = pv.Plotter()
plotter.add_mesh(mesh)
plotter.add_mesh(
    mesh.separate_cells().extract_feature_edges(),
    show_edges=True,
    line_width=3,
    color="black",
)
plotter.add_points(
    mesh.points, render_points_as_spheres=True, point_size=10.0, color="red"
)
plotter.show(cpos="xy", screenshot="coarse-quadrilateron-1d.png")
