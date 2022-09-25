import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

mesh = gf.Mesh("empty", 2)
gt = gf.GeoTrans("GT_QK(2,1)")
x = [
    2.12968779,
    1.78302097,
    2.00000000,
    2.41700006,
    1.16499996,
    1.36939037,
    0.00000000,
    0.00000000,
    2.83276558,
    3.25000000,
    1.78299999,
    0.00000000,
]
y = [
    0.748563945,
    0.453000009,
    0.000000000,
    0.000000000,
    0.812830687,
    1.304417730,
    1.582999940,
    1.000000000,
    1.348000050,
    0.000000000,
    2.299205780,
    2.750000000,
]
mesh.add_convex(gt, [[x[0], x[1], x[3], x[2]], [y[0], y[1], y[3], y[2]]])
mesh.add_convex(gt, [[x[4], x[5], x[7], x[6]], [y[4], y[5], y[7], y[6]]])
mesh.add_convex(gt, [[x[8], x[0], x[9], x[3]], [y[8], y[0], y[9], y[3]]])
mesh.add_convex(gt, [[x[10], x[5], x[8], x[0]], [y[10], y[5], y[8], y[0]]])
mesh.add_convex(gt, [[x[5], x[10], x[6], x[11]], [y[5], y[10], y[6], y[11]]])
mesh.add_convex(gt, [[x[5], x[4], x[0], x[1]], [y[5], y[4], y[0], y[1]]])
mesh.save("quadrilateron-coarse.msh")
mesh.export_to_vtk("quadrilateron-coarse.vtk", "ascii")

m = pv.read("quadrilateron-coarse.vtk")
m.plot(cpos="xy", show_edges=True, screenshot="quadrilateron-coarse.png")
