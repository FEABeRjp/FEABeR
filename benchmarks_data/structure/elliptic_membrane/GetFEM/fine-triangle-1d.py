import getfem as gf
import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

# Parameters
Emodulus = 210000.0 * 0.1  # Young Modulus (N/mm2) * depth(mm)
nu = 0.3  # Poisson Coefficient
clambda = Emodulus * nu / ((1.0 + nu) * (1.0 - 2.0 * nu))
mu = Emodulus / (2.0 * (1 + nu))

mesh = gf.Mesh("load", "./mesh/fine-triangle-1d.msh")

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

F = mfrhs.eval("[10.0 * 0.1, 0.0, 0.0, 10.0 * 0.1]")  # F (N/mm2) * depth (mm)

md = gf.Model("real")
md.add_fem_variable("u", mfu)
md.add_initialized_fem_data("NeumannData", mfrhs, F)
md.add_initialized_data("E", Emodulus)
md.add_initialized_data("nu", nu)
md.add_isotropic_linearized_elasticity_pstress_brick(mim, "u", "E", "nu")
md.add_normal_source_term_brick(mim, "u", "NeumannData", OUTER_BOUND)
# md.add_source_term(mim, "(Reshape(NeumannData,qdim(u),meshdim)*Normal).Test_u", OUTER_BOUND)
md.assembly()
RHS = md.rhs()
md.add_initialized_data("r1", [0, 0])
md.add_initialized_data("r2", [0, 0])
md.add_initialized_data("H1", [[1, 0], [0, 0]])
md.add_initialized_data("H2", [[0, 0], [0, 1]])
md.add_generalized_Dirichlet_condition_with_multipliers(
    mim, "u", mfu, LEFT_BOUND, "r1", "H1"
)
md.add_generalized_Dirichlet_condition_with_multipliers(
    mim, "u", mfu, BOTTOM_BOUND, "r2", "H2"
)
md.solve()
U = md.variable("u")
grad_u = gf.compute_gradient(mfu, U, mfd)
sigmayy = clambda * (grad_u[0, 0] + grad_u[1, 1]) + 2.0 * mu * grad_u[1, 1]
mfu.export_to_vtk(
    "fine-triangle-1d.vtk", "ascii", mfd, sigmayy, "sigmayy", mfu, RHS, "RHS", U, "U"
)

m = pv.read("fine-triangle-1d.vtk")
pl = pv.Plotter()
pl.add_mesh(m, show_edges=True, line_width=2, scalars="sigmayy")
pl.add_point_labels(
    m.points[8], [str(m["sigmayy"][8])], point_size=10, font_size=20, text_color="white"
)

for i in [18, 20, 22, 24, 26, 30, 32]:
    pl.add_point_labels(
        m.points[i],
        ["( " + str(m["RHS"][:, 0][i]) + ", " + str(m["RHS"][:, 1][i]) + ") "],
        point_size=10,
        font_size=20,
        text_color="white",
    )

pl.show(cpos="xy", screenshot="fine-triangle-1d.png")
