"""

"""
###############################################################################

import getfem as gf
import pyvista as pv
import matplotlib.pyplot as plt

pv.set_plot_theme("document")

###############################################################################

E = 21e6  # Young Modulus(N/cm^2)
nu = 0.3  # Poisson ratio
alpha_th = 16.6e-6  # Thermal expansion coefficient(/K)
elements_degree = 2  # Degree of the finite element methods

###############################################################################

a = 5.0
b = 10.0
h = 0.5

mo1 = gf.MesherObject("ball", [0.0, 0.0], a)
mo2 = gf.MesherObject("ball", [0.0, 0.0], b)
mo3 = gf.MesherObject("half space", [0.0, 0.0], [-1.0, 0.0])
mo4 = gf.MesherObject("half space", [0.0, 0.0], [0.0, -1.0])

mo5 = gf.MesherObject("set minus", mo2, mo1)
mo6 = gf.MesherObject("set minus", mo5, mo3)
mo7 = gf.MesherObject("set minus", mo6, mo4)

mesh = gf.Mesh("generate", mo7, h, 2)

###############################################################################

fb1 = mesh.outer_faces_with_direction([-1.0, 0.0], 0.01)
fb2 = mesh.outer_faces_with_direction([0.0, -1.0], 0.01)

LEFT_BOUND = 1
BOTTOM_BOUND = 2

mesh.set_region(LEFT_BOUND, fb1)
mesh.set_region(BOTTOM_BOUND, fb2)

###############################################################################

mesh.export_to_vtk("mesh.vtk", "ascii")
grid = pv.read("mesh.vtk")

plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(grid, show_edges=True)

plotter.show(cpos="xy", screenshot="test_thermal_stress_mesh.png")

###############################################################################

mfu = gf.MeshFem(mesh, 2)
mfu.set_classical_fem(elements_degree)
mim = gf.MeshIm(mesh, elements_degree * 2)

###############################################################################

md = gf.Model("real")
md.add_fem_variable("u", mfu)
md.add_initialized_data("E", [E])
md.add_initialized_data("nu", [nu])
md.add_initialized_data("H1", [[1.0, 0.0], [0.0, 0.0]])
md.add_initialized_data("r1", [0.0, 0.0])
md.add_initialized_data("H2", [[0.0, 0.0], [0.0, 1.0]])
md.add_initialized_data("r2", [0.0, 0.0])

###############################################################################

md.add_generalized_Dirichlet_condition_with_multipliers(
    mim, "u", mfu, LEFT_BOUND, "r1", "H1"
)
md.add_generalized_Dirichlet_condition_with_multipliers(
    mim, "u", mfu, BOTTOM_BOUND, "r2", "H2"
)

###############################################################################

md.add_isotropic_linearized_elasticity_brick_pstress(mim, "u", "E", "nu")
md.add_macro("theta", "1.0*sqrt(X(1)*X(1)+X(2)*X(2))")
md.add_initialized_data("beta", [alpha_th * E / (1 - 2 * nu)])
md.add_linear_term(mim, "-(beta*theta)*Div_Test_u")

###############################################################################

md.solve()

###############################################################################

U = md.variable("u")
mfu.export_to_vtk("displacement.vtk", "ascii", mfu, U, "Displacement")

###############################################################################

result = pv.read("displacement.vtk")
cmap = plt.cm.get_cmap("gist_rainbow", 20)
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(result, scalars="Displacement", cmap=cmap)
plotter.show(cpos="xy", screenshot="test_thermal_stress_displacement.png")

###############################################################################
