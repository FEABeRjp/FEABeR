import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

# Parameters
Emodulus = 210000.0  # Young Modulus (N/mm2)
nu = 0.3  # Poisson Coefficient

mesh = gf.Mesh("empty", 2)
gt = gf.GeoTrans("GT_QK(2,1)")
mesh.add_convex(gt, [[0.0, 1.0, 0.0, 2.0], [1.0, 0.0, 2.0, 0.0]])

fb1 = mesh.outer_faces_with_direction([-1.0, 0.0], 0.01)
fb2 = mesh.outer_faces_with_direction([0.0, -1.0], 0.01)
fb3 = mesh.outer_faces_with_direction([1.0, 1.0], np.pi / 4.0 - 0.01)

LEFT_BOUND = 1
BOTTOM_BOUND = 2
OUTER_BOUND = 3

mesh.set_region(LEFT_BOUND, fb1)
mesh.set_region(BOTTOM_BOUND, fb2)
mesh.set_region(OUTER_BOUND, fb3)

elements_degree = 1

mfu = gf.MeshFem(mesh, 2)
mfd = gf.MeshFem(mesh, 1)
mfrhs = gf.MeshFem(mesh, 2)
mfu.set_classical_fem(elements_degree)
mfd.set_classical_fem(elements_degree)
mfrhs.set_classical_fem(elements_degree)

mim = gf.MeshIm(mesh, elements_degree * 2)

mesh.export_to_vtk("check.vtk", "ascii")

m = pv.read("check.vtk")
pl = pv.Plotter()
pl.add_mesh(m, show_edges=True)
pl.show(cpos="xy")

mesh.
