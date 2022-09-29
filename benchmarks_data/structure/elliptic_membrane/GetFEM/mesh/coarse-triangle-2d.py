import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

mesh = gf.Mesh("empty", 2)
gt = gf.GeoTrans("GT_PK(2,2)")
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
    2.1000104,
    2.20849991,
    2.34407163,
    1.26719522,
    0.71696496,
    0.684695184,
    0.0,
    0.611832142,
    2.48122668,
    2.68984389,
    2.83349991,
    3.14396143,
    1.57619524,
    2.10107803,
    2.37534261,
    1.8002671,
    0.891499996,
    0.930445969,
    0.0,
    1.51729536,
    1.64734387,
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
    0.226500005,
    0.0,
    0.385926574,
    1.05862427,
    1.51175106,
    1.15220881,
    1.29149997,
    0.952058494,
    1.04828203,
    0.374281973,
    0.0,
    0.696732461,
    1.80181181,
    1.32620883,
    1.87690723,
    1.05625403,
    1.94110286,
    2.63489246,
    2.16650009,
    0.651501119,
    0.780697346,
]

mesh.add_convex(
    gt,
    [[x[2], x[15], x[3], x[13], x[14], x[1]], [y[2], y[15], y[3], y[13], y[14], y[1]]],
)
mesh.add_convex(
    gt,
    [[x[0], x[12], x[1], x[16], x[14], x[3]], [y[0], y[12], y[1], y[16], y[14], y[3]]],
)
mesh.add_convex(
    gt,
    [[x[6], x[20], x[7], x[18], x[19], x[5]], [y[6], y[20], y[7], y[18], y[19], y[5]]],
)
mesh.add_convex(
    gt,
    [[x[4], x[17], x[5], x[21], x[19], x[7]], [y[4], y[17], y[5], y[21], y[19], y[7]]],
)
mesh.add_convex(
    gt,
    [[x[3], x[24], x[9], x[16], x[23], x[0]], [y[3], y[24], y[9], y[16], y[23], y[0]]],
)
mesh.add_convex(
    gt,
    [[x[8], x[22], x[0], x[25], x[23], x[9]], [y[8], y[22], y[0], y[25], y[23], y[9]]],
)
mesh.add_convex(
    gt,
    [[x[0], x[22], x[8], x[29], x[27], x[5]], [y[0], y[22], y[8], y[29], y[27], y[5]]],
)
mesh.add_convex(
    gt,
    [
        [x[10], x[26], x[5], x[28], x[27], x[8]],
        [y[10], y[26], y[5], y[28], y[27], y[8]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[5], x[26], x[10], x[18], x[30], x[6]],
        [y[5], y[26], y[10], y[18], y[30], y[6]],
    ],
)
mesh.add_convex(
    gt,
    [
        [x[10], x[31], x[11], x[30], x[32], x[6]],
        [y[10], y[31], y[11], y[30], y[32], y[6]],
    ],
)
mesh.add_convex(
    gt,
    [[x[1], x[12], x[0], x[33], x[34], x[4]], [y[1], y[12], y[0], y[33], y[34], y[4]]],
)
mesh.add_convex(
    gt,
    [[x[5], x[17], x[4], x[29], x[34], x[0]], [y[5], y[17], y[4], y[29], y[34], y[0]]],
)

mesh.save("coarse-triangle-2d.msh")
mesh.export_to_vtk("coarse-triangle-2d.vtk", "ascii")

mesh = pv.read("coarse-triangle-2d.vtk")

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
plotter.show(cpos="xy", screenshot="coarse-triangle-2d.png")
