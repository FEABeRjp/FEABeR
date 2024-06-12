import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

mesh = gf.Mesh("empty", 2)
gt = gf.GeoTrans("GT_Q2_INCOMPLETE(2)")
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
    1.95635438,
    1.94499898,
    2.20849991,
    2.34407163,
    1.26719522,
    0.71696496,
    0.0,
    0.611832142,
    2.48122668,
    2.83349991,
    3.14396143,
    1.57619524,
    1.8002671,
    2.37534261,
    0.930445969,
    0.0,
    1.51729536,
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
    0.600781977,
    0.232905,
    0.0,
    0.385926574,
    1.05862427,
    1.51175106,
    1.29149997,
    0.952058494,
    1.04828203,
    0.0,
    0.696732461,
    1.80181181,
    1.05625403,
    1.87690723,
    2.63489246,
    2.16650009,
    0.651501119,
]

mesh.add_convex(
    gt,
    [
        [x[0], x[12], x[1], x[15], x[13], x[3], x[14], x[2]],
        [y[0], y[12], y[1], y[15], y[13], y[3], y[14], y[2]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[4], x[16], x[5], x[19], x[17], x[7], x[18], x[6]],
        [y[4], y[16], y[5], y[19], y[17], y[7], y[18], y[6]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[8], x[20], x[0], x[22], x[15], x[9], x[21], x[3]],
        [y[8], y[20], y[0], y[22], y[15], y[9], y[21], y[3]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[10], x[23], x[5], x[25], x[24], x[8], x[20], x[0]],
        [y[10], y[23], y[5], y[25], y[24], y[8], y[20], y[0]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[5], x[23], x[10], x[17], x[26], x[6], x[27], x[11]],
        [y[5], y[23], y[10], y[17], y[26], y[6], y[27], y[11]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[5], x[16], x[4], x[24], x[28], x[0], x[12], x[1]],
        [y[5], y[16], y[4], y[24], y[28], y[0], y[12], y[1]],
    ],
)

mesh.save("coarse-quadrilateron-2d.msh")
mesh.export_to_vtk("coarse-quadrilateron-2d.vtk", "ascii")

mesh = pv.read("coarse-quadrilateron-2d.vtk")

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
plotter.show(cpos="xy", screenshot="coarse-quadrilateron-2d.png")
