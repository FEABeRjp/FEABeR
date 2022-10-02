import getfem as gf
import numpy as np

# Parameters
Emodulus = 210000.0  # Young Modulus
nu = 0.3  # Poisson Coefficient

mesh = gf.Mesh("load", "./mesh/coarse-quadrilateron-1d.msh")

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
mfrhs = gf.MeshFem(mesh, 2)
mfu.set_classical_fem(elements_degree)
mfrhs.set_classical_fem(elements_degree)

mim = gf.MeshIm(mesh, elements_degree * 2)

F = mfrhs.eval("[10.0, 0.0, 0.0, 10.0]")

md = gf.Model("real")
md.add_fem_variable("u", mfu)
md.add_initialized_fem_data("NeumannData", mfrhs, F)
md.add_initialized_data("E", Emodulus)
md.add_initialized_data("nu", nu)
md.add_isotropic_linearized_elasticity_pstrain_brick(mim, "u", "E", "nu")
md.add_normal_source_term_brick(mim, "u", "NeumannData", OUTER_BOUND)
# md.add_source_term(mim, "(Reshape(NeumannData,qdim(u),meshdim)*Normal).Test_u", OUTER_BOUND)
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
md.assembly("build_all")
