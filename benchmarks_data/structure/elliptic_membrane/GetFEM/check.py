import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

mesh = gf.Mesh("empty", 2)
gt = gf.GeoTrans("GT_QK(2,1)")
mesh.add_convex(gt, [[0.0, 1.0, 0.0, 2.0], [1.0, 0.0, 2.0, 0.0]])
mesh.export_to_vtk("check.vtk", "ascii")

m = pv.read("check.vtk")
pl = pv.Plotter()
pl.add_mesh(m, show_edges=True)
pl.show(cpos="xy")

