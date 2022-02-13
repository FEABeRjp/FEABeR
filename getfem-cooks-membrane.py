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

xns = [2, 4, 8, 16]
yns = [2, 4, 8, 16]
meshs = []
for xn, yn in zip(xns, yns):
    mesh = gf.Mesh("regular simplices", range(xn+1), range(yn+1))
    pts = mesh.pts()
    x = mesh.pts()[0, :]
    y = mesh.pts()[1, :]
    pts[0, :] = x * 48.0 / xn
    pts[1, :] = 44.0 / xn * x + (44.0 - (44.0 - 16.0) / xn * x) / yn * y
    mesh.set_pts(pts)
    meshs.append(mesh)

###############################################################################

for mesh in meshs:
    fb1 = mesh.outer_faces_with_direction([1.0, 0.0], 0.01)
    fb2 = mesh.outer_faces_with_direction([-1.0, 0.0], 0.01)

    RIGHT_BOUND = 1
    LEFT_BOUND = 2

    mesh.set_region(RIGHT_BOUND, fb1)
    mesh.set_region(LEFT_BOUND, fb2)

###############################################################################

meshs[0].export_to_vtk("mesh0.vtk", "ascii")
meshs[1].export_to_vtk("mesh1.vtk", "ascii")
meshs[2].export_to_vtk("mesh2.vtk", "ascii")
meshs[3].export_to_vtk("mesh3.vtk", "ascii")

grid0 = pv.read("mesh0.vtk")
grid1 = pv.read("mesh1.vtk")
grid2 = pv.read("mesh2.vtk")
grid3 = pv.read("mesh3.vtk")
points0 = grid0.points
points1 = grid1.points
points2 = grid2.points
points3 = grid3.points

plotter = pv.Plotter(shape=(2, 2), off_screen=True)

plotter.subplot(0, 0)
plotter.add_text("2 x 2")
plotter.add_mesh(grid0, show_edges=True)
plotter.show_grid(grid="back", location="back", color="gray", all_edges=True)

plotter.subplot(0, 1)
plotter.add_text("4 x 4")
plotter.add_mesh(grid1, show_edges=True)
plotter.show_grid(grid="back", location="back", color="gray", all_edges=True)

plotter.subplot(1, 0)
plotter.add_text("8 x 8")
plotter.add_mesh(grid2, show_edges=True)
plotter.show_grid(grid="back", location="back", color="gray", all_edges=True)

plotter.subplot(1, 1)
plotter.add_text("16 x 16")
plotter.add_mesh(grid3, show_edges=True)
plotter.show_grid(grid="back", location="back", color="gray", all_edges=True)

plotter.show(cpos="xy", screenshot="mesh.png")

###############################################################################

mfus = []
mims = []
for mesh in meshs:
    mfu = gf.MeshFem(mesh, 2)
    mfu.set_classical_fem(elements_degree)
    mfus.append(mfu)
    mim = gf.MeshIm(mesh, elements_degree * 2)
    mims.append(mim)

###############################################################################

mds = []
for mfu, mim in zip(mfus, mims):
    md = gf.Model("real")
    md.add_fem_variable("u", mfu)
    md.add_initialized_data("E", [E])
    md.add_initialized_data("nu", [nu])
    md.add_initialized_data("F", [0.0, F])
    md.add_isotropic_linearized_elasticity_brick_pstress(mim, "u", "E", "nu")
    md.add_source_term_brick(mim, "u", "F", RIGHT_BOUND)
    md.add_Dirichlet_condition_with_simplification("u", LEFT_BOUND)
    mds.append(md)

###############################################################################

for md in mds:
    md.solve()

###############################################################################

U0 = mds[0].variable("u")
mfu.export_to_vtk("displacement0.vtk", "ascii", mfus[0], U0, "Displacement")
U1 = mds[1].variable("u")
mfu.export_to_vtk("displacement1.vtk", "ascii", mfus[1], U1, "Displacement")
U2 = mds[2].variable("u")
mfu.export_to_vtk("displacement2.vtk", "ascii", mfus[2], U2, "Displacement")
U3 = mds[3].variable("u")
mfu.export_to_vtk("displacement3.vtk", "ascii", mfus[3], U3, "Displacement")

###############################################################################

result0 = pv.read("displacement0.vtk")
warped0 = result0.warp_by_vector()
result1 = pv.read("displacement1.vtk")
warped1 = result1.warp_by_vector()
result2 = pv.read("displacement2.vtk")
warped2 = result2.warp_by_vector()
result3 = pv.read("displacement3.vtk")
warped3 = result3.warp_by_vector()

plotter = pv.Plotter(shape=(2, 2), off_screen=True)

plotter.subplot(0, 0)
plotter.add_mesh(warped0, scalars="Displacement", cmap='turbo')
plotter.add_text("Max:" + str(np.round(np.max(U0), 2)))
plotter.subplot(0, 1)
plotter.add_mesh(warped1, scalars="Displacement", cmap='turbo')
plotter.add_text("Max:" + str(np.round(np.max(U1), 2)))
plotter.subplot(1, 0)
plotter.add_mesh(warped2, scalars="Displacement", cmap='turbo')
plotter.add_text("Max:" + str(np.round(np.max(U2), 2)))
plotter.subplot(1, 1)
plotter.add_mesh(warped3, scalars="Displacement", cmap='turbo')
plotter.add_text("Max:" + str(np.round(np.max(U3), 2)))
plotter.show(cpos="xy", screenshot="displacement.png") 
