"""

"""
###############################################################################

import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

###############################################################################

E = 1.0  # Young Modulus
nu = 1.0/3.0  # Poisson ratio
elements_degree = 2  # Degree of the finite element methods
F = 1.00/16.0  # Force density at the right boundary

###############################################################################
# TODO: 三角形メッシュの方向を揃えられないか確認する。

xn = 4
yn = 4
mesh = gf.Mesh("regular simplices", range(xn+1), range(yn+1))
pts = mesh.pts()
x = mesh.pts()[0, :]
y = mesh.pts()[1, :]
pts[0, :] = x * 44.0 / xn
pts[1, :] = 44.0 / xn * x + (44.0 - (44.0 - 16.0) / xn * x) / yn * y
mesh.set_pts(pts)

###############################################################################

fb1 = mesh.outer_faces_with_direction([1.0, 0.0], 0.01)
fb2 = mesh.outer_faces_with_direction([-1.0, 0.0], 0.01)

RIGHT_BOUND = 1
LEFT_BOUND = 2

mesh.set_region(RIGHT_BOUND, fb1)
mesh.set_region(LEFT_BOUND, fb2)

###############################################################################

mesh.export_to_vtk("mesh.vtk", "ascii")

grid = pv.read("mesh.vtk")
points = grid.points
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(grid, show_edges=True)
plotter.add_point_labels(
    points, points.tolist(), point_size=10, font_size=10, always_visible=True
)
plotter.show(cpos="xy", screenshot="mesh.png")

###############################################################################

mfu = gf.MeshFem(mesh, 2)
mfu.set_classical_fem(elements_degree)
mim = gf.MeshIm(mesh, elements_degree * 2)

###############################################################################

md = gf.Model("real")
md.add_fem_variable("u", mfu)
md.add_initialized_data("E", [E])
md.add_initialized_data("nu", [nu])
md.add_initialized_data("F", [0.0, F])
md.add_isotropic_linearized_elasticity_brick_pstress(mim, "u", "E", "nu")
md.add_source_term_brick(mim, "u", "F", RIGHT_BOUND)
md.add_Dirichlet_condition_with_simplification("u", LEFT_BOUND)

###############################################################################

md.solve()

###############################################################################

U = md.variable("u")
mfu.export_to_vtk("displacement.vtk", "ascii", mfu, U, "Displacement")

###############################################################################

result = pv.read("displacement.vtk")
warped = result.warp_by_vector()

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(warped, scalars="Displacement", cmap='turbo')
plotter.add_text("Max:" + str(np.round(np.max(U), 2)str())
plotter.show(cpos="xy", screenshot="displacement.png")

