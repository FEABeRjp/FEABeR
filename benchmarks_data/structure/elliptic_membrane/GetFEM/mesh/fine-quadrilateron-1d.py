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
    1.95635438,
    1.93760836,
    2.20849991,
    2.33895946,
    1.26719522,
    0.699454725,
    0.0,
    0.590530932,
    2.48122668,
    2.83349991,
    3.14145494,
    1.57619524,
    1.78156114,
    2.36494803,
    0.920210361,
    0.0,
    1.49321365,
    2.13828373,
    0.644992828,
    2.7402072,
    2.07325459,
    0.809832573,
    1.63738739,
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
    0.24782756,
    0.0,
    0.399010003,
    1.05862427,
    1.51526558,
    1.29149997,
    0.955415249,
    1.04828203,
    0.0,
    0.704780996,
    1.80181181,
    1.06977248,
    1.88628185,
    2.63746476,
    2.16650009,
    0.66526556,
    0.323418766,
    1.23534048,
    0.551895499,
    1.47802711,
    2.07636523,
    0.867518961,
]
mesh.add_convex(gt, [[x[0], x[12], x[15], x[29]], [y[0], y[12], y[15], y[29]]])
mesh.add_convex(gt, [[x[12], x[1], x[29], x[13]], [y[12], y[1], y[29], y[13]]])
mesh.add_convex(gt, [[x[15], x[29], x[3], x[14]], [y[15], y[29], y[3], y[14]]])
mesh.add_convex(gt, [[x[29], x[13], x[14], x[2]], [y[29], y[13], y[14], y[2]]])
mesh.add_convex(gt, [[x[4], x[16], x[19], x[30]], [y[4], y[16], y[19], y[30]]])
mesh.add_convex(gt, [[x[16], x[5], x[30], x[17]], [y[16], y[5], y[30], y[17]]])
mesh.add_convex(gt, [[x[19], x[30], x[7], x[18]], [y[19], y[30], y[7], y[18]]])
mesh.add_convex(gt, [[x[30], x[17], x[18], x[6]], [y[30], y[17], y[18], y[6]]])
mesh.add_convex(gt, [[x[8], x[20], x[22], x[31]], [y[8], y[20], y[22], y[31]]])
mesh.add_convex(gt, [[x[20], x[0], x[31], x[15]], [y[20], y[0], y[31], y[15]]])
mesh.add_convex(gt, [[x[22], x[31], x[9], x[21]], [y[22], y[31], y[9], y[21]]])
mesh.add_convex(gt, [[x[31], x[15], x[21], x[3]], [y[31], y[15], y[21], y[3]]])
mesh.add_convex(gt, [[x[10], x[23], x[25], x[32]], [y[10], y[23], y[25], y[32]]])
mesh.add_convex(gt, [[x[23], x[5], x[32], x[24]], [y[23], y[5], y[32], y[24]]])
mesh.add_convex(gt, [[x[25], x[32], x[8], x[20]], [y[25], y[32], y[8], y[20]]])
mesh.add_convex(gt, [[x[32], x[24], x[20], x[0]], [y[32], y[24], y[20], y[0]]])
mesh.add_convex(gt, [[x[5], x[23], x[17], x[33]], [y[5], y[23], y[17], y[33]]])
mesh.add_convex(gt, [[x[23], x[10], x[33], x[26]], [y[23], y[10], y[33], y[26]]])
mesh.add_convex(gt, [[x[17], x[33], x[6], x[27]], [y[17], y[33], y[6], y[27]]])
mesh.add_convex(gt, [[x[33], x[26], x[27], x[11]], [y[33], y[26], y[27], y[11]]])
mesh.add_convex(gt, [[x[5], x[16], x[24], x[34]], [y[5], y[16], y[24], y[34]]])
mesh.add_convex(gt, [[x[16], x[4], x[34], x[28]], [y[16], y[4], y[34], y[28]]])
mesh.add_convex(gt, [[x[24], x[34], x[0], x[12]], [y[24], y[34], y[0], y[12]]])
mesh.add_convex(gt, [[x[34], x[28], x[12], x[1]], [y[34], y[28], y[12], y[1]]])
mesh.save("fine-quadrilateron-1d.msh")
mesh.export_to_vtk("fine-quadrilateron-1d.vtk", "ascii")

mesh = pv.read("fine-quadrilateron-1d.vtk")

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
plotter.show(cpos="xy", screenshot="fine-quadrilateron-1d.png")
